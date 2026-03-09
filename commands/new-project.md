---
name: new-project
description: Scaffold a new project/venture on the MediaWiki knowledge base with hub page and all stub sub-pages
argument-hint: (optional) project name
allowed-tools:
  - Read
  - Write
  - Bash
  - mcp__mediawiki__wiki_get_page
  - mcp__mediawiki__wiki_create_or_edit_page
  - mcp__mediawiki__wiki_search
  - mcp__mediawiki__wiki_list_pages
  - mcp__mediawiki__wiki_list_category
  - mcp__mediawiki__wiki_get_site_info
---

You are scaffolding a new project on the user's MediaWiki knowledge base. This wiki serves as a central, persistent reference library for all of the user's businesses, ventures, and ideas.

## Step 1: Gather Project Information

If the user provided a project name as an argument, use it. Otherwise, ask for it.

Then ask these questions ONE AT A TIME (do not batch them):

1. **What is {name}?** — Ask for a one-sentence description of what this venture/business is.
2. **What industry or domain is this in?** — Offer examples: tech, equestrian, legal, media, consulting, e-commerce, etc.
3. **What stage are you at?** — Offer: Idea, Research, Building, Launched
4. **Is this a business/venture or a personal tool?** — If personal tool, tell the user: "The wiki template system is designed for businesses and ventures. Personal tools don't need this level of structure. Want to create a simple wiki page instead?" If yes, create a basic page and stop. If they insist, proceed with the full template.

## Step 2: Confirm Before Creating

Present a summary:
```
Project: {name}
Description: {description}
Industry: {industry}
Stage: {stage}
Location: Projects/{name}
Pages to create: ~52 pages across 8 domains
```

Ask: "Ready to create? This will generate the hub page and all stub pages with Claude Instructions."

## Step 3: Create the Hub Page

Create the hub page at `Projects/{name}` with this wikitext structure:

```wikitext
= {name} =

{description}

'''Industry:''' {industry}<br/>
'''Stage:''' {stage}<br/>
'''Created:''' {current date}<br/>

== Summary ==
''Main article: [[Projects/{name}/Summary]]''

{one-sentence placeholder based on description}

== Brand & Identity ==
''Main article: [[Projects/{name}/Brand & Identity]]''

Defines how {name} looks, sounds, and presents itself to the world.

* [[Projects/{name}/Brand & Identity/Brand Vision]]
* [[Projects/{name}/Brand & Identity/Brand Voice]]
* [[Projects/{name}/Brand & Identity/Color System]]
* [[Projects/{name}/Brand & Identity/Typography]]
* [[Projects/{name}/Brand & Identity/Logo]]
* [[Projects/{name}/Brand & Identity/Imagery]]
* [[Projects/{name}/Brand & Identity/Brand Personality]]
* [[Projects/{name}/Brand & Identity/Brand Guidelines]]

== Marketing ==
''Main article: [[Projects/{name}/Marketing]]''

How {name} reaches and communicates with its audience.

* [[Projects/{name}/Marketing/Target Audience]]
* [[Projects/{name}/Marketing/Content Strategy]]
* [[Projects/{name}/Marketing/Channels]]
* [[Projects/{name}/Marketing/Positioning]]
* [[Projects/{name}/Marketing/Competitive Analysis]]
* [[Projects/{name}/Marketing/Messaging]]

== Product ==
''Main article: [[Projects/{name}/Product]]''

What {name} builds and delivers.

* [[Projects/{name}/Product/Product Vision]]
* [[Projects/{name}/Product/Features]]
* [[Projects/{name}/Product/User Journeys]]
* [[Projects/{name}/Product/UX Notes]]
* [[Projects/{name}/Product/Wireframes]]
* [[Projects/{name}/Product/Roadmap]]

== Development ==
''Main article: [[Projects/{name}/Development]]''

How {name} is built and deployed.

* [[Projects/{name}/Development/Architecture]]
* [[Projects/{name}/Development/Tech Stack]]
* [[Projects/{name}/Development/Database Schema]]
* [[Projects/{name}/Development/API Reference]]
* [[Projects/{name}/Development/Dev Setup]]
* [[Projects/{name}/Development/Deployment]]

== Operations ==
''Main article: [[Projects/{name}/Operations]]''

How {name} runs day-to-day.

* [[Projects/{name}/Operations/Team & Roles]]
* [[Projects/{name}/Operations/SOPs]]
* [[Projects/{name}/Operations/Workflows]]
* [[Projects/{name}/Operations/Vendors & Tools]]
* [[Projects/{name}/Operations/KPIs]]

== Legal ==
''Main article: [[Projects/{name}/Legal]]''

Legal foundation and compliance.

* [[Projects/{name}/Legal/Entity Formation]]
* [[Projects/{name}/Legal/Terms of Service]]
* [[Projects/{name}/Legal/Privacy Policy]]
* [[Projects/{name}/Legal/Contractor Agreements]]
* [[Projects/{name}/Legal/IP & DMCA]]
* [[Projects/{name}/Legal/Risk Register]]
* [[Projects/{name}/Legal/Compliance]]

== Finance ==
''Main article: [[Projects/{name}/Finance]]''

Revenue, costs, and financial planning.

* [[Projects/{name}/Finance/Revenue Model]]
* [[Projects/{name}/Finance/Pricing]]
* [[Projects/{name}/Finance/Projections]]
* [[Projects/{name}/Finance/Funding]]
* [[Projects/{name}/Finance/Expenses]]

[[Category:Projects]]
[[Category:{industry}]]
[[Category:Active]]
```

## Step 4: Create Domain Hub Pages

For each of the 8 domains (Brand & Identity, Marketing, Product, Development, Operations, Legal, Finance), create a domain hub page at `Projects/{name}/{Domain}` that lists its sub-pages with brief descriptions.

The Summary page is special — it does not have sub-pages. Create it as a stub with Claude Instructions (see Step 5 format).

## Step 5: Create All Stub Sub-Pages

For EVERY sub-page listed in the hub, create a stub page with this structure:

```wikitext
= {Page Title} =

''This page is a stub. Use the Claude Instructions below to generate content.''

== Content ==
<!-- Content goes here once generated -->

== Claude Instructions ==
=== Prerequisites ===
Generate or review these pages first:
* [[Projects/{name}/{prerequisite 1}]]
* [[Projects/{name}/{prerequisite 2}]]

=== What To Generate ===
{Bulleted list of specific deliverables for this page — e.g., mission statement, vision statement, core values}

=== Prompting Framework ===
{Specific conversational approach — e.g., "Start by discussing what problem this venture solves and for whom. Use the Brand Strategy Canvas: Purpose → Promise → Personality → Position. Work through each quadrant conversationally before drafting content."}

=== Session Type ===
{Recommendation: Claude Code, Claude Desktop, or Claude Cowork, with rationale}

=== Downstream Effects ===
After creating or editing this page, evaluate these pages for needed updates:
* [[Projects/{name}/{downstream page 1}]]
* [[Projects/{name}/{downstream page 2}]]

=== Recommended Tools ===
==== Plugins & Skills ====
{Numbered list of 10 recommended plugins/skills}

==== MCP Servers ====
{Numbered list of relevant MCP servers}

==== Resources ====
{Numbered list of open source tools, frameworks, documentation, or 3rd party solutions}

[[Category:{Domain}]]
[[Category:Projects/{name}]]
```

### Page-Specific Instructions

Use the wiki-management skill's template definitions to populate each stub with the correct:
- Prerequisites (which pages should exist before this one)
- What to generate (specific deliverables)
- Prompting framework (conversational approach)
- Session type recommendation
- Downstream effects (which pages to check after editing)
- Tool recommendations (plugins, skills, MCPs, resources)

If the wiki-management skill is not loaded, use your best judgment based on the domain. The key principle: each stub page must be a complete, self-contained instruction manual that tells Claude exactly how to help the user fill it out.

## Step 6: Report Results

After creating all pages, report:
```
Created {name} wiki structure:
- Hub page: Projects/{name} — [link]
- {count} sub-pages across 8 domains
- All pages include Claude Instructions for guided content creation

Next steps:
1. Add `wiki-context: Projects/{name}/Summary` to your project's CLAUDE.md
2. Start filling in pages — try: "Let's work on the Summary page for {name}"
3. Run /wiki:audit "{name}" anytime to check completeness
```
