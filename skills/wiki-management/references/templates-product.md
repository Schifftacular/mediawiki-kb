# Product Templates

## Domain Hub: Projects/{Name}/Product

Navigation page linking to all product sub-pages.

---

## Page: Product Vision

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Marketing/Target Audience

### What To Generate
- Product vision statement (what the product will become)
- Problem statement (what specific problem the product solves)
- Solution hypothesis (how the product solves it)
- Success metrics (how to know if the product is working)
- Product principles (3-5 guiding rules for product decisions)
- Scope boundaries (what this product is NOT)
- Long-term product direction (1-year, 3-year view)

### Prompting Framework
Start with: "If {name}'s product worked perfectly, what would change in the user's life?" Work backwards from the ideal outcome to the current reality. Use the Product Vision Board: Target Group → Needs → Product → Business Goals. Ensure the vision connects to the Summary's mission and the Target Audience's pain points.

### Session Type
Claude Desktop or Cowork — strategic and visionary. Requires understanding both user needs and business goals.

### Downstream Effects
- Features (features must serve the vision)
- Roadmap (roadmap must progress toward the vision)
- User Journeys (journeys must deliver the vision)
- Architecture (technical architecture must support the vision)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — vision exploration
2. brand-strategist — product-brand alignment
3. ui-ux-pro-max — user experience vision
4. interface-design — interface vision
5. react-patterns — product pattern exploration
6. nextjs-best-practices — modern web product patterns
7. api-design-principles — platform product vision
8. backend-architect — technical feasibility
9. e2e-testing-patterns — product quality vision
10. find-skills — discover product skills

#### MCP Servers
1. Notion — product research and planning
2. Supabase — product data model exploration
3. Context7 — technology feasibility research

#### Resources
1. Inspired (Marty Cagan) — product vision methodology
2. Lean Product Playbook (Dan Olsen) — product-market fit
3. Shape Up (Basecamp) — product development methodology
4. Product Vision Board template (Roman Pichler)
5. Productboard — product management reference

---

## Page: Features

### Prerequisites
- Projects/{Name}/Product/Product Vision
- Projects/{Name}/Marketing/Target Audience

### What To Generate
- Feature inventory (all planned features with brief descriptions)
- Feature priority matrix (impact vs. effort)
- MVP feature set (minimum for launch)
- Feature specifications (for top-priority features)
- Feature dependencies (which features require others)
- Feature-persona mapping (which features serve which personas)
- Cut list (features explicitly deferred or rejected, with reasons)

### Prompting Framework
Start from the Target Audience's jobs-to-be-done. For each job, ask: "What's the simplest feature that gets this job done?" Resist feature creep — apply the "Would the user pay for this alone?" test. Use the MoSCoW method: Must have, Should have, Could have, Won't have. Build the MVP from "Must haves" only.

### Session Type
Claude Code — structured, may involve technical specification. Benefits from code context if building.

### Downstream Effects
- Roadmap (features determine roadmap)
- User Journeys (journeys use features)
- Architecture (architecture must support features)
- Database Schema (schema must store feature data)
- API Reference (API must expose feature functionality)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — feature ideation
2. ui-ux-pro-max — feature UX
3. interface-design — feature UI
4. react-patterns — feature implementation patterns
5. nextjs-best-practices — web feature patterns
6. api-design-principles — API feature design
7. backend-architect — feature architecture
8. e2e-testing-patterns — feature testing
9. frontend-testing — feature test coverage
10. find-skills — discover product skills

#### MCP Servers
1. Notion — feature tracking and prioritization
2. Asana — feature project management
3. Supabase — feature data requirements

#### Resources
1. MoSCoW Method — prioritization framework
2. RICE Scoring — quantitative prioritization (Intercom)
3. Linear — modern feature tracking tool
4. Productboard — feature management
5. Canny — user feature request tracking

---

## Page: User Journeys

### Prerequisites
- Projects/{Name}/Marketing/Target Audience
- Projects/{Name}/Product/Features

### What To Generate
- End-to-end user journey maps per persona
- Journey stages (Awareness → Consideration → Onboarding → First Value → Retention → Advocacy)
- Touchpoints at each stage
- User emotions at each stage
- Pain points and friction per stage
- Opportunities for delight
- Journey metrics (conversion rates, drop-off points)

### Prompting Framework
Walk through the journey as the persona: "You're [persona name]. You just heard about {name} for the first time. What happens next?" Map every step from discovery to becoming a regular user. At each step, ask: "What could go wrong here? What would make this delightful?" Build the emotional curve alongside the functional journey.

### Session Type
Claude Desktop or Cowork — empathy-driven, storytelling approach.

### Downstream Effects
- UX Notes (UX must support the journey)
- Wireframes (wireframes must map to journey steps)
- Features (features must enable the journey)
- Content Strategy (content must support each journey stage)

### Recommended Tools
#### Plugins & Skills
1. ui-ux-pro-max — journey design
2. interface-design — journey touchpoints
3. brainstorming — journey mapping
4. react-ui-patterns — UI at each journey stage
5. e2e-testing-patterns — journey testing
6. web-design-guidelines — web journey
7. screen-reader-testing — accessible journeys
8. frontend-design — journey implementation
9. nextjs-app-router-patterns — web journey architecture
10. find-skills — discover UX skills

#### MCP Servers
1. Notion — journey documentation
2. Miro — visual journey mapping
3. Stripe — payment journey integration

#### Resources
1. Service Design Tools — journey mapping templates
2. Miro Journey Map Template — visual mapping
3. NNGroup Journey Mapping — best practices
4. Hotjar — user behavior recording
5. FullStory — digital experience analytics

---

## Page: UX Notes

### Prerequisites
- Projects/{Name}/Product/User Journeys
- Projects/{Name}/Brand & Identity/Brand Vision

### What To Generate
- Design principles (3-5 UX principles for this product)
- Interaction patterns (navigation, forms, feedback, loading states)
- Accessibility requirements (WCAG level, specific needs)
- Responsive strategy (mobile-first, breakpoints, adaptive vs. responsive)
- Error handling patterns (how the product communicates errors)
- Onboarding flow design
- Key UX decisions with rationale

### Prompting Framework
Start from the User Journeys — identify the 3 most critical moments. For each, ask: "What does the user see, do, and feel?" Define UX principles that prevent the pain points identified in the journeys. Use Nielsen's 10 Usability Heuristics as a checklist. Focus on the first-time user experience.

### Session Type
Claude Code or Cowork — benefits from seeing actual UI context if building.

### Downstream Effects
- Wireframes (wireframes must follow UX notes)
- Features (features must meet UX requirements)
- Architecture (architecture must support UX requirements like real-time, offline, etc.)
- Brand Guidelines (UX must align with brand)

### Recommended Tools
#### Plugins & Skills
1. ui-ux-pro-max — comprehensive UX design
2. interface-design — interface patterns
3. web-design-guidelines — web UX standards
4. react-ui-patterns — React UX patterns
5. react-patterns — component patterns
6. screen-reader-testing — accessibility
7. frontend-design — UX implementation
8. nextjs-best-practices — Next.js UX patterns
9. e2e-testing-patterns — UX testing
10. find-skills — discover UX skills

#### MCP Servers
1. Notion — UX research and documentation
2. Miro — UX wireframing and ideation
3. Context7 — UI library documentation

#### Resources
1. Nielsen's 10 Usability Heuristics — UX checklist
2. Laws of UX — collection of UX principles
3. Refactoring UI — practical UI/UX tips
4. A11y Project — accessibility checklist
5. Mobbin — mobile UX pattern library

---

## Page: Wireframes

### Prerequisites
- Projects/{Name}/Product/User Journeys
- Projects/{Name}/Product/UX Notes
- Projects/{Name}/Product/Features

### What To Generate
- Low-fidelity wireframes for key screens/flows
- Screen inventory (list of all screens/pages needed)
- Navigation structure (sitemap or app flow)
- Component inventory (reusable UI elements)
- Responsive wireframe notes (mobile vs. desktop differences)
- Interaction annotations (what happens on click, hover, swipe)

### Prompting Framework
Start from the User Journeys — wireframe the critical path first (the minimum screens for the primary persona to achieve their goal). Use text-based wireframe descriptions or ASCII art. For each screen: "What's the one thing the user needs to do here?" Remove everything that doesn't support that action. Add screens for error states and edge cases last.

### Session Type
Claude Code — if generating component structures or design system code. Claude Desktop for conceptual wireframes.

### Downstream Effects
- Architecture (screens inform component architecture)
- Features (wireframes may reveal missing features)
- UX Notes (wireframes may challenge UX assumptions)

### Recommended Tools
#### Plugins & Skills
1. ui-ux-pro-max — wireframe design
2. interface-design — wireframe patterns
3. frontend-design — wireframe to code
4. react-patterns — component wireframes
5. react-ui-patterns — UI pattern wireframes
6. web-design-guidelines — web wireframes
7. nextjs-best-practices — Next.js page wireframes
8. design-md — design system wireframes
9. stitch-loop — iterative wireframe building
10. find-skills — discover design skills

#### MCP Servers
1. Miro — collaborative wireframing
2. Canva — quick wireframe mockups
3. Stitch — screen generation from text

#### Resources
1. Figma (free tier) — industry-standard wireframing
2. Excalidraw — open-source whiteboard for wireframes
3. Balsamiq — rapid wireframing tool
4. Whimsical — flowcharts and wireframes
5. Wireframe.cc — minimal wireframing tool

---

## Page: Roadmap

### Prerequisites
- Projects/{Name}/Product/Product Vision
- Projects/{Name}/Product/Features

### What To Generate
- Phased roadmap (Phase 1: MVP, Phase 2: Growth, Phase 3: Scale)
- Timeline (realistic, with buffers)
- Milestones and success criteria per phase
- Dependencies between phases
- Risk register (what could delay each phase)
- Resource requirements per phase
- Go/no-go criteria between phases

### Prompting Framework
Work backwards from the Product Vision — "What does the product look like in 1 year?" Then: "What must be true for that to happen? What's the minimum viable first step?" Use the Now/Next/Later framework instead of specific dates if timelines are uncertain. For each phase, define the hypothesis being tested and how success is measured.

### Session Type
Claude Code — structured planning, may involve timeline calculations.

### Downstream Effects
- Features (features are organized by roadmap phases)
- Development pages (Architecture, Tech Stack — must support roadmap)
- Finance/Projections (financial model depends on roadmap timing)
- Operations/KPIs (KPIs track roadmap progress)

### Recommended Tools
#### Plugins & Skills
1. brainstorming — roadmap ideation
2. backend-architect — technical roadmap feasibility
3. api-design-principles — API roadmap
4. nextjs-best-practices — web product roadmap
5. react-native-architecture — mobile roadmap
6. e2e-testing-patterns — quality roadmap
7. python-project-structure — backend roadmap
8. comprehensive-review-full-review — roadmap review
9. brand-strategist — roadmap-strategy alignment
10. find-skills — discover planning skills

#### MCP Servers
1. Notion — roadmap tracking
2. Asana — project management
3. Supabase — technical milestone tracking

#### Resources
1. Shape Up (Basecamp) — 6-week cycle roadmapping
2. Now/Next/Later framework — flexible roadmapping
3. Linear — modern product roadmapping
4. ProductPlan — visual roadmapping tool
5. Ganttic — resource-aware roadmapping
