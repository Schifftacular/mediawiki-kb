# Development Templates

## Domain Hub: Projects/{Name}/Development

Navigation page linking to all development sub-pages.

---

## Page: Architecture

### Prerequisites
- Projects/{Name}/Product/Product Vision
- Projects/{Name}/Product/Features
- Projects/{Name}/Product/Roadmap

### What To Generate
- High-level system architecture diagram (components and their relationships)
- Architecture style decision (monolith, microservices, serverless, hybrid) with rationale
- Component inventory (frontend, backend, database, cache, queue, etc.)
- Communication patterns (REST, GraphQL, WebSocket, event-driven)
- Data flow diagram (how data moves through the system)
- Infrastructure decisions (cloud provider, hosting, CDN)
- Architecture decision records (ADRs) for key choices
- Scalability considerations (what scales, what doesn't, what breaks first)
- Security architecture (auth, encryption, secrets management)

### Prompting Framework
Start from the Product Vision and Features — "What does this system need to DO?" Map features to technical capabilities. Then ask: "What's the simplest architecture that supports the MVP features?" Apply the KISS principle aggressively. Only add complexity when a specific, current requirement demands it. Document every "why" — architecture decisions without rationale become legacy debt.

### Session Type
Claude Code — technical, may involve generating architecture diagrams as code (Mermaid), configuration files, or initial project scaffolding.

### Downstream Effects
- Tech Stack (stack must support architecture)
- Database Schema (schema must fit architecture's data model)
- API Reference (API design must align with architecture)
- Dev Setup (dev environment must replicate architecture)
- Deployment (deployment must match infrastructure decisions)

### Recommended Tools
#### Plugins & Skills
1. backend-architect — architecture design
2. api-design-principles — API architecture
3. nextjs-best-practices — Next.js architecture
4. react-native-architecture — mobile architecture
5. python-project-structure — Python backend structure
6. backend-dev-guidelines — backend standards
7. react-vite-expert — frontend architecture
8. postgres-best-practices — database architecture
9. supabase-postgres-best-practices — Supabase architecture
10. find-skills — discover architecture skills

#### MCP Servers
1. Supabase — database and auth infrastructure
2. Cloudflare — edge computing and CDN
3. Context7 — framework documentation

#### Resources
1. The Twelve-Factor App — modern app architecture principles
2. System Design Primer (GitHub) — architecture patterns
3. AWS Well-Architected Framework — cloud architecture best practices
4. Mermaid.js — architecture diagram as code
5. C4 Model — architecture visualization framework

---

## Page: Tech Stack

### Prerequisites
- Projects/{Name}/Development/Architecture

### What To Generate
- Frontend stack (framework, language, styling, state management)
- Backend stack (language, framework, ORM, validation)
- Database stack (primary DB, cache, search)
- Infrastructure stack (hosting, CI/CD, monitoring, logging)
- Development tools (editor, linter, formatter, testing)
- Third-party services (auth, email, payments, analytics)
- Version requirements (minimum versions, compatibility matrix)
- Stack decision rationale (why each choice was made)

### Prompting Framework
Start from the Architecture — for each component, ask: "What are the top 3 options? Which does the team already know? Which has the best ecosystem for our needs?" Avoid technology FOMO — choose boring technology where possible. For each choice, document: what it is, why it was chosen, and what would make us reconsider. Check Context7 for latest documentation on candidate technologies.

### Session Type
Claude Code — technical research and decision-making.

### Downstream Effects
- Dev Setup (must install and configure the stack)
- Deployment (must deploy the stack)
- Architecture (stack must support architecture patterns)
- All code in the project

### Recommended Tools
#### Plugins & Skills
1. backend-architect — stack evaluation
2. nextjs-best-practices — Next.js stack
3. react-vite-expert — Vite stack
4. python-project-structure — Python stack
5. backend-dev-guidelines — backend stack standards
6. react-native-architecture — mobile stack
7. prisma-orm-v7-skills — ORM selection
8. postgres-best-practices — database selection
9. e2e-testing-patterns — test tool selection
10. find-skills — discover tech-specific skills

#### MCP Servers
1. Context7 — up-to-date library documentation
2. Supabase — BaaS evaluation
3. Cloudflare — edge platform evaluation

#### Resources
1. StackShare — technology stack comparisons
2. ThoughtWorks Technology Radar — tech trend assessment
3. State of JS/CSS/HTML surveys — ecosystem trends
4. Choose Boring Technology (Dan McKinley) — stack philosophy
5. Awesome lists (GitHub) — curated tool lists per technology

---

## Page: Database Schema

### Prerequisites
- Projects/{Name}/Development/Architecture
- Projects/{Name}/Product/Features

### What To Generate
- Entity-relationship diagram
- Table definitions (columns, types, constraints, indexes)
- Relationship documentation (foreign keys, junction tables)
- Naming conventions (snake_case, singular/plural, prefixes)
- Migration strategy (how schema changes are managed)
- Seed data requirements (initial/reference data)
- Performance considerations (indexes, partitioning, denormalization)
- Data retention and archiving policies

### Prompting Framework
Start from the Features — "What data does each feature need to store?" Map features to entities. Normalize to third normal form first, then denormalize only where performance requires it. For each entity: "What are the required fields? What are the relationships? What queries will run against this?" Design for the queries, not just the data.

### Session Type
Claude Code — highly technical, involves SQL or ORM code generation.

### Downstream Effects
- API Reference (API endpoints must map to data model)
- Features (features depend on data availability)
- Dev Setup (dev environment needs seed data)

### Recommended Tools
#### Plugins & Skills
1. postgres-best-practices — PostgreSQL schema design
2. supabase-postgres-best-practices — Supabase schema
3. prisma-orm-v7-skills — Prisma ORM schema
4. backend-architect — data architecture
5. backend-dev-guidelines — database standards
6. api-design-principles — data-API alignment
7. python-project-structure — migration patterns
8. e2e-testing-patterns — data testing
9. javascript-testing-patterns — data layer testing
10. find-skills — discover database skills

#### MCP Servers
1. Supabase — schema management and migrations
2. Cloudflare D1 — edge database
3. Context7 — ORM documentation

#### Resources
1. Use The Index, Luke — SQL indexing guide
2. DBDiagram.io — visual schema design (free)
3. Prisma Schema reference — ORM schema patterns
4. PostgreSQL documentation — authoritative reference
5. SQLite documentation — for lightweight/edge databases

---

## Page: API Reference

### Prerequisites
- Projects/{Name}/Development/Architecture
- Projects/{Name}/Development/Database Schema
- Projects/{Name}/Product/Features

### What To Generate
- API style guide (REST conventions, naming, versioning)
- Endpoint inventory (all routes with methods, params, responses)
- Authentication scheme (JWT, API keys, OAuth)
- Error response format (standard error structure)
- Rate limiting policy
- Pagination strategy
- Request/response examples per endpoint
- OpenAPI/Swagger specification (if REST)
- GraphQL schema (if GraphQL)

### Prompting Framework
Start from the Features and User Journeys — "What API calls does the frontend need to make?" Map each user action to an API endpoint. Follow REST conventions unless there's a strong reason not to. Design the API from the consumer's perspective, not the database structure. For each endpoint: "What does the client send? What does it receive? What can go wrong?"

### Session Type
Claude Code — technical, involves API specification code.

### Downstream Effects
- Dev Setup (developers need API documentation to build against)
- Features (features depend on API availability)
- Database Schema (API may reveal missing data)

### Recommended Tools
#### Plugins & Skills
1. api-design-principles — API design patterns
2. api-documentation-generator — API doc generation
3. backend-architect — API architecture
4. backend-dev-guidelines — API standards
5. nextjs-best-practices — Next.js API routes
6. python-project-structure — Python API structure
7. prisma-orm-v7-skills — ORM-API integration
8. e2e-testing-patterns — API testing
9. javascript-testing-patterns — API test patterns
10. find-skills — discover API skills

#### MCP Servers
1. Supabase — auto-generated API from schema
2. Context7 — framework API documentation
3. Stripe — payment API integration reference

#### Resources
1. OpenAPI Specification — API description standard
2. Swagger Editor — visual API design
3. Postman — API testing and documentation
4. HTTPie — CLI HTTP client for testing
5. JSON:API specification — API conventions

---

## Page: Dev Setup

### Prerequisites
- Projects/{Name}/Development/Tech Stack
- Projects/{Name}/Development/Database Schema

### What To Generate
- Prerequisites (required software, versions, accounts)
- Step-by-step setup instructions (clone, install, configure, run)
- Environment variables documentation (all env vars with descriptions)
- Database setup (migrations, seed data, test data)
- IDE/editor configuration (recommended extensions, settings)
- Common issues and troubleshooting
- Development workflow (branch strategy, PR process, review guidelines)

### Prompting Framework
Write for a developer joining on their first day. Every step must be copy-pasteable — no "set up your database" without the actual commands. Test the setup by mentally walking through each step. Ask: "What would confuse a new developer? What assumptions am I making about their environment?" Include troubleshooting for every step that could fail.

### Session Type
Claude Code — technical, involves terminal commands and configuration files.

### Downstream Effects
- All development work (developers can't contribute without setup)
- Deployment (deployment setup often parallels dev setup)

### Recommended Tools
#### Plugins & Skills
1. backend-dev-guidelines — dev environment standards
2. python-project-structure — Python dev setup
3. nextjs-best-practices — Next.js dev setup
4. react-vite-expert — Vite dev setup
5. prisma-orm-v7-skills — ORM setup
6. postgres-best-practices — database setup
7. unix-macos-engineer — shell and system setup
8. e2e-testing-patterns — test environment setup
9. frontend-testing — frontend test setup
10. find-skills — discover setup skills

#### MCP Servers
1. Supabase — database setup automation
2. Context7 — framework setup documentation
3. Cloudflare — deployment environment setup

#### Resources
1. Dev Containers — reproducible dev environments
2. Docker — containerized development
3. direnv — per-project environment variables
4. mise-en-place — dev tool version management
5. Homebrew — macOS package management

---

## Page: Deployment

### Prerequisites
- Projects/{Name}/Development/Architecture
- Projects/{Name}/Development/Tech Stack
- Projects/{Name}/Development/Dev Setup

### What To Generate
- Deployment architecture (environments: dev, staging, production)
- CI/CD pipeline configuration
- Deployment checklist (pre-deploy, deploy, post-deploy steps)
- Rollback procedure
- Environment-specific configuration
- Domain and DNS setup
- SSL/TLS configuration
- Monitoring and alerting setup
- Backup and disaster recovery plan
- Cost estimates per environment

### Prompting Framework
Start simple: "How do I get this from my laptop to a URL someone can visit?" Start with the simplest deployment path (Vercel, Railway, Fly.io) and add complexity only when required. For each environment, define: what triggers a deploy, what checks run before deploy, and how to roll back. The production deployment checklist should be something you can follow at 2 AM under stress.

### Session Type
Claude Code — infrastructure as code, CI/CD configuration, deployment scripts.

### Downstream Effects
- Operations/Workflows (deployment is an operational workflow)
- Operations/KPIs (uptime and deploy frequency are KPIs)
- Finance/Expenses (hosting costs)

### Recommended Tools
#### Plugins & Skills
1. backend-architect — deployment architecture
2. backend-dev-guidelines — deployment standards
3. nextjs-best-practices — Next.js deployment
4. python-project-structure — Python deployment
5. unix-macos-engineer — server management
6. e2e-testing-patterns — deployment testing
7. react-vite-expert — frontend deployment
8. prisma-orm-v7-skills — database migrations in deploy
9. comprehensive-review-full-review — deployment review
10. find-skills — discover DevOps skills

#### MCP Servers
1. Cloudflare — Workers, Pages deployment
2. Supabase — database deployment
3. Context7 — deployment documentation

#### Resources
1. Vercel — frontend deployment platform
2. Railway — full-stack deployment
3. Fly.io — global app deployment
4. GitHub Actions — CI/CD
5. Kamal (37signals) — open-source deployment tool
