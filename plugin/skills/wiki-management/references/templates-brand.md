# Brand & Identity Templates

## Domain Hub: Projects/{Name}/Brand & Identity

Brief overview page linking to all brand sub-pages. No Claude Instructions needed — this is a navigation page.

---

## Page: Brand Vision

### Prerequisites
- Projects/{Name}/Summary

### What To Generate
- Brand purpose (why the brand exists beyond making money)
- Brand promise (what the audience can always expect)
- Brand aspiration (what the brand aims to become)
- Core beliefs (3-5 fundamental beliefs that drive the brand)
- Brand archetype (e.g., Creator, Explorer, Caregiver — with rationale)

### Prompting Framework
Use the Brand Strategy Canvas: Purpose → Promise → Personality → Position. Work through each quadrant conversationally. Start by asking: "What change do you want {name} to create in the world?" Then: "If {name} were a person at a dinner party, how would people describe them after they left?" Ground every answer in the Summary page's mission and vision.

### Session Type
Claude Desktop or Cowork — deeply creative and conversational. Requires back-and-forth exploration, not code.

### Downstream Effects
- Brand Voice (voice derives from vision and archetype)
- Brand Personality (personality maps to archetype)
- Brand Guidelines (codifies the vision into rules)
- Positioning (market position must reflect brand promise)
- Messaging (messages must deliver on brand promise)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — brand positioning frameworks
2. brand-identity — identity system design
3. brand-designer — visual identity expertise
4. brainstorming — structured ideation
5. ui-ux-pro-max — brand experience design
6. interface-design — brand expression in interfaces
7. web-design-guidelines — brand-aligned web design
8. 12-principles-of-animation — brand motion language
9. design-md — semantic design tokens
10. find-skills — discover brand-related skills

#### MCP Servers
1. Notion — pull existing brand notes or mood boards
2. Canva — create brand visual explorations
3. Miro — collaborative brand workshops

#### Resources
1. Brand Archetypes framework (Carol Pearson) — 12 archetype model
2. StoryBrand (Donald Miller) — brand messaging framework
3. Branding in Five and a Half Steps (Michael Johnson) — brand design process
4. Open-source brand guideline templates on GitHub
5. Coolors.co — color palette exploration

---

## Page: Brand Voice

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Brand & Identity/Brand Vision
- Projects/{Name}/Brand & Identity/Brand Personality

### What To Generate
- Voice attributes (3-4 adjective pairs with scales, e.g., Formal ←→ Casual)
- Do's and Don'ts list for writing
- Tone variations by context (marketing, support, internal, social)
- Vocabulary preferences (words to use, words to avoid)
- Example copy in the brand voice (3-5 examples across contexts)
- Writing for specific audiences (if the venture has multiple personas)

### Prompting Framework
Start by reading the Brand Vision and Brand Personality pages. Then ask: "Show me 3 examples of communication you love from other brands — and 3 you hate." Use the contrast to triangulate the voice. Draft sample copy in progressively different tones until the user says "that's us." Codify the winning tone into rules.

### Session Type
Claude Desktop or Cowork — this is a creative writing and refinement task. Expect multiple iterations of sample copy.

### Downstream Effects
- Content Strategy (content must use this voice)
- Messaging (messages must match voice attributes)
- Channels (voice may adapt per channel)
- All future content pages

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — voice strategy
2. brand-identity — voice as identity element
3. email-best-practices — voice in email context
4. resend — email delivery with brand voice
5. code-documentation-doc-generate — documentation voice
6. api-documentation-generator — API docs voice
7. react-email — branded email templates
8. brainstorming — voice exploration
9. brand-designer — voice-visual alignment
10. find-skills — discover writing skills

#### MCP Servers
1. Notion — existing voice guidelines or examples
2. Slack — real examples of current communication tone
3. Gmail — email communication examples

#### Resources
1. Voiceandtone.com (Mailchimp) — voice and tone reference
2. Nielsen Norman Group voice guidelines — UX writing voice
3. GOV.UK Content Design Guide — clarity-focused voice principles
4. Hemingway App — simplicity checker
5. The Elements of Style (Strunk & White) — writing fundamentals

---

## Page: Color System

### Prerequisites
- Projects/{Name}/Brand & Identity/Brand Vision
- Projects/{Name}/Brand & Identity/Brand Personality

### What To Generate
- Primary color palette (2-3 colors with hex, RGB, HSL values)
- Secondary/accent palette (2-3 supporting colors)
- Neutral palette (backgrounds, text, borders)
- Semantic colors (success, warning, error, info)
- Color usage rules (when to use each color, minimum contrast ratios)
- Dark mode considerations (if applicable)
- Color meaning/rationale (why each color was chosen, what it represents)

### Prompting Framework
Start with the Brand Vision's archetype and personality. Ask: "What emotions should someone feel when they see {name}?" Map emotions to color psychology. Present 3 palette options with mood boards. Explore each palette in context (logo mock, UI mock, print mock) before finalizing. Reference the 60-30-10 rule for palette balance.

### Session Type
Claude Desktop or Cowork — visual and creative. If the user has design tools, Cowork is ideal for collaborative exploration.

### Downstream Effects
- Logo (must use the color system)
- Imagery (imagery style must complement colors)
- Typography (type colors must follow the system)
- Brand Guidelines (codifies color rules)
- Any UI/UX work in Development

### Recommended Tools
#### Plugins & Skills
1. brand-designer — color system design
2. ui-ux-pro-max — UI color application
3. design-md — design token generation
4. web-design-guidelines — accessible color usage
5. interface-design — color in interface context
6. screen-reader-testing — color accessibility
7. 12-principles-of-animation — color in motion
8. frontend-design — color implementation
9. react-dev — color system in components
10. find-skills — discover design skills

#### MCP Servers
1. Canva — color palette visualization
2. Miro — color exploration boards
3. Notion — existing color research

#### Resources
1. Coolors.co — palette generator and explorer
2. Adobe Color — color wheel and harmony rules
3. Contrast Checker (WebAIM) — WCAG accessibility testing
4. Open Color — open-source color scheme for UI
5. Tailwind CSS Colors — well-designed color scales for reference

---

## Page: Typography

### Prerequisites
- Projects/{Name}/Brand & Identity/Brand Vision
- Projects/{Name}/Brand & Identity/Color System

### What To Generate
- Primary typeface (name, foundry, license, usage context)
- Secondary typeface (for body text or accents)
- Monospace typeface (for code/technical content, if applicable)
- Type scale (heading sizes, body size, small text — with ratios)
- Line height and spacing rules
- Font weight usage (when to use bold, medium, regular, light)
- Web font loading strategy (if digital product)
- Fallback font stack
- Pairing rationale (why these fonts work together)

### Prompting Framework
Start from the Brand Personality — is the brand modern or classic? Playful or serious? Technical or approachable? Present 3 type pairing options with sample text in context (heading + body). Test readability at different sizes. Consider licensing constraints early. Ask: "Where will this typography appear most?" (web, print, app, all).

### Session Type
Claude Desktop or Cowork — visual comparison task. Benefits from seeing type samples side by side.

### Downstream Effects
- Brand Guidelines (codifies typography rules)
- Logo (wordmark must use or complement the type system)
- All UI/UX work
- Content Strategy (typography affects content formatting)

### Recommended Tools
#### Plugins & Skills
1. brand-designer — typographic identity
2. ui-ux-pro-max — type in UI
3. web-design-guidelines — web typography
4. frontend-design — font implementation
5. design-md — typography tokens
6. interface-design — type hierarchy
7. react-dev — font loading in React
8. nextjs-best-practices — font optimization in Next.js
9. screen-reader-testing — type accessibility
10. find-skills — discover typography skills

#### MCP Servers
1. Canva — typography exploration
2. Notion — type research notes

#### Resources
1. Google Fonts — open-source font library
2. Fontjoy — AI-powered font pairing
3. Typescale.com — visual type scale calculator
4. Practical Typography (Butterick) — typography best practices
5. Variable Fonts (v-fonts.com) — modern font technology reference

---

## Page: Logo

### Prerequisites
- Projects/{Name}/Brand & Identity/Brand Vision
- Projects/{Name}/Brand & Identity/Color System
- Projects/{Name}/Brand & Identity/Typography

### What To Generate
- Logo concept and rationale
- Primary logo (full color, horizontal)
- Logo variations (stacked, icon-only, wordmark-only)
- Minimum size requirements
- Clear space rules
- Color variations (full color, single color, reversed, grayscale)
- Incorrect usage examples (what NOT to do)
- File format inventory (SVG, PNG, PDF, etc.)

### Prompting Framework
Start by reviewing the Brand Vision, Color System, and Typography pages. Ask: "Does {name} need a symbol/icon, a wordmark, or both?" Explore the brand name itself — any visual metaphors in the name or concept? Present 3 conceptual directions with rough descriptions before any design. Get alignment on direction before refining.

### Session Type
Claude Desktop or Cowork — conceptual exploration. Note: Claude cannot create final logo files, but can define the brief, explore concepts, and create an SVG approximation. Recommend Canva or a designer for final production.

### Downstream Effects
- Imagery (imagery must complement the logo)
- Brand Guidelines (logo usage rules)
- All marketing materials
- Favicon and app icons (Development)

### Recommended Tools
#### Plugins & Skills
1. brand-designer — logo design principles
2. brand-identity — logo as identity cornerstone
3. brand-strategist — logo strategy
4. ui-ux-pro-max — logo in UI context
5. design-md — logo design tokens
6. interface-design — logo in interface
7. web-design-guidelines — logo on web
8. frontend-design — logo implementation
9. react-dev — logo component
10. find-skills — discover design skills

#### MCP Servers
1. Canva — logo design and iteration
2. Miro — logo concept exploration
3. Notion — logo research and inspiration

#### Resources
1. Logo Design Love (David Airey) — logo design principles
2. Logoipsum — placeholder logo generator for mockups
3. SVG-Edit — open-source SVG editor
4. Inkscape — open-source vector editor
5. Figma (free tier) — collaborative logo design

---

## Page: Imagery

### Prerequisites
- Projects/{Name}/Brand & Identity/Brand Vision
- Projects/{Name}/Brand & Identity/Color System
- Projects/{Name}/Brand & Identity/Brand Personality

### What To Generate
- Photography style guide (lighting, composition, subject matter, mood)
- Illustration style (if applicable — line art, flat, 3D, etc.)
- Icon style (line weight, corner radius, fill vs. stroke)
- Image treatment rules (filters, overlays, cropping)
- Stock photography guidance (where to source, what to avoid)
- Image do's and don'ts with examples
- Accessibility requirements (alt text conventions, contrast)

### Prompting Framework
Start with mood boards — ask the user to describe 3 images that feel like their brand and 3 that don't. Use the contrast to define the visual territory. Map imagery style to the Brand Personality archetype. Present guidelines as "This, not that" pairs for maximum clarity.

### Session Type
Claude Desktop or Cowork — visual and creative. Benefits from sharing example images.

### Downstream Effects
- Brand Guidelines (codifies imagery rules)
- Content Strategy (content imagery must follow these rules)
- Marketing materials
- Product UI (if applicable)

### Recommended Tools
#### Plugins & Skills
1. brand-designer — visual identity
2. ui-ux-pro-max — imagery in UI
3. senior-computer-vision — image analysis
4. vision-specialist — visual AI expertise
5. ai-multimodal — multimedia content
6. interface-design — imagery in interfaces
7. web-design-guidelines — web imagery
8. frontend-design — image implementation
9. screen-reader-testing — image accessibility
10. find-skills — discover visual skills

#### MCP Servers
1. Canva — image exploration and creation
2. Notion — mood boards and visual research
3. Miro — visual collaboration

#### Resources
1. Unsplash — free high-quality stock photography
2. Pexels — free stock photos and videos
3. unDraw — open-source illustrations
4. Heroicons — open-source icon set
5. Noun Project — icon library

---

## Page: Brand Personality

### Prerequisites
- Projects/{Name}/Summary
- Projects/{Name}/Brand & Identity/Brand Vision

### What To Generate
- Brand archetype deep dive (primary and secondary archetypes)
- Personality traits (5-7 traits with descriptions)
- Brand as a person description (age, style, interests, communication style)
- Personality spectrum (where the brand falls on key scales)
- Personality do's and don'ts
- How personality manifests across touchpoints (website, support, social, packaging)

### Prompting Framework
Use the Brand Archetype workshop approach: present all 12 archetypes with brief descriptions. Ask the user to pick their top 3, then narrow to a primary and secondary. For each trait, ask: "Show me a brand that does this well." Build the personality through examples and contrast, not abstract description.

### Session Type
Claude Desktop or Cowork — deeply conversational and exploratory.

### Downstream Effects
- Brand Voice (voice expresses the personality)
- Color System (colors evoke the personality)
- Imagery (visuals reflect the personality)
- Brand Guidelines (personality guides all brand decisions)

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — personality strategy
2. brand-identity — personality as identity
3. brainstorming — personality exploration
4. brand-designer — personality visualization
5. ui-ux-pro-max — personality in UX
6. interface-design — personality in UI
7. web-design-guidelines — personality in web
8. email-best-practices — personality in email
9. content-strategy — personality in content
10. find-skills — discover brand skills

#### MCP Servers
1. Notion — personality research and references
2. Miro — archetype workshops
3. Canva — personality mood boards

#### Resources
1. The Hero and the Outlaw (Margaret Mark) — brand archetypes framework
2. Brand Personality Scale (Jennifer Aaker) — academic personality dimensions
3. Archetypes in Branding (Margaret Hartwell) — visual archetype toolkit
4. 16Personalities.com — personality type reference (for "brand as person")
5. Brand New (UnderConsideration) — real-world brand personality examples

---

## Page: Brand Guidelines

### Prerequisites
- ALL other Brand & Identity pages should be populated first
- Projects/{Name}/Summary

### What To Generate
- Consolidated brand guidelines document
- Quick-reference brand card (one-page summary)
- Logo usage rules (from Logo page)
- Color specifications (from Color System page)
- Typography rules (from Typography page)
- Voice and tone summary (from Brand Voice page)
- Imagery guidelines (from Imagery page)
- Co-branding rules (how to use alongside partner brands)
- Brand governance (who approves brand usage, review process)
- Version history

### Prompting Framework
This is a synthesis page — not a creative session. Read ALL Brand & Identity pages and compile them into a unified, authoritative guidelines document. Ask the user: "Is there anything about the brand we discussed but didn't capture in the individual pages?" Fill gaps, then compile. The guidelines should be usable by someone who hasn't read any other page.

### Session Type
Claude Code — this is a compilation and structuring task, not creative exploration.

### Downstream Effects
- This page IS the downstream effect of all other Brand & Identity pages. When any brand page changes, this page must be updated to reflect the change.

### Recommended Tools
#### Plugins & Skills
1. brand-strategist — guidelines structure
2. brand-identity — guidelines content
3. brand-designer — visual guidelines
4. code-documentation-doc-generate — document structure
5. ui-ux-pro-max — digital brand guidelines
6. web-design-guidelines — web brand compliance
7. design-md — design token documentation
8. api-documentation-generator — structured documentation
9. comprehensive-review-full-review — quality review
10. find-skills — discover documentation skills

#### MCP Servers
1. Notion — existing brand documentation
2. Canva — brand kit creation
3. Miro — brand overview visualization

#### Resources
1. Frontify — brand guidelines platform (for reference)
2. Brandpad — brand guidelines examples
3. Style Guide Guide (bradfrost.com) — meta-guide for style guides
4. Salesforce Lightning Design System — enterprise brand guidelines example
5. Mozilla Brand Hub — open-source brand guidelines example
