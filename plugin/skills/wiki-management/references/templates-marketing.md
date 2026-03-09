# Marketing Templates

## Domain Hub: Projects/{Name}/Marketing

Navigation page linking to all marketing sub-pages. No Claude Instructions needed.

---

## Page: Target Audience

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Brand & Identity/Brand Vision

### What To Generate
- Primary persona (name, demographics, psychographics, goals, frustrations)
- Secondary persona(s) (if applicable)
- Jobs-to-be-done framework (what each persona is trying to accomplish)
- Pain points and current alternatives
- Decision-making process (how they evaluate and choose solutions)
- Where they spend time (online and offline)
- Communication preferences (how they like to be reached)
- Persona anti-patterns (who this is NOT for)

### Prompting Framework
Use the Jobs-to-be-Done framework: "When [situation], I want to [motivation], so I can [expected outcome]." Build each persona from real examples — ask: "Tell me about a specific person you've talked to who would use {name}. What's their day like? What's frustrating them?" Avoid fictional personas; ground them in real observations. If no real users yet, map from the Summary's target market.

### Session Type
Claude Desktop or Cowork — conversational, empathy-driven. The user needs to think about real people, not abstractions.

### Downstream Effects
- Content Strategy (content targets these personas)
- Channels (channels must reach these personas)
- Positioning (position against their alternatives)
- Messaging (messages must resonate with their pain points)
- User Journeys (journeys map to persona goals)
- Brand Voice (voice must resonate with audience)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — audience strategy
2. brainstorming — persona development
3. ui-ux-pro-max — user-centered design
4. interface-design — audience-appropriate design
5. react-ui-patterns — UI for target users
6. e2e-testing-patterns — user flow testing
7. web-design-guidelines — accessible design
8. screen-reader-testing — inclusive design
9. brand-identity — audience-brand alignment
10. find-skills — discover UX research skills

#### MCP Servers
1. Notion — existing user research or interviews
2. Slack — customer feedback channels
3. Stripe — customer data and segments

#### Resources
1. Strategyzer Value Proposition Canvas — persona-value fit
2. JTBD.info — Jobs-to-be-Done framework
3. UserInterviews.com — user research best practices
4. Hubspot Make My Persona — free persona generator
5. Xtensio Persona Template — collaborative persona builder

---

## Page: Content Strategy

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Brand & Identity/Brand Voice

### What To Generate
- Content pillars (3-5 core themes the brand owns)
- Content types per pillar (blog, video, social, email, etc.)
- Content calendar framework (frequency, cadence, ownership)
- SEO keyword strategy (primary and secondary keywords)
- Content funnel mapping (awareness → consideration → decision)
- Distribution strategy (how content gets in front of the audience)
- Content quality bar (minimum standards for publishing)
- Repurposing strategy (how one piece becomes many)

### Prompting Framework
Start with the Target Audience's pain points. Ask: "What questions does your audience ask before they know {name} exists? What about after?" Map questions to the funnel. Define content pillars around clusters of questions. For each pillar, ask: "What format does your audience prefer for this topic?" Build the strategy around audience behavior, not what's easy to produce.

### Session Type
Claude Desktop or Cowork — strategic and conversational. Requires understanding the audience deeply.

### Downstream Effects
- Channels (content must be distributed through channels)
- Messaging (content must use approved messages)
- Brand Voice (all content must follow voice guidelines)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — content strategy alignment
2. brainstorming — content ideation
3. email-best-practices — email content strategy
4. resend — email delivery
5. react-email — email templates
6. api-documentation-generator — technical content
7. code-documentation-doc-generate — documentation content
8. brand-identity — content-brand alignment
9. web-design-guidelines — content presentation
10. find-skills — discover content skills

#### MCP Servers
1. Notion — content calendar and planning
2. Slack — content distribution
3. Gmail — email content

#### Resources
1. Content Marketing Institute — strategy frameworks
2. Ahrefs/Ubersuggest — keyword research (free tiers)
3. Answer The Public — question-based content research
4. Buffer — social content scheduling (free tier)
5. Hemingway App — content readability checker

---

## Page: Channels

### Prerequisites
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Marketing/Content Strategy

### What To Generate
- Channel inventory (all active and planned channels)
- Primary vs. secondary channels with rationale
- Channel-specific strategy (tone, format, frequency per channel)
- Cross-channel integration (how channels work together)
- Channel metrics (what to track per channel)
- Resource requirements per channel
- Channel retirement criteria (when to abandon a channel)

### Prompting Framework
Start from where the Target Audience spends time. Ask: "Where are your potential customers today when they're thinking about the problem {name} solves?" For each channel, apply the ICE framework: Impact × Confidence × Ease. Prioritize ruthlessly — better to own 2 channels than be mediocre on 6.

### Session Type
Claude Desktop — strategic planning, not creative work.

### Downstream Effects
- Content Strategy (content must be adapted per channel)
- Brand Voice (voice may adapt per channel)
- Messaging (messages must be channel-appropriate)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — channel strategy
2. email-best-practices — email channel
3. resend — email infrastructure
4. brainstorming — channel exploration
5. brand-identity — channel-brand consistency
6. web-design-guidelines — web channel
7. react-email — email channel templates
8. api-design-principles — API channel
9. frontend-design — web channel implementation
10. find-skills — discover marketing skills

#### MCP Servers
1. Notion — channel planning and tracking
2. Slack — community channel management
3. Stripe — conversion tracking from channels

#### Resources
1. Reforge Growth Series — channel strategy frameworks
2. Traction (Gabriel Weinberg) — 19-channel framework
3. Buffer — social channel management
4. Mailchimp — email channel (free tier)
5. Google Analytics — channel performance measurement

---

## Page: Positioning

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Marketing/Competitive Analysis
- Projects/{Name}/Brand & Identity/Brand Vision

### What To Generate
- Positioning statement (For [audience] who [need], {name} is a [category] that [benefit]. Unlike [alternatives], {name} [differentiator].)
- Category definition (what market category does this create or belong to)
- Competitive position map (2x2 matrix with key differentiating axes)
- Key differentiators (3-5 things only {name} does or does best)
- Points of parity (where {name} must match competitors)
- Positioning proof points (evidence supporting each claim)

### Prompting Framework
Use the Positioning Statement Template: "For [target] who [need], {name} is a [category] that [key benefit]. Unlike [alternative], {name} [primary differentiator]." Draft 3 versions, each emphasizing a different differentiator. Test each against: "Would the target audience care? Is it true? Can competitors claim the same thing?" Refine to the strongest single statement.

### Session Type
Claude Desktop — strategic, requires competitive thinking.

### Downstream Effects
- Messaging (messages must reinforce the position)
- Content Strategy (content must support the position)
- Brand Vision (position must align with brand promise)
- Product Vision (product must deliver on positioning claims)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — positioning strategy
2. brainstorming — positioning exploration
3. brand-identity — positioning-brand alignment
4. brand-designer — positioning visualization
5. ui-ux-pro-max — positioning in UX
6. interface-design — positioning expression
7. web-design-guidelines — positioning on web
8. email-best-practices — positioning in email
9. api-design-principles — positioning for developer audiences
10. find-skills — discover strategy skills

#### MCP Servers
1. Notion — competitive research
2. Hugging Face — AI model search (if tech positioning)

#### Resources
1. Obviously Awesome (April Dunford) — positioning framework
2. Positioning (Ries & Trout) — classic positioning theory
3. Play Bigger (category design) — creating new categories
4. Miro — positioning map templates (free tier)
5. SWOT Analysis templates — strategic analysis

---

## Page: Competitive Analysis

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Marketing/Target Audience

### What To Generate
- Competitor inventory (direct, indirect, and substitute competitors)
- Feature comparison matrix
- Pricing comparison
- Positioning comparison (how each competitor positions itself)
- Strengths and weaknesses per competitor
- Market gaps and opportunities
- Competitive response playbook (how to react to competitor moves)
- Monitoring plan (how to track competitor changes)

### Prompting Framework
Start broad: "What does someone do today if {name} doesn't exist?" Map all alternatives — including doing nothing or manual workarounds. Then narrow to direct competitors. For each, ask: "What do they do well? What do customers complain about?" Use the SWOT format per competitor. End with: "Where is the whitespace — what does nobody do well?"

### Session Type
Claude Desktop — research and analysis. Claude can search the web for competitor information.

### Downstream Effects
- Positioning (must differentiate from competitors)
- Features (must address gaps competitors miss)
- Pricing (must be competitive or justified)
- Messaging (must counter competitor claims)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — competitive strategy
2. brainstorming — opportunity identification
3. brand-identity — competitive differentiation
4. backend-architect — technical comparison
5. api-design-principles — API comparison
6. web-design-guidelines — UX comparison
7. ui-ux-pro-max — experience comparison
8. e2e-testing-patterns — competitor testing
9. comprehensive-review-full-review — thorough analysis
10. find-skills — discover research skills

#### MCP Servers
1. Notion — competitive intelligence database
2. Context7 — technology documentation comparison

#### Resources
1. Crunchbase — competitor funding and company data
2. SimilarWeb — website traffic comparison (free tier)
3. G2/Capterra — product review comparison
4. Product Hunt — new competitor discovery
5. BuiltWith — technology stack comparison

---

## Page: Messaging

### Prerequisites
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Marketing/Positioning
- Projects/{Name}/Brand & Identity/Brand Voice

### What To Generate
- Core message (one sentence that captures everything)
- Message hierarchy (primary, secondary, supporting messages)
- Audience-specific messaging (different messages per persona)
- Objection handling (common objections with responses)
- Proof points and social proof framework
- Elevator pitch (30-second, 60-second versions)
- Tagline options (3-5 candidates)
- Message testing criteria (how to evaluate which messages work)

### Prompting Framework
Use the StoryBrand framework: Character (audience) → Has a Problem → Meets a Guide ({name}) → Who Gives Them a Plan → That Calls Them to Action → That Helps Them Avoid Failure → And Ends in Success. Draft the full narrative arc, then extract key messages from each step. Test messages by asking: "Would the target persona say this to a friend? Would they click on this?"

### Session Type
Claude Desktop or Cowork — creative writing with strategic structure.

### Downstream Effects
- Content Strategy (content must use approved messages)
- Channels (messages must be adapted per channel)
- All marketing materials

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — messaging strategy
2. brand-identity — message-brand alignment
3. brainstorming — message ideation
4. email-best-practices — email messaging
5. resend — message delivery
6. react-email — message templates
7. web-design-guidelines — web copy
8. ui-ux-pro-max — UX copy
9. interface-design — interface messaging
10. find-skills — discover copywriting skills

#### MCP Servers
1. Notion — message testing and tracking
2. Slack — internal messaging alignment
3. Gmail — email messaging

#### Resources
1. StoryBrand (Donald Miller) — messaging framework
2. Made to Stick (Heath brothers) — memorable messaging
3. Copywriting: Successful Writing for Design (Maslen) — copy fundamentals
4. VeryGoodCopy.com — copywriting examples and principles
5. Copyhackers — conversion copywriting
