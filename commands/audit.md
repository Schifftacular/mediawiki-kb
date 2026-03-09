---
name: audit
description: Audit a MediaWiki knowledge base for health issues — stubs, staleness, orphans, broken links, and more
argument-hint: optional project name
allowed-tools:
  - Read
  - Bash
  - mcp__mediawiki__wiki_list_pages
  - mcp__mediawiki__wiki_get_page
  - mcp__mediawiki__wiki_get_categories
  - mcp__mediawiki__wiki_get_links
  - mcp__mediawiki__wiki_recent_changes
  - mcp__mediawiki__wiki_search
  - mcp__mediawiki__wiki_list_category
  - mcp__mediawiki__wiki_create_or_edit_page
---

You are auditing a MediaWiki knowledge base for structural and content health issues.

## Determine scope

If the user provided a project name as an argument, scope the audit to `Projects/{ProjectName}` and its sub-pages. If no argument was provided, audit the entire wiki.

## Standard project structure

A well-formed project lives at `Projects/{Name}` and has 8 hub domains:

1. Summary
2. Brand & Identity
3. Marketing
4. Product
5. Development
6. Operations
7. Legal
8. Finance

Each hub page may have sub-pages beneath it. Populated pages with substantive content should also have a companion `/Reference` sub-page.

## Step 1: Gather data

Collect all the raw data you need before analyzing. Run these calls in parallel where possible to minimize round-trips:

1. **Page inventory** — Call `wiki_list_pages` to get the full page list. If scoped to a project, filter to pages under `Projects/{ProjectName}`.
2. **Recent changes** — Call `wiki_recent_changes` to get the latest edit timestamps.
3. **Page content and metadata** — For every page in scope, call `wiki_get_page` to retrieve its content, `wiki_get_categories` to retrieve its categories, and `wiki_get_links` to retrieve its outbound internal links. Batch these calls in parallel groups to stay efficient.

Build the following data structures in memory:

- `allPages`: set of all page titles in scope
- `pageContent`: map of title to wikitext content
- `pageCategories`: map of title to list of categories
- `outboundLinks`: map of title to list of linked page titles
- `inboundLinks`: map of title to list of pages that link TO it (derived by inverting outboundLinks)
- `lastEdited`: map of title to last-edit timestamp (from recent changes and page metadata)

## Step 2: Run audit checks

### 2a. Completeness

A page is a **stub** if its content is empty, contains only whitespace, or contains only template instructions / Claude Instructions placeholders with no substantive prose. For each hub domain, calculate:

- Total sub-pages expected vs. existing
- Number of stubs vs. populated pages
- Percentage complete

### 2b. Staleness

A page is **stale** if it has not been edited in 60 or more days AND at least one page that links to it (or that it links to) has been edited more recently. Flag these with the number of days since last edit.

### 2c. Orphans

A page is an **orphan** if no other page in the wiki links to it. Exclude top-level hub pages from this check (they are entry points). Also exclude the main project page itself.

### 2d. Missing companions

For every populated (non-stub) page, check whether a `/Reference` sub-page exists. If not, flag it as missing its reference companion.

### 2e. Broken links

For every outbound internal link in every page, check whether the target page exists in `allPages`. Collect all broken links grouped by source page.

### 2f. Category health

Every page should belong to at least one category. Pages under a project should belong to a category matching their hub domain (e.g., pages under Development should be in a "Development" category or similar). Flag pages with no categories and pages missing their expected domain category.

## Step 3: Present the report

Output a structured report with these sections, in this order. Use markdown formatting.

### Wiki Health Audit Report
#### Scope: {project name or "Entire Wiki"}

**Summary metrics:**
- Total pages audited: N
- Populated: N (X%)
- Stubs: N (X%)
- Stale: N
- Orphans: N
- Broken links: N
- Missing /Reference pages: N

Then present each category of findings as a prioritized checklist. Order items by severity: broken links first, then orphans, then stubs in core domains, then missing companions, then staleness, then category issues.

Use this format for each finding:

```
- [ ] **[Category]** Page title — description of issue
```

For example:
```
- [ ] **Broken link** Projects/Acme/Development/API — links to "Projects/Acme/Development/Auth" which does not exist
- [ ] **Orphan** Projects/Acme/Legal/Privacy Policy — no inbound links from any other page
- [ ] **Stub** Projects/Acme/Finance/Budget — page has no real content
- [ ] **Missing /Reference** Projects/Acme/Product/Roadmap — populated page has no /Reference sub-page
- [ ] **Stale** Projects/Acme/Marketing/Launch Plan — last edited 94 days ago
- [ ] **Category** Projects/Acme/Operations/Hosting — missing expected "Operations" category
```

If the audit is scoped to a project, also show a per-domain breakdown table:

| Domain | Pages | Populated | Stubs | Complete % |
|--------|-------|-----------|-------|------------|

## Step 4: Offer to fix

After presenting the report, ask:

> Want me to fix any of these? I can address them one at a time — just say which items or categories to tackle.

Do NOT make any edits until the user explicitly approves specific items. When the user approves fixes:

- **Stubs**: Ask the user what content to add, or offer to draft based on context from sibling pages.
- **Orphans**: Offer to add a link from the relevant hub page.
- **Missing /Reference**: Offer to create the Reference sub-page with a standard template.
- **Broken links**: Offer to either create the missing target page or remove/update the link.
- **Category issues**: Add the missing categories to the page.
- **Staleness**: Flag for the user's review — do not auto-edit stale pages without explicit direction on what to update.

Apply each fix individually, confirm it was applied, then move to the next approved item.
