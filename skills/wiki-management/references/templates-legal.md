# Legal Templates

## Domain Hub: Projects/{Name}/Legal

Navigation page linking to all legal sub-pages.

**Important:** Claude is not a lawyer. All legal pages should include a disclaimer that content is a starting point and must be reviewed by qualified legal counsel before use. Claude can draft, structure, and research — but the user must have an attorney review anything legally binding.

---

## Page: Entity Formation

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Finance/Revenue Model

### What To Generate
- Recommended entity type (LLC, C-Corp, S-Corp, Sole Proprietorship) with rationale
- Jurisdiction recommendation (state of incorporation, registered agent)
- Formation checklist (articles of incorporation, EIN, operating agreement, etc.)
- Ownership structure (founders, equity splits, vesting schedules)
- Tax implications summary
- Annual compliance requirements (filings, fees, reports)
- Timeline and cost estimate for formation
- Intellectual property assignment (ensuring company owns the IP)

### Prompting Framework
Start with: "How many people are involved, and is outside funding planned?" These two questions determine entity type. Walk through the decision tree: Solo + no funding → LLC. Multiple founders or VC → C-Corp. Present the trade-offs clearly. For each requirement, provide the actual form or filing needed, not just the concept. Remind the user: "This is a starting framework — have an attorney review before filing."

### Session Type
Claude Desktop — research and planning. Legal research benefits from conversational exploration.

### Downstream Effects
- Contractor Agreements (entity must exist before signing contracts)
- Terms of Service (entity name and jurisdiction appear in ToS)
- Privacy Policy (entity is the data controller)
- Finance pages (entity type affects tax and accounting)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — entity type evaluation
2. brand-strategist — entity-brand alignment
3. backend-architect — IP and technical ownership
4. comprehensive-review-full-review — legal review
5. code-documentation-doc-generate — legal documentation
6. api-documentation-generator — structured legal docs
7. python-project-structure — code ownership structure
8. unix-macos-engineer — legal filing automation
9. email-best-practices — legal communications
10. find-skills — discover legal skills

#### MCP Servers
1. Notion — legal document tracking
2. Stripe — entity requirements for payments

#### Resources
1. Stripe Atlas — startup incorporation (C-Corp)
2. Clerky — automated legal for startups
3. LegalZoom — entity formation service
4. IRS EIN application — free online
5. SCORE — free business mentoring and legal guidance

---

## Page: Terms of Service

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Legal/Entity Formation
- Projects/{Name}/Product/Features

### What To Generate
- Terms of Service document covering:
  - Acceptance of terms
  - Service description
  - User accounts and responsibilities
  - Acceptable use policy
  - Intellectual property rights
  - Payment terms (if applicable)
  - Limitation of liability
  - Dispute resolution (arbitration vs. court)
  - Termination provisions
  - Governing law and jurisdiction
  - Modification clause
  - Contact information
- Plain-language summary of key terms
- Version number and effective date

### Prompting Framework
Start from the Features page — "What can users do on the platform?" Map each feature to potential terms. Ask: "What's the worst thing a user could do with this feature?" That informs the acceptable use policy. Use existing ToS from similar products as reference (not to copy, but for coverage). Draft in clear, readable language — not legalese. End with: "This MUST be reviewed by an attorney before publishing."

### Session Type
Claude Desktop — legal drafting is conversational and iterative.

### Downstream Effects
- Privacy Policy (ToS and Privacy Policy must be consistent)
- Contractor Agreements (contractor terms must not conflict with user ToS)
- Product features (features must comply with stated terms)

### Recommended Tools
#### Plugins & Skills
1. comprehensive-review-full-review — legal review
2. code-documentation-doc-generate — document structure
3. brainstorming — terms exploration
4. api-design-principles — API terms of use
5. backend-dev-guidelines — data handling terms
6. email-best-practices — terms notification emails
7. web-design-guidelines — terms presentation on web
8. brand-strategist — terms-brand tone alignment
9. screen-reader-testing — terms accessibility
10. find-skills — discover legal skills

#### MCP Servers
1. Notion — legal document management
2. Context7 — legal framework documentation

#### Resources
1. TOS;DR (tosdr.org) — terms of service ratings and examples
2. Docracy — open-source legal documents
3. Common Paper — open-source commercial agreements
4. Termly — free ToS generator
5. Iubenda — terms and privacy compliance platform

---

## Page: Privacy Policy

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Legal/Entity Formation
- Projects/{Name}/Product/Features
- Projects/{Name}/Development/Database Schema

### What To Generate
- Privacy Policy document covering:
  - Data collected (what, how, why)
  - Legal basis for processing (consent, legitimate interest, contract)
  - Data usage (how data is used, shared, stored)
  - Third-party sharing (who data is shared with and why)
  - User rights (access, correction, deletion, portability)
  - Cookie policy
  - Data retention schedule
  - Security measures
  - Children's privacy (COPPA compliance if applicable)
  - International data transfers (GDPR if applicable)
  - Policy updates notification process
  - Contact information and DPO (if required)
- Data inventory (spreadsheet of all data points collected)
- Applicable regulations checklist (GDPR, CCPA, COPPA, etc.)

### Prompting Framework
Start from the Database Schema — "What personal data does the system store?" Map every field to a purpose. Then ask: "What third-party services receive user data?" (analytics, payment processors, email services). For each data point: "Is this necessary? What's the legal basis? How long do we keep it?" Build the policy from the data inventory, not from a template. Always flag: "Have an attorney review for compliance with applicable regulations."

### Session Type
Claude Desktop — legal and technical hybrid. Requires understanding both the data model and privacy law.

### Downstream Effects
- Terms of Service (must reference privacy policy)
- Database Schema (schema must support data deletion/export for user rights)
- Product features (consent mechanisms, data preferences)

### Recommended Tools
#### Plugins & Skills
1. comprehensive-review-full-review — privacy review
2. backend-dev-guidelines — data handling practices
3. postgres-best-practices — data retention in DB
4. supabase-postgres-best-practices — Supabase data policies
5. api-design-principles — API data exposure
6. backend-architect — data architecture privacy
7. e2e-testing-patterns — privacy testing
8. web-design-guidelines — cookie consent UI
9. screen-reader-testing — privacy controls accessibility
10. find-skills — discover privacy skills

#### MCP Servers
1. Notion — privacy documentation
2. Supabase — data inventory from schema
3. Context7 — privacy regulation documentation

#### Resources
1. Iubenda — privacy policy generator
2. GDPR.eu — GDPR compliance guide
3. California AG — CCPA compliance guide
4. Privacy Patterns — design patterns for privacy
5. OWASP Privacy by Design — security-privacy alignment

---

## Page: Contractor Agreements

### Prerequisites
- Projects/{Name}/Legal/Entity Formation
- Projects/{Name}/Operations/Team & Roles

### What To Generate
- Independent contractor agreement template covering:
  - Scope of work
  - Compensation and payment terms
  - Intellectual property assignment (work-for-hire)
  - Confidentiality / NDA provisions
  - Non-compete and non-solicitation (if applicable)
  - Termination provisions
  - Indemnification
  - Insurance requirements
  - Governing law
- Contractor onboarding checklist
- Contractor classification guidance (employee vs. contractor)
- Template for different contractor types (developer, designer, consultant)

### Prompting Framework
Start with: "What types of contractors does {name} use or plan to use?" For each type, define the scope and IP needs. The most critical clause is IP assignment — ask: "Does the contractor create anything that should belong to {name}?" If yes, work-for-hire and IP assignment clauses are essential. Draft in clear language. Flag: "Contractor misclassification is a serious legal risk — have an attorney review."

### Session Type
Claude Desktop — legal drafting, conversational.

### Downstream Effects
- Team & Roles (contractors must be documented)
- Finance/Expenses (contractor costs)
- IP & DMCA (IP ownership chain)

### Recommended Tools
#### Plugins & Skills
1. comprehensive-review-full-review — agreement review
2. code-documentation-doc-generate — agreement structure
3. brainstorming — agreement terms
4. backend-dev-guidelines — developer contractor terms
5. api-design-principles — API contractor terms
6. brand-strategist — brand contractor guidelines
7. email-best-practices — contractor communication
8. unix-macos-engineer — contractor access management
9. python-project-structure — code contribution terms
10. find-skills — discover legal skills

#### MCP Servers
1. Notion — contractor management
2. Stripe — contractor payment processing

#### Resources
1. Common Paper — open-source agreements
2. Bonsai — freelance contract templates
3. HelloSign — free e-signature
4. Deel — contractor management platform
5. IRS Form W-9 — contractor tax documentation

---

## Page: IP & DMCA

### Prerequisites
- Projects/{Name}/Legal/Entity Formation
- Projects/{Name}/Product/Features

### What To Generate
- Intellectual property inventory (trademarks, copyrights, patents, trade secrets)
- IP protection strategy (what to register, what to keep as trade secret)
- Trademark filing plan (if applicable)
- Copyright notice standards
- DMCA compliance plan (if user-generated content):
  - DMCA agent registration
  - Takedown process
  - Counter-notice process
  - Repeat infringer policy
- Open-source license compliance (if using OSS)
- IP assignment chain (ensuring company owns all IP)

### Prompting Framework
Start with: "What does {name} create that has value — code, content, designs, brand assets, data?" Map each to an IP type. For each: "Who created it? Under what terms? Does the company clearly own it?" If there's user-generated content, DMCA compliance is mandatory. If using open-source software, license compliance is mandatory. Draft the protection strategy and flag: "Have an IP attorney review before filing trademarks or relying on these protections."

### Session Type
Claude Desktop — legal research and planning.

### Downstream Effects
- Contractor Agreements (must include IP assignment)
- Terms of Service (must address user IP and DMCA)
- Brand Guidelines (trademark usage rules)

### Recommended Tools
#### Plugins & Skills
1. comprehensive-review-full-review — IP review
2. brainstorming — IP strategy
3. code-documentation-doc-generate — IP documentation
4. backend-dev-guidelines — OSS license compliance
5. python-project-structure — license management
6. brand-strategist — trademark strategy
7. brand-identity — IP-brand alignment
8. api-design-principles — API IP terms
9. web-design-guidelines — copyright notices
10. find-skills — discover IP skills

#### MCP Servers
1. Notion — IP tracking database
2. Context7 — open-source license documentation

#### Resources
1. USPTO (trademark search) — free trademark database
2. Copyright.gov — copyright registration
3. FOSSA — open-source license compliance
4. Creative Commons — content licensing
5. choosealicense.com — OSS license selector

---

## Page: Risk Register

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Product/Features
- Projects/{Name}/Legal/Entity Formation

### What To Generate
- Risk inventory with per-risk:
  - Risk ID and title
  - Description
  - Category (legal, technical, financial, operational, market)
  - Likelihood (1-5)
  - Impact (1-5)
  - Risk score (likelihood × impact)
  - Mitigation strategy
  - Owner
  - Status (open, mitigated, accepted, closed)
- Risk heat map (visual matrix of likelihood vs. impact)
- Top 5 risks with detailed mitigation plans
- Risk review schedule
- Escalation criteria (when a risk becomes a crisis)

### Prompting Framework
Start with: "What keeps you up at night about {name}?" Capture gut-level fears first. Then systematically walk through categories: "What could go wrong technically? Legally? Financially? Operationally? In the market?" For each risk, ask: "What would we do if this happened tomorrow?" If the answer is "I don't know," that's a high-priority risk. Score and prioritize.

### Session Type
Claude Desktop — risk assessment is conversational and requires honest reflection.

### Downstream Effects
- Compliance (compliance addresses legal/regulatory risks)
- Finance/Projections (risk contingencies affect projections)
- Operations/KPIs (risk indicators should be tracked)
- All domain pages (risks may exist in any domain)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — risk identification
2. comprehensive-review-full-review — risk review
3. backend-architect — technical risk assessment
4. api-design-principles — API security risks
5. e2e-testing-patterns — quality risks
6. backend-dev-guidelines — development risks
7. postgres-best-practices — data risks
8. brand-strategist — reputation risks
9. unix-macos-engineer — infrastructure risks
10. find-skills — discover risk management skills

#### MCP Servers
1. Notion — risk tracking database
2. Supabase — risk data storage

#### Resources
1. NIST Risk Management Framework — comprehensive risk methodology
2. OWASP Top 10 — web security risks
3. ISO 31000 — risk management standard
4. Risk Register templates (ProjectManager.com) — free templates
5. Failure Mode and Effects Analysis (FMEA) — systematic risk analysis

---

## Page: Compliance

### Prerequisites
- Projects/{Name}/Legal/Entity Formation
- Projects/{Name}/Legal/Privacy Policy
- Projects/{Name}/Legal/Risk Register
- Projects/{Name}/Product/Features

### What To Generate
- Applicable regulations inventory (federal, state, industry-specific)
- Compliance checklist per regulation
- Compliance calendar (filing deadlines, renewal dates, audit dates)
- Compliance officer/owner designation
- Audit trail requirements
- Reporting obligations
- Penalty/consequence summary per regulation
- Compliance monitoring plan
- Third-party compliance requirements (vendor compliance)

### Prompting Framework
Start from the industry and product: "What regulations apply to a {industry} company that {product description}?" Map regulations systematically: data privacy (GDPR/CCPA), payments (PCI-DSS if handling cards), industry-specific (HIPAA for health, SOX for finance, etc.), employment law, tax obligations. For each: "What specifically must {name} do to comply? What's the penalty for non-compliance?" Create actionable checklists, not just awareness. Flag: "Have a compliance attorney verify the regulatory inventory."

### Session Type
Claude Desktop — research-heavy, regulatory analysis.

### Downstream Effects
- All Legal pages (compliance may require updates to ToS, Privacy Policy, etc.)
- Development (compliance may require technical controls)
- Operations (compliance requires operational procedures)
- Finance (compliance has costs)

### Recommended Tools
#### Plugins & Skills
1. comprehensive-review-full-review — compliance review
2. brainstorming — compliance planning
3. backend-dev-guidelines — technical compliance
4. api-design-principles — API compliance
5. postgres-best-practices — data compliance
6. supabase-postgres-best-practices — data storage compliance
7. e2e-testing-patterns — compliance testing
8. backend-architect — compliance architecture
9. web-design-guidelines — accessibility compliance
10. find-skills — discover compliance skills

#### MCP Servers
1. Notion — compliance tracking
2. Supabase — compliance data storage
3. Context7 — regulatory documentation

#### Resources
1. GDPR.eu — GDPR compliance toolkit
2. OWASP Compliance — security compliance guides
3. SOC 2 Compliance Guide (Vanta) — startup compliance
4. PCI Security Standards Council — payment compliance
5. Comply.ai — compliance automation (reference)
