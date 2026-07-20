# Curb Appeal

Curb Appeal is a Claude Code and Codex plugin for building professional, production ready business websites that are designed to generate enquiries, bookings, calls, and sales.

It has advanced support for salons, spas, barbershops, nail studios, lash studios, and other beauty businesses. It also supports restaurants, law firms, clinics, real estate businesses, trades, hotels, gyms, educational businesses, and general local businesses.

You describe the business using simple language. Curb Appeal then detects the existing project, recommends the right approach, creates a plan, builds the website, finds suitable images, connects real forms or booking features, and completes the required SEO, accessibility, responsive design, security, performance, and quality assurance work.

You do not need to understand frameworks or technical terminology to use it.

## How It Works

The `website-director` controls a structured workflow with 17 states:

`DETECT → INTAKE → CLASSIFY → RECOMMEND → CONFIRM → PLAN → PREPARE → BUILD → CONTENT → IMAGES → INTEGRATIONS → SEO → RESPONSIVE → TEST → FIX → HANDOFF → COMPLETE`

Progress is saved inside:

```text
.curb-appeal/project-state.json
```

This allows Curb Appeal to continue from the previous state during a later session instead of restarting the entire process.

## Included Skills

### website-director

The main orchestrator that manages the complete workflow and controls the project state.

### project-detector

Checks whether the folder contains a new project or an existing project. It also detects the current technology stack before creating or editing files.

### business-intake

Collects the business requirements using simple questions. You can paste a complete brief, answer questions one at a time, or temporarily use placeholders.

### project-recommender

Recommends the most suitable project type and technology stack based on what the website needs to achieve. It does not require the user to understand framework terminology.

### project-planner

Creates the project plan, writes `project-brief.md`, and prepares the resumable project state file.

### design-system

Creates consistent design tokens, typography, spacing, colours, buttons, forms, cards, and other visual rules before pages are built.

### business-blueprints

Provides page structures, conversion goals, content rules, schema recommendations, and information architecture for different business industries.

### salon-blueprint

Provides advanced support for salons, spas, barbershops, nail studios, lash studios, and beauty businesses. It includes detailed intake requirements, page recipes, content models, booking guidance, and quality standards.

### conversion-copy

Creates clear, outcome focused website copy with strong calls to action.

### content-integrity

Prevents the website from including fabricated reviews, awards, prices, employees, certifications, achievements, or other unverified information. It also prevents unfinished placeholder content from reaching production.

### frontend-craft

Builds the frontend using supported technologies such as Astro, Laravel Blade, Livewire, Inertia, React with Vite, Vue, Svelte, and standard HTML.

### form-integrations

Connects forms to real destinations and verifies that submissions work. It never creates a form that only appears to submit successfully.

### booking-engine

Provides appointment and reservation functionality, including data models, availability management, conflict prevention, notifications, and administration features.

### image-pipeline

Finds suitable images, optimises them, verifies that they work correctly, and records their original sources for future reference.

### responsive-design

Creates a mobile first interface and verifies the website across mobile phones, tablets, laptops, desktops, and other important screen sizes.

### accessibility-audit

Checks the website against WCAG 2.2 AA accessibility requirements.

### seo

Handles technical SEO, page metadata, structured data, sitemap generation, robots configuration, and Core Web Vitals improvements.

### security-audit

Checks CSRF protection, input validation, authorisation, secret management, security headers, webhook handling, and other important security requirements.

### performance-audit

Checks practical Lighthouse targets, page speed, asset optimisation, loading behaviour, and Core Web Vitals.

### deployment-readiness

Creates a deployment checklist based on the technology stack. Curb Appeal never deploys a project without asking for permission.

### launch-audit

Performs a complete quality assurance review before the website is handed over.

### status-badge-system

Creates a centralised status system with consistent labels, accessible colours, reactive updates, status normalisation, and application wide migration.

### client-handoff

Creates a simple handoff document that explains how a nontechnical business owner can manage and maintain the website.

## Installation

Start an interactive Claude Code session by running `claude`.

Then run the following commands:

```text
/plugin marketplace add DevJanidu/curb-appeal
/plugin install curb-appeal@lyco-labs
/reload-plugins
```

For a private repository, make sure GitHub authentication is configured first. You can use:

```bash
gh auth login
```

You can also use an SSH key that has already been added to `ssh-agent`.

Claude Code will reuse your existing Git credentials.

No authentication is required when installing from a public repository.

## Testing a Local Checkout

To test a local copy of the plugin, run:

```text
/plugin marketplace add /path/to/this/repo
/plugin install curb-appeal@lyco-labs
```

Replace `/path/to/this/repo` with the actual location of the repository on your computer.

## Usage

Open Claude Code inside the website project folder and enter:

```text
Use Curb Appeal to build a website for my business. Ask me simple questions.
```

Curb Appeal will:

1. Detect whether the folder contains a new or existing project.
2. Let you paste a business brief, answer simple questions, or use placeholders.
3. Ask what the website should help the business achieve.
4. Recommend a suitable project type and technology stack.
5. Create and save a project plan.
6. Build the website.
7. Add suitable content and images.
8. Connect real contact forms or booking functionality.
9. Complete SEO, responsive design, accessibility, security, and performance work.
10. Test the project and fix identified problems.
11. Create a clear `HANDOFF.md` document.

You do not need to choose or name a framework unless you specifically want to.

## Updating Curb Appeal

Run the following commands to install the latest available version:

```text
/plugin marketplace update lyco-labs
/reload-plugins
```

## Development and Validation

Dependency free validation checks run through continuous integration for every push and pull request.

Validate manifests, versions, frontmatter, references, secrets, and paths:

```bash
python scripts/validate_plugin.py
```

Test the project state schema:

```bash
python scripts/validate_state.py --self-test
```

Test project detection for a specific directory:

```bash
python skills/project-detector/scripts/detect_project.py <dir>
```

Replace `<dir>` with the directory you want to inspect.

## License

Curb Appeal is available under the MIT License.

See the `LICENSE` file for the complete licence terms.
