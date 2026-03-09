# Finance Templates

## Domain Hub: Projects/{Name}/Finance

Navigation page linking to all finance sub-pages.

**Important:** Claude is not a financial advisor. All financial pages should note that projections and strategies are starting frameworks and should be reviewed by a qualified accountant or financial advisor.

---

## Page: Revenue Model

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Product/Features

### What To Generate
- Revenue model type (subscription, transactional, freemium, marketplace, advertising, licensing, etc.) with rationale
- Revenue streams (all ways the business makes money)
- Per-stream details: source, pricing mechanism, expected contribution
- Unit economics (cost per acquisition, lifetime value, payback period)
- Revenue assumptions (conversion rates, churn rates, growth rates)
- Monetization timeline (when each stream activates)
- Revenue model risks and alternatives

### Prompting Framework
Start with: "How does {name} make money? If it doesn't yet, how will it?" Map the value chain — "Who pays? For what? How often? How much?" Compare against competitors' models. Calculate unit economics: "What does it cost to acquire one customer? How much do they pay over their lifetime?" If LTV > 3× CAC, the model works. If not, explore alternatives. Use the Business Model Canvas revenue block.

### Session Type
Claude Desktop — strategic and analytical. May involve spreadsheet-like calculations.

### Downstream Effects
- Pricing (pricing implements the revenue model)
- Projections (projections are based on revenue model assumptions)
- Product/Features (features must support the revenue model)
- Marketing (marketing must drive the revenue model)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — revenue model exploration
2. brand-strategist — revenue-brand alignment
3. backend-architect — technical revenue infrastructure
4. api-design-principles — API monetization
5. comprehensive-review-full-review — model review
6. e2e-testing-patterns — payment flow testing
7. nextjs-best-practices — pricing page implementation
8. web-design-guidelines — pricing page design
9. email-best-practices — billing communications
10. find-skills — discover finance skills

#### MCP Servers
1. Stripe — payment infrastructure and revenue data
2. Notion — revenue model documentation
3. Supabase — subscription data management

#### Resources
1. Strategyzer Business Model Canvas — revenue model framework
2. Stripe Revenue Recognition — revenue accounting
3. ProfitWell — subscription revenue analytics (free)
4. Baremetrics — revenue dashboard (reference)
5. SaaS Metrics 2.0 (David Skok) — SaaS revenue metrics

---

## Page: Pricing

### Prerequisites
- Projects/{Name}/Finance/Revenue Model
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Marketing/Competitive Analysis

### What To Generate
- Pricing strategy (value-based, cost-plus, competitive, penetration, premium)
- Pricing tiers/plans (features, limits, and price per tier)
- Pricing page copy (how pricing is presented to customers)
- Discount and promotion strategy
- Free tier / trial strategy (if applicable)
- Pricing experiments plan (A/B tests, willingness-to-pay research)
- International pricing considerations (PPP, currency)
- Price change policy (how to communicate increases)

### Prompting Framework
Start with: "What's the most your ideal customer would pay for {name} without hesitating?" and "What price would make them think it's too cheap to be good?" Use the Van Westendorp Price Sensitivity Meter. Compare against competitive pricing from the Competitive Analysis page. Design tiers around the Target Audience's willingness to pay, not around features. Ask: "Can someone get value from {name} without paying? What's the trigger to upgrade?"

### Session Type
Claude Desktop — strategic pricing requires understanding psychology and market dynamics.

### Downstream Effects
- Revenue Model (pricing validates revenue assumptions)
- Projections (projections use specific price points)
- Product/Features (features must align with tiers)
- Marketing/Messaging (pricing must be communicated clearly)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — pricing strategy
2. brand-strategist — pricing-brand alignment
3. web-design-guidelines — pricing page design
4. nextjs-best-practices — pricing page implementation
5. react-ui-patterns — pricing UI patterns
6. interface-design — pricing page interface
7. frontend-design — pricing page build
8. comprehensive-review-full-review — pricing review
9. e2e-testing-patterns — pricing flow testing
10. find-skills — discover pricing skills

#### MCP Servers
1. Stripe — pricing implementation (products, prices, subscriptions)
2. Notion — pricing research and planning
3. Context7 — Stripe documentation

#### Resources
1. Pricing Page Teardown (ProfitWell) — real-world pricing analysis
2. Van Westendorp Price Sensitivity Meter — pricing research method
3. Stripe Billing documentation — pricing implementation
4. OpenPricing — open-source pricing experiments
5. Price Intelligently — pricing strategy methodology

---

## Page: Projections

### Prerequisites
- Projects/{Name}/Finance/Revenue Model
- Projects/{Name}/Finance/Pricing
- Projects/{Name}/Finance/Expenses
- Projects/{Name}/Product/Roadmap

### What To Generate
- Three financial scenarios (conservative, base, optimistic)
- Per-scenario monthly projections (12 months) and annual (3 years):
  - Revenue (by stream)
  - Cost of goods sold
  - Gross margin
  - Operating expenses
  - Net income / burn rate
  - Cash position
- Key assumptions per scenario (growth rate, conversion rate, churn rate)
- Break-even analysis (when does the business become profitable?)
- Sensitivity analysis (which assumptions have the biggest impact?)
- Cash runway calculation (how long until money runs out?)

### Prompting Framework
Build bottom-up, not top-down. Start with: "How many customers can you realistically acquire in month 1?" Project forward with modest growth. Never start with market size and assume a percentage — that's fiction. Use the Revenue Model's unit economics. For expenses, list every cost: "What do you have to pay for whether you have 0 customers or 1000?" (fixed costs) and "What costs increase with each customer?" (variable costs). Run three scenarios by varying the growth rate assumption.

### Session Type
Claude Code — involves calculations, may generate spreadsheet formulas or financial models.

### Downstream Effects
- Funding (funding needs depend on projections)
- KPIs (projection targets become KPI goals)
- Roadmap (roadmap must be financially viable)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — scenario planning
2. comprehensive-review-full-review — projection review
3. backend-architect — cost estimation
4. python-project-structure — financial modeling scripts
5. postgres-best-practices — financial data queries
6. supabase-postgres-best-practices — financial analytics
7. brand-strategist — growth strategy
8. api-design-principles — API cost estimation
9. unix-macos-engineer — infrastructure cost estimation
10. find-skills — discover financial modeling skills

#### MCP Servers
1. Stripe — actual revenue data
2. Supabase — financial data storage
3. Notion — financial planning

#### Resources
1. Causal — modern financial modeling
2. Google Sheets financial templates — free spreadsheet models
3. Foresight (YC) — startup financial planning
4. Standard Metrics — SaaS financial benchmarks
5. Pulley — cap table and financial modeling

---

## Page: Funding

### Prerequisites
- Projects/{Name}/Finance/Revenue Model
- Projects/{Name}/Finance/Projections
- Projects/{Name}/Legal/Entity Formation

### What To Generate
- Funding strategy (bootstrapped, angel, VC, grants, crowdfunding, revenue-funded)
- Current funding status (raised to date, source, terms)
- Funding needs (how much, for what, by when)
- Use of funds breakdown (where the money goes)
- Investor pitch framework (if seeking investment)
- Cap table (current and post-funding ownership)
- Term sheet considerations (valuation, dilution, board seats, liquidation preferences)
- Alternative funding sources (grants, competitions, accelerators)

### Prompting Framework
Start with: "Does {name} need external money, or can it grow from revenue?" If bootstrapping, document the path to revenue. If seeking funding, ask: "How much runway do you need to reach the next meaningful milestone?" Never raise more than needed — dilution is permanent. Map: "What milestone will justify 3-5× the current valuation?" That's your fundraising story. Draft the narrative, not just the numbers.

### Session Type
Claude Desktop — strategic, involves storytelling and financial planning.

### Downstream Effects
- Entity Formation (entity type must support funding strategy)
- Projections (funding extends runway)
- Expenses (funding enables spending)
- Roadmap (funding accelerates roadmap)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — funding strategy
2. brand-strategist — investor brand narrative
3. comprehensive-review-full-review — funding plan review
4. code-documentation-doc-generate — pitch deck structure
5. interface-design — pitch deck design
6. web-design-guidelines — investor-facing web
7. email-best-practices — investor communications
8. brand-identity — investor brand perception
9. brand-designer — pitch visual design
10. find-skills — discover fundraising skills

#### MCP Servers
1. Notion — investor pipeline tracking
2. Stripe — revenue proof for investors

#### Resources
1. YC Application — standard startup pitch structure
2. Pitch Deck examples (Slidebean) — real pitch decks
3. Pulley — cap table management
4. AngelList — investor discovery
5. SBIR.gov — government grants for innovation

---

## Page: Expenses

### Prerequisites
- Projects/{Name}/Operations/Team & Roles
- Projects/{Name}/Operations/Vendors & Tools
- Projects/{Name}/Development/Tech Stack

### What To Generate
- Fixed expenses inventory (rent, salaries, subscriptions, insurance)
- Variable expenses inventory (hosting, transaction fees, marketing spend)
- Per-expense details: amount, frequency, category, owner, vendor
- Expense categories and budgets
- Cost optimization opportunities
- Expense approval process
- Monthly burn rate calculation
- Expense tracking system setup

### Prompting Framework
Start with a complete inventory: "List every recurring cost — monthly and annual. Include everything: software, hosting, domains, insurance, legal, accounting, marketing, contractors." Then categorize: fixed vs. variable, essential vs. nice-to-have. Calculate monthly burn rate. Ask: "Which expenses can be reduced without hurting the business? Which will increase as you grow?" Build an expense model that scales with the business.

### Session Type
Claude Code — structured data, may involve spreadsheet generation.

### Downstream Effects
- Projections (expenses feed the financial model)
- Revenue Model (expenses inform break-even requirements)
- Vendors & Tools (tool expenses tracked here)
- KPIs (burn rate is a key metric)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — cost optimization
2. comprehensive-review-full-review — expense review
3. backend-architect — infrastructure cost analysis
4. unix-macos-engineer — server cost optimization
5. api-design-principles — API cost management
6. postgres-best-practices — database cost optimization
7. supabase-postgres-best-practices — Supabase cost management
8. nextjs-best-practices — hosting cost optimization
9. python-project-structure — build cost optimization
10. find-skills — discover finance skills

#### MCP Servers
1. Stripe — payment processing costs
2. Supabase — hosting costs
3. Cloudflare — CDN and infrastructure costs

#### Resources
1. Ramp — expense management platform
2. Mercury — startup banking with expense tracking
3. Brex — startup credit card with expense management
4. Infracost — cloud infrastructure cost estimation
5. AWS/GCP/Azure pricing calculators — infrastructure cost planning
