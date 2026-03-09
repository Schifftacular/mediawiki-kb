# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **mediawiki-kb**, a Claude Code plugin that scaffolds, organizes, and maintains a structured MediaWiki knowledge base for businesses, ventures, and projects. It connects Claude to a MediaWiki instance via an MCP server and provides commands, skills, agents, and hooks for wiki management.

## Architecture

```
plugin/
├── .claude-plugin/plugin.json   # Plugin manifest (name, version, keywords)
├── .mcp.json                    # MCP server configuration (mediawiki server)
├── server/
│   └── server.py                # Python MCP server using FastMCP + httpx
├── commands/
│   ├── new-project.md           # /new-project — scaffolds ~52 wiki pages across 8 domains
│   └── audit.md                 # /audit — health check for wiki content (stubs, staleness, orphans, broken links)
├── skills/
│   └── wiki-management/
│       ├── SKILL.md             # Core wiki management skill (page hierarchy, behavioral rules, editing guidelines)
│       └── references/          # Per-domain template definitions (brand, marketing, product, dev, ops, legal, finance, summary)
├── agents/
│   └── wiki-organizer.md        # Agent for bulk restructuring, category reorganization, template compliance
└── hooks/
    └── hooks.json               # UserPromptSubmit hook — auto-loads wiki context from CLAUDE.md `wiki-context:` lines
```

### MCP Server (`server/server.py`)

Python server using `mcp.server.fastmcp.FastMCP` with `httpx` for async HTTP. Authenticates to MediaWiki via BotPasswords. Provides these tools:

- **Read-only:** `wiki_get_page`, `wiki_search`, `wiki_list_pages`, `wiki_list_category`, `wiki_get_categories`, `wiki_get_links`, `wiki_recent_changes`, `wiki_get_site_info`, `wiki_get_login_status`
- **Write:** `wiki_create_or_edit_page`, `wiki_append_to_page`, `wiki_move_page`, `wiki_delete_page`

All tools use Pydantic input models with validation. Session cookies are managed globally for login persistence.

### Wiki Page Structure

Every project follows an 8-domain hub structure under `Projects/{Name}`:
1. Summary, 2. Brand & Identity, 3. Marketing, 4. Product, 5. Development, 6. Operations, 7. Legal, 8. Finance

Each domain has sub-pages with stub templates containing "Claude Instructions" (prerequisites, deliverables, prompting frameworks, downstream effects, tool recommendations). Populated pages get a `/Reference` companion sub-page.

## Development

### Server dependencies

```bash
# Python venv is at .venv/ in project root
source .venv/bin/activate
pip install -r plugin/server/requirements.txt   # mcp>=1.0.0, httpx>=0.27.0, pydantic>=2.0.0
```

### Running the MCP server locally

```bash
python plugin/server/server.py
```

Requires env vars: `WIKI_URL`, `WIKI_BOT_USER`, `WIKI_BOT_PASS` (configured in `.mcp.json`).

## Key Conventions

- **Wikitext format:** `= H1 =`, `== H2 ==`, `'''bold'''`, `''italic''`, `[[Internal Link]]`, `[[Category:Name]]` at page bottom
- **Page paths:** Always use full paths from `Projects/` (e.g., `Projects/Trotle/Brand & Identity/Brand Vision`)
- **Categories required:** Every page needs `[[Category:Projects]]`, `[[Category:Projects/{Name}]]`, and domain/industry categories
- **Stub detection:** A page is a stub if it contains `''This page is a stub.''` or has only Claude Instructions with no real content
- **Downstream ripple check:** After editing any populated page, scan other project pages for references to changed content and propose updates
- **wiki-context hook:** Projects can add `wiki-context: Projects/{Name}/Summary, ...` to their CLAUDE.md to auto-load wiki pages on each prompt
- **Edit summaries:** Always descriptive (e.g., "Updated brand vision to reflect audience pivot"), never generic
- **Claude Instructions sections** on wiki pages are permanent — never remove them even after content is generated
