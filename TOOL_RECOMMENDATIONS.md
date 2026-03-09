# MediaWiki Knowledge Base Plugin — Tool Recommendations by Domain

Reference document for building wiki content across 8 business domains using Claude Code skills, MCP servers, open source tools, and guided prompting frameworks.

---

## 1. Summary — Business Overview, Mission, Vision

### Claude Code Skills & Plugins
1. **business-model-canvas** — Structured canvas generation for business model articulation
2. **executive-summary-writer** — Guided executive summary and elevator pitch drafting
3. **brainstorm** (from obra/superpowers) — Divergent ideation for mission/vision exploration
4. **write-plan** (from obra/superpowers) — Structured planning and goal articulation
5. **claude-scientific-skills/analysis** — Analytical frameworks for market sizing and opportunity assessment
6. **strategic-planning** — SWOT, PESTEL, and Porter's Five Forces generation
7. **document-processing** — Export summaries to Word/PDF for stakeholder review
8. **pitch-deck-generator** — Investor-ready narrative structuring

### MCP Servers
- **Notion** (`mcp__claude_ai_Notion`) — Store and organize business plans, OKRs, and strategy docs in a collaborative workspace
- **Canva** (`mcp__claude_ai_Canva`) — Generate pitch deck presentations directly from strategy outlines
- **Supabase** (`mcp__claude_ai_Supabase`) — Store structured business data (KPIs, milestones, metrics) in a queryable database

### Online Resources & Open Source Tools
1. [Business Model Fiddle](https://bmfiddle.com) — Free browser-based Business Model Canvas tool, no account required for local use
2. [Canvanizer](https://canvanizer.com/) — Collaborative online canvas tool supporting BMC, Lean Canvas, SWOT, and more
3. [Leantime](https://leantime.io) — Open source project management with built-in Lean Canvas, SWOT analysis, and Goal/Idea management
4. [Strategyzer (free resources)](https://www.strategyzer.com/library) — Business Model Canvas and Value Proposition Canvas templates and guides
5. [Open Source Ecology Business Model Canvas](https://wiki.opensourceecology.org/wiki/Business_Model_Canvas) — Community-maintained open business planning framework

### Prompting Framework
> **Framework: "Vision Pyramid"**
> Start broad with industry context and narrow to specifics. Use Socratic questioning:
> 1. "What problem does this business solve, and for whom?"
> 2. "What would the world look like if this business fully succeeded?"
> 3. "What is the single sentence a customer would use to describe you?"
> Guide through Mission (what we do) -> Vision (where we're going) -> Values (how we operate). Use the Business Model Canvas as a structured backbone, filling each of the 9 blocks conversationally.

---

## 2. Brand & Identity — Voice, Color System, Typography, Logo, Guidelines

### Claude Code Skills & Plugins
1. **brand-strategist** — Brand positioning, archetype identification, and voice definition
2. **design-system-creator** — Color palette, typography scale, and component token generation
3. **style-guide-generator** — Comprehensive brand guidelines document creation
4. **color-theory-advisor** — Color psychology and accessible palette generation (WCAG compliance)
5. **typography-specialist** — Font pairing recommendations and type hierarchy systems
6. **brand-voice-writer** — Tone-of-voice documentation with do/don't examples
7. **d3-visualization** — Generate brand color swatches and visual system diagrams
8. **mermaid-diagram** — Visual brand architecture and identity system diagrams

### MCP Servers
- **Canva** (`mcp__claude_ai_Canva`) — Access brand kits, generate branded designs, manage visual assets; use `list-brand-kits` to pull existing brand elements
- **Notion** (`mcp__claude_ai_Notion`) — Central brand bible storage with linked databases for assets, voice examples, and guidelines
- **Miro** (`mcp__claude_ai_Miro`) — Collaborative brand workshops, mood boards, and identity mapping on visual whiteboards

### Online Resources & Open Source Tools
1. [Coolors.co](https://coolors.co) — Free color palette generator with accessibility contrast checker
2. [Google Fonts](https://fonts.google.com) — Open source font library with curated pairing suggestions
3. [Realtime Colors](https://www.realtimecolors.com) — Visualize color palettes on a real website layout instantly
4. [Open Source Design](https://opensourcedesign.net) — Community of designers contributing to open source; resources for brand/identity work
5. [Style Dictionary](https://github.com/amzn/style-dictionary) — Amazon's open source tool for managing design tokens across platforms

### Prompting Framework
> **Framework: "Brand Archetype Workshop"**
> Use the 12 Jungian Brand Archetypes as a conversation scaffold:
> 1. Present the 12 archetypes with examples (Innocent=Dove, Hero=Nike, Outlaw=Harley-Davidson)
> 2. Ask: "Which 2-3 archetypes resonate with your brand's personality?"
> 3. Derive voice attributes from archetype (e.g., Hero -> bold, confident, action-oriented)
> 4. Build color system from psychological associations of chosen archetype
> 5. Generate a "Brand Personality Spectrum" with sliders (Formal<->Casual, Playful<->Serious, etc.)
> End with a one-page Brand Identity Brief that feeds into all downstream content.

---

## 3. Marketing — Audience, Content Strategy, Channels, Competitive Analysis

### Claude Code Skills & Plugins
1. **content-strategist** — Editorial calendar, content pillar development, and channel planning
2. **seo-keyword-researcher** — Keyword analysis and search intent mapping
3. **competitor-analysis** — Structured competitive landscape documentation
4. **audience-persona-builder** — Detailed customer persona creation with demographics, psychographics, and jobs-to-be-done
5. **messaging-framework** — Value propositions, taglines, and positioning statements
6. **social-media-strategist** — Platform-specific content strategy and posting frameworks
7. **copywriting-assistant** — Marketing copy generation aligned with brand voice
8. **growth-experiment-designer** — Hypothesis-driven growth experiment planning (ICE/RICE scoring)

### MCP Servers
- **Notion** (`mcp__claude_ai_Notion`) — Marketing content databases, editorial calendars, campaign trackers
- **Slack** (`mcp__claude_ai_Slack`) — Monitor team marketing discussions, share campaign updates, turn conversations into action items
- **Stripe** (`mcp__claude_ai_Stripe`) — Pull real customer and product data to inform marketing segmentation and pricing positioning

### Online Resources & Open Source Tools
1. [Wappalyzer](https://www.wappalyzer.com) — Free browser extension to analyze competitor tech stacks
2. [SpyFu (free tier)](https://www.spyfu.com) — Competitor keyword and ad research
3. [Wayback Machine](https://web.archive.org) — Track competitor website/branding evolution over time
4. [PostHog](https://posthog.com) — Open source product analytics, session recording, feature flags, and A/B testing (self-hostable)
5. [Matomo](https://matomo.org) — Open source Google Analytics alternative with full data ownership

### Prompting Framework
> **Framework: "Outside-In Market Discovery"**
> Start with the competitive landscape before defining your own positioning:
> 1. "Who are the 3-5 closest competitors? What do they promise? Where do they fall short?"
> 2. Map the competitive landscape on a 2x2 positioning matrix (choose relevant axes)
> 3. Identify the "white space" — unoccupied positions in the market
> 4. Build customer personas using Jobs-to-Be-Done: "When [situation], I want to [motivation], so I can [outcome]"
> 5. Draft positioning statement: "For [target], [brand] is the [category] that [key benefit] because [reason to believe]"
> Use concrete examples and competitor screenshots/quotes as stimulus material.

---

## 4. Product — Vision, Features, User Journeys, UX, Wireframes, Roadmap

### Claude Code Skills & Plugins
1. **product-requirements-doc** — PRD generation with user stories, acceptance criteria, and scope
2. **user-journey-mapper** — End-to-end user flow documentation with touchpoints and pain points
3. **ux-research-guide** — Interview scripts, usability test plans, and synthesis frameworks
4. **wireframe-describer** — Detailed wireframe specifications in structured text (for handoff to design tools)
5. **api-design-principles** — RESTful API design best practices and endpoint documentation
6. **roadmap-planner** — Quarterly/annual product roadmap with prioritization frameworks (RICE, MoSCoW)
7. **accessibility-auditor** — WCAG compliance checking and inclusive design recommendations
8. **mermaid-diagram** — User flow diagrams, system architecture, and journey maps in Mermaid syntax

### MCP Servers
- **Notion** (`mcp__claude_ai_Notion`) — Product backlogs, sprint boards, feature specs, and roadmap databases
- **Miro** (`mcp__claude_ai_Miro`) — Collaborative user journey maps, wireframe workshops, and design sprints on visual boards
- **Asana** (`mcp__plugin_asana_asana`) — Product roadmap tracking, sprint management, task dependencies, and team workload visibility

### Online Resources & Open Source Tools
1. [Diagrams.net (Draw.io)](https://diagrams.net) — Open source diagramming for wireframes, flowcharts, UML, and system architecture; integrates with GitHub, Google Drive
2. [Quant-UX](https://quant-ux.com) — Open source prototyping and usability testing platform with real-time collaboration
3. [Penpot](https://penpot.app) — Open source design and prototyping platform (Figma alternative); SVG-native, self-hostable
4. [Plane](https://plane.so) — Open source project management with issues, cycles, modules, and AI integration
5. [Wireframe.cc](https://wireframe.cc) — Minimal free wireframing tool for quick low-fidelity mockups

### Prompting Framework
> **Framework: "Story-First Product Definition"**
> Build product specs from user narratives, not feature lists:
> 1. Start with a "Day in the Life" scenario: "Walk me through a typical day for your target user. Where does frustration occur?"
> 2. Map the current journey (before your product) vs. desired journey (with your product)
> 3. For each pain point, ask: "What is the minimum feature that removes this friction?"
> 4. Prioritize using RICE: Reach x Impact x Confidence / Effort
> 5. Structure the roadmap in Now/Next/Later buckets rather than fixed timelines
> Generate wireframes as structured text descriptions that can be handed to Penpot/Figma.

---

## 5. Development — Architecture, Tech Stack, Database, API, Deployment

### Claude Code Skills & Plugins
1. **backend-dev-guidelines** — Server architecture patterns, API design, and code organization standards
2. **frontend-dev-guidelines** — Component architecture, state management, and rendering patterns
3. **database-schema-designer** — ERD generation, migration planning, and query optimization guidance
4. **api-design-principles** — OpenAPI/Swagger spec generation, REST best practices, versioning strategy
5. **devops-pipeline** — CI/CD pipeline configuration, Docker/Kubernetes setup, deployment automation
6. **security-audit** (OWASP skills) — OWASP Top 10:2025, ASVS 5.0 compliance, and vulnerability scanning guidance
7. **testing-strategy** (TDD skills from obra/superpowers) — Test pyramid design, TDD workflows, and coverage targets
8. **architecture-decision-records** — ADR template generation and tech decision documentation
9. **git-workflow** — Branching strategy, commit conventions, and PR review guidelines
10. **performance-optimization** — Profiling, caching strategies, and load testing guidance

### MCP Servers
- **Supabase** (`mcp__claude_ai_Supabase`) — Postgres database management, migrations, edge functions, and real-time APIs; execute SQL directly
- **GitHub** (via MCP) — Repository management, issue tracking, PR workflows, and code search
- **Cloudflare** (`mcp__claude_ai_Cloudflare_Developer_Platform`) — Workers deployment, D1 databases, KV storage, R2 buckets, and edge computing

### Online Resources & Open Source Tools
1. [Context7](https://context7.com) — Up-to-date documentation for any library, queryable via MCP (available as `mcp__claude_ai_Context7`)
2. [Supabase](https://supabase.com) — Open source Firebase alternative: Postgres, Auth, Storage, Edge Functions, Realtime
3. [n8n](https://n8n.io) — Open source workflow automation; connect APIs, databases, and services with visual flows
4. [Diagrams.net](https://diagrams.net) — Architecture diagrams, ERDs, network topology, and deployment diagrams
5. [OpenAPI Generator](https://openapi-generator.tech) — Generate API client SDKs, server stubs, and documentation from OpenAPI specs

### Prompting Framework
> **Framework: "Architecture Decision Records (ADR)"**
> Document every significant technical decision using the ADR format:
> 1. **Context**: "What is the technical challenge or decision point?"
> 2. **Options Considered**: List 2-4 alternatives with pros/cons
> 3. **Decision**: State the chosen approach and rationale
> 4. **Consequences**: What trade-offs are accepted?
> For initial architecture, use C4 Model progression: Context -> Container -> Component -> Code diagrams. Start with "What are the 3-5 major system boundaries?" and drill down.

---

## 6. Operations — Team/Roles, SOPs, Workflows, Vendor/Tools, KPIs

### Claude Code Skills & Plugins
1. **sop-writer** — Standard Operating Procedure documentation with step-by-step instructions
2. **process-mapper** — Workflow visualization and process optimization
3. **okr-framework** — OKR/KPI definition, cascading objectives, and progress tracking
4. **team-structure-designer** — Org chart generation, RACI matrices, and role definition documents
5. **vendor-evaluation** — Vendor comparison matrices and selection criteria frameworks
6. **meeting-facilitator** — Agenda templates, decision logs, and action item tracking
7. **onboarding-guide** — New hire onboarding checklists and knowledge transfer documents
8. **mermaid-diagram** — Process flowcharts, sequence diagrams, and organizational charts

### MCP Servers
- **Asana** (`mcp__plugin_asana_asana`) — Task management, project tracking, team workloads, goals, and portfolio oversight
- **Notion** (`mcp__claude_ai_Notion`) — SOPs, team wikis, process databases, vendor directories, and KPI dashboards
- **Slack** (`mcp__claude_ai_Slack`) — Team communication monitoring, workflow triggers, and operational updates

### Online Resources & Open Source Tools
1. [Plane](https://plane.so) — Open source project management with cycles, modules, and team dashboards
2. [n8n](https://n8n.io) — Open source workflow automation for connecting operational tools and automating repetitive processes
3. [Activepieces](https://www.activepieces.com) — Open source business automation alternative to Zapier; 200+ integrations
4. [Camunda](https://camunda.com) — Open source process orchestration with BPMN visual modeling for complex workflows
5. [Budibase](https://budibase.com) — Open source low-code platform for building internal ops tools, dashboards, and forms

### Prompting Framework
> **Framework: "Process Archaeology"**
> Document operations by excavating existing (often undocumented) practices:
> 1. "Walk me through what happens when [trigger event]. Who does what, in what order?"
> 2. For each step: "What tool do you use? What could go wrong? How long does it take?"
> 3. Identify bottlenecks: "Where do things get stuck or require waiting?"
> 4. Build the SOP in three layers: Overview (flowchart) -> Detailed Steps (numbered) -> Troubleshooting (decision tree)
> 5. Define KPIs for each process: "How would you know if this process is working well?"
> Use RACI (Responsible, Accountable, Consulted, Informed) for every process to clarify ownership.

---

## 7. Legal — Entity, ToS, Privacy Policy, Contracts, IP/DMCA, Compliance

### Claude Code Skills & Plugins
1. **legal-document-drafter** — Terms of Service, Privacy Policy, and contract template generation
2. **privacy-policy-generator** — GDPR/CCPA/CPRA-compliant privacy policy creation
3. **compliance-checklist** — Regulatory compliance tracking for relevant jurisdictions
4. **contract-reviewer** — Clause analysis, risk identification, and plain-language summaries
5. **ip-strategy-advisor** — Intellectual property protection planning, trademark/copyright guidance
6. **risk-register** — Risk identification, assessment matrix, and mitigation planning
7. **data-processing-agreement** — DPA generation for vendor and processor relationships
8. **corporate-structure-advisor** — Entity formation comparison (LLC, C-Corp, S-Corp) with pros/cons

### MCP Servers
- **Notion** (`mcp__claude_ai_Notion`) — Legal document repository, contract tracking databases, compliance checklists, and deadline calendars
- **Supabase** (`mcp__claude_ai_Supabase`) — Structured storage for risk registers, compliance audit logs, and contract metadata
- **Gmail** (`mcp__claude_ai_Gmail`) — Search and reference legal correspondence, send document drafts for attorney review

### Online Resources & Open Source Tools
1. [TermsFeed](https://www.termsfeed.com) — Free Privacy Policy and Terms & Conditions generators; covers GDPR, CCPA
2. [Termly](https://termly.io) — Free privacy policy generator with AI-ready disclosures and cookie consent management
3. [GetTerms](https://getterms.io) — Lawyer-written legal document generator in plain, human-readable language
4. [Clerky](https://www.clerky.com) — Startup-focused legal document automation (incorporation, equity, contracts)
5. [CommonAccord](http://www.commonaccord.org) — Open source legal document assembly using modular, composable prose objects on GitHub

### Prompting Framework
> **Framework: "Legal Layered Defense"**
> Build legal documentation from foundation up, flagging attorney review points:
> 1. **Entity Layer**: "What type of business entity? Where is it registered? Who are the principals?"
> 2. **Customer Layer**: "What data do you collect? How do you process payments? What jurisdictions do your users reside in?" -> Generate ToS + Privacy Policy
> 3. **Vendor Layer**: "Who are your contractors/vendors? What data do they access?" -> Generate contractor agreements + DPAs
> 4. **Protection Layer**: "What IP do you own? What content do users submit?" -> DMCA policy + IP strategy
> 5. **Risk Layer**: Build a risk register with Likelihood x Impact scoring
> **IMPORTANT**: Always include a disclaimer that generated legal content requires attorney review. Flag specific clauses that are jurisdiction-dependent.

---

## 8. Finance — Revenue Model, Pricing, Projections, Funding, Expenses

### Claude Code Skills & Plugins
1. **financial-model-builder** — Three-statement financial model generation (P&L, Balance Sheet, Cash Flow)
2. **pricing-strategist** — Pricing model analysis (freemium, tiered, usage-based, per-seat) with competitive benchmarking
3. **unit-economics-calculator** — CAC, LTV, churn rate, and payback period computation
4. **fundraising-advisor** — Pitch deck financial slides, valuation frameworks, and term sheet guidance
5. **expense-tracker-designer** — Budget template and expense categorization system design
6. **revenue-forecasting** — Cohort analysis, growth modeling, and scenario planning (bull/base/bear)
7. **burn-rate-analyzer** — Runway calculation, cash flow forecasting, and break-even analysis
8. **d3-visualization** — Financial charts, revenue waterfall diagrams, and projection visualizations

### MCP Servers
- **Stripe** (`mcp__claude_ai_Stripe`) — Real revenue data, subscription metrics, product/price management, invoice creation, and refund tracking
- **Supabase** (`mcp__claude_ai_Supabase`) — Financial data storage, custom reporting queries, and structured expense/revenue tables
- **Notion** (`mcp__claude_ai_Notion`) — Financial planning documents, investor update templates, and budget tracking databases

### Online Resources & Open Source Tools
1. [Graphite Financial Open Source Model](https://graphitefinancial.com/open-source-financial-model/) — Free startup financial model template (Excel + Google Sheets) with revenue, expenses, and projections
2. [OpenVC Startup Financial Model Templates](https://www.openvc.app/blog/startup-financial-model) — 12 curated free and paid financial model templates for startups
3. [Damodaran Online (NYU Stern)](http://pages.stern.nyu.edu/~adamodar/) — Free downloadable DCF valuation models, datasets, and financial analysis tools from Professor Aswath Damodaran
4. [Sturppy](https://www.sturppy.com) — Financial modeling tool designed for early-stage startups; build investor-ready models without Excel expertise
5. [Delfos](https://delfos.co) — Automated financial forecasting for startups; anticipates cash shortages and funding requirements

### Prompting Framework
> **Framework: "Bottom-Up Financial Narrative"**
> Build financial models from unit economics up, not top-down market sizing:
> 1. "What is your revenue model? How does a single dollar enter your business?"
> 2. "What does it cost to acquire one customer? What is their expected lifetime value?"
> 3. Build a monthly cohort model: New customers x ARPU x Retention curve = Revenue
> 4. Layer in costs: Fixed (rent, salaries, tools) + Variable (COGS, support, hosting per user)
> 5. Model three scenarios: Conservative (50% of target), Base (target), Optimistic (150% of target)
> 6. Calculate runway: "At current burn rate, when do you need to raise or become profitable?"
> Use real Stripe data via MCP when available to ground projections in actual metrics rather than assumptions.

---

## Cross-Domain Resources

### Essential MCP Servers (Available in Your Environment)
| Server | Primary Domains | Key Capabilities |
|--------|----------------|-------------------|
| **Notion** | All 8 domains | Wiki-like docs, databases, templates, team collaboration |
| **Supabase** | Development, Finance, Operations | Postgres DB, SQL execution, migrations, edge functions |
| **Stripe** | Finance, Marketing, Product | Payment data, subscriptions, pricing, invoices |
| **Canva** | Brand, Summary, Marketing | Design generation, brand kits, presentations |
| **Asana** | Operations, Product | Task/project management, goals, portfolios |
| **Slack** | Operations, Marketing | Team communication, channel monitoring, message automation |
| **Cloudflare** | Development | Edge deployment, D1 databases, KV storage, Workers |
| **GitHub** (via MCP) | Development | Code repos, issues, PRs, CI/CD |
| **Context7** | Development | Live documentation lookup for any library/framework |
| **Miro** | Product, Brand, Operations | Visual collaboration, diagrams, whiteboards |
| **Gmail** | Legal, Operations | Email search, draft creation, correspondence tracking |

### Essential Claude Code Skill Collections
| Collection | Source | Skills Count | Best For |
|-----------|--------|-------------|----------|
| **obra/superpowers** | GitHub | 20+ | Brainstorming, planning, execution, TDD |
| **claude-skills (full-stack)** | GitHub | 65 | React, NestJS, Python, DevOps |
| **OWASP Security Skills** | SkillsMP | 10+ | Security audits, ASVS compliance |
| **Claude Scientific Skills** | GitHub | 15+ | Research, analysis, finance, writing |
| **awesome-claude-code-toolkit** | GitHub | 135 agents, 35 skills, 42 commands | Comprehensive development toolkit |

### Skill Discovery & Installation
- **SkillsMP** ([skillsmp.com](https://skillsmp.com)) — 400,000+ searchable agent skills with category filtering and quality indicators
- **SkillHub** ([skillhub.club](https://www.skillhub.club/)) — Claude Skills marketplace with curated collections
- **awesome-claude-skills** ([GitHub](https://github.com/travisvn/awesome-claude-skills)) — Curated list with verified skills for TDD, debugging, git, docs
- **awesome-agent-skills** ([GitHub](https://github.com/VoltAgent/awesome-agent-skills)) — 500+ skills compatible with Claude Code, Codex, Gemini CLI, Cursor
- Install skills to `~/.claude/skills/` (personal) or `.claude/skills/` (project-level)

### MediaWiki-Specific Integration Notes
Your MediaWiki MCP server (`server.py`) provides the backbone for all 8 domains. Each domain maps to a wiki page hierarchy:
- `Business/Summary`, `Business/Mission`, `Business/Vision`
- `Brand/Identity`, `Brand/Voice`, `Brand/Colors`, `Brand/Typography`
- `Marketing/Audience`, `Marketing/Channels`, `Marketing/Competitors`
- `Product/Vision`, `Product/Features`, `Product/Roadmap`
- `Development/Architecture`, `Development/API`, `Development/Schema`
- `Operations/Team`, `Operations/SOPs`, `Operations/KPIs`
- `Legal/Terms`, `Legal/Privacy`, `Legal/Contracts`
- `Finance/Revenue`, `Finance/Pricing`, `Finance/Projections`

Use `wiki_create_or_edit_page` to write content and `[[Category:DomainName]]` to organize pages. Use `wiki_append_to_page` for iterative refinement sessions.

---

## Sources
- [SkillsMP — Agent Skills Marketplace](https://skillsmp.com)
- [awesome-claude-code (GitHub)](https://github.com/hesreallyhim/awesome-claude-code)
- [awesome-claude-skills (GitHub)](https://github.com/travisvn/awesome-claude-skills)
- [awesome-agent-skills (VoltAgent)](https://github.com/VoltAgent/awesome-agent-skills)
- [awesome-claude-code-toolkit (GitHub)](https://github.com/rohitg00/awesome-claude-code-toolkit)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Awesome MCP Servers Directory](https://mcp-awesome.com/)
- [MCP Official Registry](https://registry.modelcontextprotocol.io/)
- [MCP Servers Directory](https://mcp.so/)
- [Business Model Fiddle](https://bmfiddle.com)
- [Canvanizer](https://canvanizer.com/)
- [Diagrams.net](https://diagrams.net)
- [Penpot — Open Source Design](https://penpot.app)
- [Quant-UX](https://quant-ux.com)
- [PostHog — Open Source Analytics](https://posthog.com)
- [n8n — Workflow Automation](https://n8n.io)
- [Activepieces — Open Source Automation](https://www.activepieces.com)
- [Plane — Open Source Project Management](https://plane.so)
- [TermsFeed](https://www.termsfeed.com)
- [Termly](https://termly.io)
- [GetTerms](https://getterms.io)
- [Graphite Financial Open Source Model](https://graphitefinancial.com/open-source-financial-model/)
- [OpenVC Financial Model Templates](https://www.openvc.app/blog/startup-financial-model)
- [Damodaran Online (NYU Stern)](http://pages.stern.nyu.edu/~adamodar/)
- [Context7 Documentation](https://context7.com)
- [Style Dictionary (Amazon)](https://github.com/amzn/style-dictionary)
- [Supabase](https://supabase.com)
- [10 Free Wireframing Tools (IxDF)](https://ixdf.org/literature/article/10-free-to-use-wireframing-tools)
- [Open Source Workflow Software (Digital PM)](https://thedigitalprojectmanager.com/tools/best-open-source-workflow-software/)
- [Free Competitor Analysis Tools](https://thestartingidea.com/competitor-analysis-tools/)
