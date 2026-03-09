"""
MediaWiki MCP Server
Connects Claude to your Real Neat Solutions wiki at Hostinger.
Uses MediaWiki Action API with BotPasswords authentication.
"""

import asyncio
import json
import os
from typing import Optional, Any
import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, ConfigDict

# ── Config ──────────────────────────────────────────────────────────────────
WIKI_URL = os.environ.get("WIKI_URL", "https://palegreen-starling-721736.hostingersite.com")
API_URL  = f"{WIKI_URL}/api.php"

BOT_USER = os.environ.get("WIKI_BOT_USER", "")   # e.g. "Admin@mybot"
BOT_PASS = os.environ.get("WIKI_BOT_PASS", "")   # BotPassword secret

# ── MCP Server ───────────────────────────────────────────────────────────────
mcp = FastMCP("mediawiki_mcp")


# ── Shared HTTP client & session management ───────────────────────────────────
_client: Optional[httpx.AsyncClient] = None
_session_cookies: dict = {}


async def get_client() -> httpx.AsyncClient:
    global _client
    if _client is None or _client.is_closed:
        _client = httpx.AsyncClient(
            timeout=30.0,
            follow_redirects=True,
            headers={"User-Agent": "RealNeatSolutions-MCP/1.0 (MediaWiki bot)"}
        )
    return _client


async def api_get(params: dict) -> dict:
    client = await get_client()
    params["format"] = "json"
    r = await client.get(API_URL, params=params, cookies=_session_cookies)
    r.raise_for_status()
    data = r.json()
    # Save any new cookies
    _session_cookies.update(dict(r.cookies))
    if "error" in data:
        raise ValueError(f"API error: {data['error'].get('info', data['error'])}")
    return data


async def api_post(params: dict) -> dict:
    client = await get_client()
    params["format"] = "json"
    r = await client.post(API_URL, data=params, cookies=_session_cookies)
    r.raise_for_status()
    data = r.json()
    _session_cookies.update(dict(r.cookies))
    if "error" in data:
        raise ValueError(f"API error: {data['error'].get('info', data['error'])}")
    return data


async def ensure_logged_in() -> bool:
    """Log in via BotPasswords if credentials are set and we aren't already."""
    if not BOT_USER or not BOT_PASS:
        return False
    # Check current login state
    info = await api_get({"action": "query", "meta": "userinfo"})
    user = info["query"]["userinfo"]
    if "anon" not in user:
        return True  # Already logged in

    # Step 1: get login token
    token_data = await api_get({"action": "query", "meta": "tokens", "type": "login"})
    login_token = token_data["query"]["tokens"]["logintoken"]

    # Step 2: log in
    result = await api_post({
        "action": "login",
        "lgname": BOT_USER,
        "lgpassword": BOT_PASS,
        "lgtoken": login_token,
    })
    if result.get("login", {}).get("result") != "Success":
        raise ValueError(f"Login failed: {result.get('login', {}).get('reason', 'unknown')}")
    return True


async def get_csrf_token() -> str:
    await ensure_logged_in()
    data = await api_get({"action": "query", "meta": "tokens"})
    return data["query"]["tokens"]["csrftoken"]


def _truncate(text: str, max_len: int = 8000) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len] + f"\n\n[... truncated, {len(text) - max_len} chars omitted]"


# ── Input models ─────────────────────────────────────────────────────────────

class PageTitleInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., description="Wiki page title (e.g. 'Projects/RNS Videomedia' or 'Main Page')", min_length=1)


class SearchInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    query: str = Field(..., description="Full-text search query", min_length=1)
    limit: int = Field(default=10, description="Max results to return", ge=1, le=50)
    namespace: Optional[int] = Field(default=None, description="Namespace ID to search in (0=main, 4=project, 10=template)")


class EditPageInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., description="Page title to create or edit", min_length=1)
    content: str = Field(..., description="Full wikitext content for the page", min_length=1)
    summary: str = Field(default="Edited via MCP", description="Edit summary shown in page history")
    create_only: bool = Field(default=False, description="If true, fail if page already exists")


class AppendPageInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., description="Page title to append content to", min_length=1)
    content: str = Field(..., description="Wikitext to append to the page", min_length=1)
    summary: str = Field(default="Appended via MCP", description="Edit summary")
    new_section_title: Optional[str] = Field(default=None, description="If set, creates a new section with this heading")


class MovePageInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    from_title: str = Field(..., description="Current page title", min_length=1)
    to_title: str = Field(..., description="New page title", min_length=1)
    reason: str = Field(default="Moved via MCP", description="Reason for move shown in logs")
    leave_redirect: bool = Field(default=True, description="Leave a redirect at the old title")


class CategoryInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    category: str = Field(..., description="Category name WITHOUT 'Category:' prefix (e.g. 'Projects')", min_length=1)
    limit: int = Field(default=50, description="Max pages to list", ge=1, le=500)


class ListPagesInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    prefix: Optional[str] = Field(default=None, description="List pages starting with this prefix")
    namespace: int = Field(default=0, description="Namespace ID (0=main, 4=project, 10=template)")
    limit: int = Field(default=50, description="Max pages to list", ge=1, le=500)


class DeletePageInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., description="Page title to delete", min_length=1)
    reason: str = Field(default="Deleted via MCP", description="Reason for deletion")


class UploadTextInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., description="Page title", min_length=1)
    content: str = Field(..., description="Full wikitext content", min_length=1)
    summary: str = Field(default="Created via MCP", description="Edit summary")


# ── Tools ─────────────────────────────────────────────────────────────────────

@mcp.tool(
    name="wiki_get_page",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_get_page(params: PageTitleInput) -> str:
    """
    Retrieve the wikitext source and metadata of a wiki page.
    Returns the raw wikitext, last editor, last edit time, and page URL.
    """
    data = await api_get({
        "action": "query",
        "titles": params.title,
        "prop": "revisions|info",
        "rvprop": "content|timestamp|user",
        "rvslots": "main",
        "inprop": "url",
    })
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if page.get("missing") is not None:
        return f"Page not found: '{params.title}'"

    revisions = page.get("revisions", [])
    if not revisions:
        return f"No revisions found for '{params.title}'"

    rev = revisions[0]
    content = rev.get("slots", {}).get("main", {}).get("*", rev.get("*", ""))
    timestamp = rev.get("timestamp", "unknown")
    editor = rev.get("user", "unknown")
    url = page.get("fullurl", f"{WIKI_URL}/index.php/{params.title.replace(' ', '_')}")

    result = f"# {params.title}\n"
    result += f"**URL:** {url}\n"
    result += f"**Last edited:** {timestamp} by {editor}\n\n"
    result += "## Content (wikitext)\n\n"
    result += _truncate(content)
    return result



@mcp.tool(
    name="wiki_search",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_search(params: SearchInput) -> str:
    """
    Full-text search across the wiki. Returns matching page titles, snippets, and URLs.
    Use this to find existing pages before creating new ones.
    """
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": params.query,
        "srlimit": params.limit,
        "srprop": "snippet|titlesnippet|size|wordcount",
    }
    if params.namespace is not None:
        search_params["srnamespace"] = params.namespace

    data = await api_get(search_params)
    results = data["query"]["search"]

    if not results:
        return f"No pages found matching '{params.query}'"

    lines = [f"## Search results for '{params.query}' ({len(results)} found)\n"]
    for r in results:
        title = r["title"]
        snippet = r.get("snippet", "").replace('<span class="searchmatch">', "**").replace("</span>", "**")
        url = f"{WIKI_URL}/index.php/{title.replace(' ', '_')}"
        lines.append(f"### [{title}]({url})")
        lines.append(f"  {snippet}\n")

    return "\n".join(lines)


@mcp.tool(
    name="wiki_list_pages",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_list_pages(params: ListPagesInput) -> str:
    """
    List all pages in the wiki, optionally filtered by prefix or namespace.
    Good for exploring the wiki structure.
    """
    ap_params = {
        "action": "query",
        "list": "allpages",
        "apnamespace": params.namespace,
        "aplimit": params.limit,
    }
    if params.prefix:
        ap_params["apprefix"] = params.prefix

    data = await api_get(ap_params)
    pages = data["query"]["allpages"]

    if not pages:
        return "No pages found."

    ns_names = {0: "Main", 4: "Project", 10: "Template", 14: "Category"}
    ns_label = ns_names.get(params.namespace, f"NS:{params.namespace}")
    lines = [f"## Pages in {ns_label} namespace ({len(pages)} found)\n"]
    for p in pages:
        url = f"{WIKI_URL}/index.php/{p['title'].replace(' ', '_')}"
        lines.append(f"- [{p['title']}]({url})")

    return "\n".join(lines)


@mcp.tool(
    name="wiki_list_category",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_list_category(params: CategoryInput) -> str:
    """
    List all pages in a wiki category.
    """
    data = await api_get({
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Category:{params.category}",
        "cmlimit": params.limit,
        "cmprop": "title|type",
    })
    members = data["query"]["categorymembers"]

    if not members:
        return f"Category '{params.category}' is empty or doesn't exist."

    lines = [f"## Category: {params.category} ({len(members)} members)\n"]
    for m in members:
        url = f"{WIKI_URL}/index.php/{m['title'].replace(' ', '_')}"
        mtype = m.get("type", "page")
        lines.append(f"- [{m['title']}]({url}) ({mtype})")

    return "\n".join(lines)


@mcp.tool(
    name="wiki_get_categories",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_get_categories(params: PageTitleInput) -> str:
    """
    Get all categories a page belongs to.
    """
    data = await api_get({
        "action": "query",
        "titles": params.title,
        "prop": "categories",
        "cllimit": 100,
    })
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if page.get("missing") is not None:
        return f"Page not found: '{params.title}'"

    cats = page.get("categories", [])
    if not cats:
        return f"'{params.title}' has no categories."

    lines = [f"## Categories for '{params.title}'\n"]
    for c in cats:
        name = c["title"].replace("Category:", "")
        lines.append(f"- {name}")
    return "\n".join(lines)


@mcp.tool(
    name="wiki_get_links",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_get_links(params: PageTitleInput) -> str:
    """
    Get all internal links on a page — useful for mapping wiki structure.
    """
    data = await api_get({
        "action": "query",
        "titles": params.title,
        "prop": "links",
        "pllimit": 200,
    })
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if page.get("missing") is not None:
        return f"Page not found: '{params.title}'"

    links = page.get("links", [])
    if not links:
        return f"'{params.title}' has no internal links."

    lines = [f"## Internal links on '{params.title}' ({len(links)} links)\n"]
    for l in links:
        url = f"{WIKI_URL}/index.php/{l['title'].replace(' ', '_')}"
        lines.append(f"- [{l['title']}]({url})")
    return "\n".join(lines)


@mcp.tool(
    name="wiki_recent_changes",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_recent_changes() -> str:
    """
    Show recent changes to the wiki (last 20 edits).
    """
    data = await api_get({
        "action": "query",
        "list": "recentchanges",
        "rclimit": 20,
        "rcprop": "title|user|timestamp|comment|sizes",
        "rctype": "edit|new",
    })
    changes = data["query"]["recentchanges"]

    if not changes:
        return "No recent changes found."

    lines = ["## Recent Changes\n"]
    for c in changes:
        url = f"{WIKI_URL}/index.php/{c['title'].replace(' ', '_')}"
        delta = c.get("newlen", 0) - c.get("oldlen", 0)
        delta_str = f"+{delta}" if delta >= 0 else str(delta)
        lines.append(f"- **[{c['title']}]({url})** — {c.get('user', '?')} at {c['timestamp']} ({delta_str} bytes) — _{c.get('comment', '')}_")

    return "\n".join(lines)


@mcp.tool(
    name="wiki_create_or_edit_page",
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True}
)
async def wiki_create_or_edit_page(params: EditPageInput) -> str:
    """
    Create a new wiki page or completely replace an existing page's content.
    Use wikitext format. Requires bot credentials.
    
    Wikitext tips:
    - == Heading == for sections
    - [[Link]] for internal links
    - [[Category:Name]] to add to category
    - '''bold''' and ''italic''
    - * for bullet lists, # for numbered lists
    """
    csrf = await get_csrf_token()

    edit_params: dict[str, Any] = {
        "action": "edit",
        "title": params.title,
        "text": params.content,
        "summary": params.summary,
        "token": csrf,
        "bot": "1",
    }
    if params.create_only:
        edit_params["createonly"] = "1"

    result = await api_post(edit_params)
    edit_result = result.get("edit", {})
    status = edit_result.get("result", "unknown")
    url = f"{WIKI_URL}/index.php/{params.title.replace(' ', '_')}"

    if status == "Success":
        action = "created" if edit_result.get("new") else "updated"
        return f"✅ Page {action}: [{params.title}]({url})\nRevision: {edit_result.get('newrevid', '?')}"
    else:
        return f"❌ Edit failed: {json.dumps(edit_result)}"


@mcp.tool(
    name="wiki_append_to_page",
    annotations={"readOnlyHint": False, "destructiveHint": False}
)
async def wiki_append_to_page(params: AppendPageInput) -> str:
    """
    Append content to an existing page without overwriting it.
    Optionally adds content as a new section. Requires bot credentials.
    """
    csrf = await get_csrf_token()

    edit_params: dict[str, Any] = {
        "action": "edit",
        "title": params.title,
        "summary": params.summary,
        "token": csrf,
        "bot": "1",
    }

    if params.new_section_title:
        edit_params["section"] = "new"
        edit_params["sectiontitle"] = params.new_section_title
        edit_params["text"] = params.content
    else:
        edit_params["appendtext"] = "\n" + params.content

    result = await api_post(edit_params)
    edit_result = result.get("edit", {})
    status = edit_result.get("result", "unknown")
    url = f"{WIKI_URL}/index.php/{params.title.replace(' ', '_')}"

    if status == "Success":
        return f"✅ Content appended to [{params.title}]({url})\nRevision: {edit_result.get('newrevid', '?')}"
    else:
        return f"❌ Append failed: {json.dumps(edit_result)}"


@mcp.tool(
    name="wiki_delete_page",
    annotations={"readOnlyHint": False, "destructiveHint": True}
)
async def wiki_delete_page(params: DeletePageInput) -> str:
    """
    Delete a wiki page. Requires admin/sysop rights on the wiki. Use carefully.
    """
    csrf = await get_csrf_token()
    result = await api_post({
        "action": "delete",
        "title": params.title,
        "reason": params.reason,
        "token": csrf,
    })
    if "delete" in result:
        return f"✅ Deleted: '{params.title}'"
    return f"❌ Delete failed: {json.dumps(result)}"


@mcp.tool(
    name="wiki_move_page",
    annotations={"readOnlyHint": False, "destructiveHint": False}
)
async def wiki_move_page(params: MovePageInput) -> str:
    """
    Rename / move a wiki page to a new title.
    """
    csrf = await get_csrf_token()
    move_params: dict[str, Any] = {
        "action": "move",
        "from": params.from_title,
        "to": params.to_title,
        "reason": params.reason,
        "token": csrf,
    }
    if not params.leave_redirect:
        move_params["noredirect"] = "1"

    result = await api_post(move_params)
    if "move" in result:
        new_url = f"{WIKI_URL}/index.php/{params.to_title.replace(' ', '_')}"
        return f"✅ Moved '{params.from_title}' → '[{params.to_title}]({new_url})'"
    return f"❌ Move failed: {json.dumps(result)}"


@mcp.tool(
    name="wiki_get_site_info",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_get_site_info() -> str:
    """
    Get overall wiki statistics and configuration info: page count, user count, etc.
    """
    data = await api_get({
        "action": "query",
        "meta": "siteinfo",
        "siprop": "general|statistics|namespaces",
    })
    info = data["query"]
    general = info.get("general", {})
    stats = info.get("statistics", {})

    lines = [
        f"## Wiki Info: {general.get('sitename', 'Unknown')}",
        f"**URL:** {general.get('base', WIKI_URL)}",
        f"**MediaWiki version:** {general.get('generator', '?')}",
        f"",
        f"### Statistics",
        f"- Pages: {stats.get('pages', '?'):,}",
        f"- Articles: {stats.get('articles', '?'):,}",
        f"- Edits: {stats.get('edits', '?'):,}",
        f"- Images: {stats.get('images', '?'):,}",
        f"- Users: {stats.get('users', '?'):,}",
        f"- Active users: {stats.get('activeusers', '?'):,}",
    ]
    return "\n".join(lines)


@mcp.tool(
    name="wiki_get_login_status",
    annotations={"readOnlyHint": True, "destructiveHint": False}
)
async def wiki_get_login_status() -> str:
    """
    Check current login status and bot credentials configuration.
    """
    info = await api_get({"action": "query", "meta": "userinfo", "uiprop": "groups|rights"})
    user = info["query"]["userinfo"]

    if "anon" in user:
        creds_set = bool(BOT_USER and BOT_PASS)
        return (
            f"⚠️ Not logged in (anonymous).\n"
            f"Bot credentials configured: {'Yes' if creds_set else 'No — set WIKI_BOT_USER and WIKI_BOT_PASS env vars'}\n"
            f"Write operations will fail until you log in."
        )

    groups = user.get("groups", [])
    return (
        f"✅ Logged in as: **{user['name']}**\n"
        f"Groups: {', '.join(groups)}\n"
        f"User ID: {user.get('id', '?')}"
    )


if __name__ == "__main__":
    mcp.run()
