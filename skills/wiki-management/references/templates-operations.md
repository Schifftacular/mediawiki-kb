# Operations Templates

## Domain Hub: Projects/{Name}/Operations

Navigation page linking to all operations sub-pages.

---

## Page: Team & Roles

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Product/Roadmap

### What To Generate
- Current team roster (name, role, responsibilities, availability)
- Role definitions (what each role owns and is accountable for)
- RACI matrix for key activities (Responsible, Accountable, Consulted, Informed)
- Skill gaps (what expertise is missing)
- Hiring plan (if applicable — roles needed, timeline, budget)
- Communication norms (how the team communicates, meeting cadence)
- Decision-making framework (who decides what)
- Contractor/vendor roster (external help and their roles)

### Prompting Framework
Start with: "Who's involved in {name} today, and what does each person do?" Map current reality first. Then ask: "What work is falling through the cracks or depends on one person?" Identify single points of failure. Use the RACI framework to clarify ownership. Only then ask about future hiring — keep it grounded in actual gaps, not aspirational org charts.

### Session Type
Claude Desktop — organizational planning, conversational.

### Downstream Effects
- SOPs (SOPs must be assigned to roles)
- Workflows (workflows must map to team capacity)
- KPIs (KPIs must have owners)
- Finance/Expenses (team costs)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — team structure ideation
2. brand-strategist — team-brand alignment
3. backend-architect — technical team structure
4. comprehensive-review-full-review — team plan review
5. api-design-principles — API team ownership
6. code-documentation-doc-generate — role documentation
7. e2e-testing-patterns — QA role planning
8. unix-macos-engineer — DevOps role planning
9. python-project-structure — backend role planning
10. find-skills — discover management skills

#### MCP Servers
1. Notion — team directory and org chart
2. Asana — role-based task assignment
3. Slack — team communication

#### Resources
1. RACI Matrix template — responsibility assignment
2. Basecamp's Shape Up — small team organization
3. Team Topologies (Skelton & Pais) — team structure patterns
4. The Manager's Path (Camille Fournier) — team leadership
5. Loom — async team communication

---

## Page: SOPs

### Prerequisites
- Projects/{Name}/Operations/Team & Roles
- Projects/{Name}/Operations/Workflows

### What To Generate
- SOP inventory (list of all standard operating procedures)
- SOP template (consistent format for all procedures)
- Priority SOPs (which procedures need documentation first)
- Per-SOP content: purpose, scope, steps, responsible role, tools needed, exceptions, revision history
- SOP review schedule (how often each SOP is reviewed)
- Emergency procedures (critical SOPs for incidents)

### Prompting Framework
Start with: "What tasks does your team do repeatedly that depend on one person knowing how?" Those are your first SOPs. For each: "Walk me through the last time you did this, step by step." Document the real process, not the ideal one. Then ask: "What goes wrong? What shortcuts exist?" Incorporate error handling. Write SOPs so someone with no context could follow them.

### Session Type
Claude Desktop or Code — depends on whether SOPs involve technical procedures or business processes.

### Downstream Effects
- Workflows (SOPs are components of workflows)
- Team & Roles (SOPs clarify role responsibilities)
- KPIs (SOP compliance is measurable)

### Recommended Tools
#### Plugins & Skills
1. code-documentation-doc-generate — procedure documentation
2. api-documentation-generator — technical SOPs
3. backend-dev-guidelines — development SOPs
4. e2e-testing-patterns — testing SOPs
5. unix-macos-engineer — ops/infra SOPs
6. brainstorming — SOP identification
7. comprehensive-review-full-review — SOP review
8. python-project-structure — code review SOPs
9. nextjs-best-practices — deploy SOPs
10. find-skills — discover documentation skills

#### MCP Servers
1. Notion — SOP documentation and tracking
2. Asana — SOP task checklists
3. Slack — SOP distribution

#### Resources
1. Process Street — SOP management platform
2. Notion SOP templates — free templates
3. Loom — video SOPs for visual processes
4. Scribe — automatic SOP generation from screen recordings
5. Tettra — internal knowledge base for SOPs

---

## Page: Workflows

### Prerequisites
- Projects/{Name}/Operations/Team & Roles
- Projects/{Name}/Product/Features (if product-related workflows)

### What To Generate
- Core workflow inventory (all repeating business processes)
- Workflow diagrams (flowcharts for each core workflow)
- Automation opportunities (which steps can be automated)
- Integration points (where workflows connect to tools/systems)
- Bottleneck analysis (where workflows slow down)
- Workflow metrics (cycle time, throughput, error rate)
- Improvement backlog (planned workflow optimizations)

### Prompting Framework
Map the three most critical workflows end-to-end. For each: "What triggers this workflow? What are the steps? Who's involved at each step? Where does it get stuck?" Draw the flow before optimizing it — understand the current state. Then identify: "Which steps are manual but could be automated? Which steps have the highest error rate?" Prioritize automation by impact.

### Session Type
Claude Code — workflow diagrams (Mermaid), automation scripts, integration code.

### Downstream Effects
- SOPs (workflows break down into SOPs)
- Vendors & Tools (workflows require specific tools)
- KPIs (workflow metrics feed KPIs)
- Development (automation requires development)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — workflow design
2. backend-architect — workflow architecture
3. api-design-principles — API workflow integration
4. backend-dev-guidelines — dev workflow standards
5. e2e-testing-patterns — workflow testing
6. unix-macos-engineer — automation scripting
7. python-project-structure — automation code
8. nextjs-best-practices — web workflow integration
9. comprehensive-review-full-review — workflow review
10. find-skills — discover automation skills

#### MCP Servers
1. Notion — workflow documentation
2. Asana — workflow task management
3. Supabase — workflow data storage

#### Resources
1. n8n — open-source workflow automation
2. Temporal.io — durable workflow execution
3. Mermaid.js — workflow diagrams as code
4. Zapier (free tier) — no-code workflow automation
5. Make (Integromat) — visual workflow builder

---

## Page: Vendors & Tools

### Prerequisites
- Projects/{Name}/Development/Tech Stack
- Projects/{Name}/Operations/Workflows

### What To Generate
- Vendor/tool inventory (all external services and tools)
- Per-vendor details: purpose, cost, contract terms, owner, alternatives
- Vendor risk assessment (single vendor dependencies, lock-in risk)
- Tool stack diagram (how tools connect)
- Evaluation criteria (how new tools are evaluated)
- Consolidation opportunities (overlapping tools)
- Budget summary (total monthly/annual tool spend)

### Prompting Framework
Start with: "List every tool and service {name} pays for or relies on — including free tiers." For each: "What does it do? Who uses it? What would happen if it disappeared tomorrow?" Identify critical dependencies and single points of failure. Ask: "Are any tools doing the same thing? Could any be consolidated?"

### Session Type
Claude Desktop — inventory and strategic evaluation.

### Downstream Effects
- Finance/Expenses (tool costs feed expenses)
- Workflows (workflows depend on tools)
- Dev Setup (dev tools must be documented)
- Deployment (infrastructure tools)

### Recommended Tools
#### Plugins & Skills
1. backend-architect — tooling architecture
2. brainstorming — tool evaluation
3. api-design-principles — API tool evaluation
4. backend-dev-guidelines — dev tool standards
5. unix-macos-engineer — ops tool evaluation
6. comprehensive-review-full-review — vendor review
7. python-project-structure — build tool evaluation
8. nextjs-best-practices — frontend tool evaluation
9. e2e-testing-patterns — test tool evaluation
10. find-skills — discover tool-specific skills

#### MCP Servers
1. Notion — vendor tracking database
2. Stripe — payment tool evaluation
3. Supabase — BaaS tool evaluation

#### Resources
1. StackShare — tool comparison platform
2. AlternativeTo — find alternatives to any tool
3. G2 — software reviews and comparisons
4. OpenAlternative — open-source alternative finder
5. ToolJet — open-source internal tool builder

---

## Page: KPIs

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Product/Roadmap
- Projects/{Name}/Operations/Workflows

### What To Generate
- KPI framework (North Star metric + supporting metrics)
- Per-KPI definition: name, formula, target, frequency, owner, data source
- KPI dashboard design (what the dashboard shows)
- Leading vs. lagging indicators
- Alert thresholds (when metrics need attention)
- Reporting cadence (daily, weekly, monthly reviews)
- KPI review process (how metrics inform decisions)

### Prompting Framework
Start with: "If you could only track ONE number to know if {name} is succeeding, what would it be?" That's your North Star metric. Then ask: "What 3-5 metrics would predict whether that number goes up or down?" Those are your leading indicators. For each KPI, apply the SMART framework: Specific, Measurable, Achievable, Relevant, Time-bound. Avoid vanity metrics — every KPI must drive a decision.

### Session Type
Claude Desktop — strategic, involves defining metrics and targets.

### Downstream Effects
- Finance/Projections (KPI targets feed financial projections)
- Team & Roles (KPIs must have owners)
- Workflows (workflows must produce KPI data)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — KPI selection
2. brand-strategist — brand KPIs
3. backend-architect — technical KPIs
4. api-design-principles — API performance KPIs
5. e2e-testing-patterns — quality KPIs
6. comprehensive-review-full-review — KPI review
7. postgres-best-practices — data query for KPIs
8. supabase-postgres-best-practices — analytics queries
9. web-design-guidelines — dashboard design
10. find-skills — discover analytics skills

#### MCP Servers
1. Supabase — KPI data queries
2. Notion — KPI tracking dashboard
3. Stripe — revenue KPIs

#### Resources
1. Lean Analytics (Alistair Croll) — startup metrics framework
2. Measure What Matters (John Doerr) — OKR framework
3. Metabase — open-source BI dashboard
4. Apache Superset — open-source data exploration
5. Google Looker Studio — free dashboard builder
