## Hi, I'm Khaneil Campbell

I'm an enterprise technology professional focused on AI Solutions Engineering and automation. Over five years in IT service management and user support at Columbia University and NYC Health + Hospitals, I've learned how technical needs connect to the people and processes around them.

That perspective informs my independent AI projects, most of all [**AI Ops Atlas**](https://github.com/khaneilcampbell/ai-ops-atlas), a desktop command center for AI agents and repositories with a Claude agent that audits code on a schedule and a budget. Every write action in it needs a human, a confirmation dialog and Touch ID. I focus on clear task design, careful testing, documentation and human review.

My CompTIA Security+ and ITIL 4 Foundation certifications, along with a Splunk SOC detection lab based on a simulated brute-force scenario, reinforce my attention to security and reliability. I'm pursuing AI Solutions Engineering roles where I can understand customer needs, design and implement workflows and support adoption.

*Fix it twice, document it. Ten times, automate it.*

[khaneilcampbell.com](https://khaneilcampbell.com) · [LinkedIn](https://www.linkedin.com/in/khaneil-campbell) · contact@khaneilcampbell.com

---

## Production systems

Three systems built to run unattended, each with tests, CI and security scanning on every pull request.

### [AI Ops Atlas](https://github.com/khaneilcampbell/ai-ops-atlas) · macOS app and [web](https://ai-ops-atlas.pages.dev)

A command center for AI agents and GitHub repositories, with a Claude agent that audits any repository on a schedule and budget.

![AI Ops Atlas workspace map: each project is a district, its repository the HQ, its agents the buildings around it](assets/atlas-map.png)

- **Problem:** agents, workflows and repositories were spread across n8n, CrewAI, GitHub Actions and local scripts with no single view of what was running, idle or failing.
- **Built:** TypeScript and React front end, Rust (Tauri) back end, Cloudflare Pages site with GitHub App webhooks for live updates, an agent registry with KPI tracking, and the Repository Intelligence Agent, which reads a repository, asks Claude for a structured assessment and separates verified facts from unverified recommendations.
- **Governance:** read only by default. The two write actions (re run a failed job, merge a ready pull request) are off until enabled per repository, confirmed in a macOS dialog, gated by Touch ID for merges, scoped to their own tokens and audited. API keys live in the macOS Keychain and never reach the web view.
- **Cost control:** per run and per month spend caps checked before any call to Claude; unchanged repositories reuse the saved analysis.

![Agent registry: each GitHub Actions agent with its schedule, last run, monthly spend cap and run history](assets/atlas-agents.png)
- **Production evidence:** 47k lines across TypeScript and Rust, 300+ automated tests, 8 GitHub Actions workflows (CI, CodeQL, visual regression, design consistency, signed releases), Dependabot, universal macOS release builds.

### [Multi-Agent Commerce Pipeline](https://github.com/khaneilcampbell/multi-agent-commerce-pipeline) · Linux VPS

An autonomous loop in which CrewAI agents on Claude take a digital product from brand research through Canva design to a live Stripe listing, with a human approving every publish. It ran as a systemd service on a Linux VPS and is being moved to a new host.

- **Problem:** turn a seven phase, multi tool product workflow into something a single operator can run unattended without losing control of what goes live.
- **Built:** six CrewAI agents, Canva's remote MCP server through the Anthropic API connector with a Connect API fallback, Stripe products and Payment Links, SQLite state, SMTP delivery of purchased templates, SEO maintenance and a health report, all driven by a systemd service.
- **Governance:** every product publishes as a draft and goes live only after `approve`; idempotency keys on every Stripe create so retries never duplicate; daily caps; three strikes and a product is parked as failed instead of blocking the queue; `pause` and `resume` without stopping the service; gitleaks and pip audit in CI.
- **Production evidence:** 10k lines of Python, 58 tests, preflight checks before each phase, phase results streamed to AI Ops Atlas without sending prompts, copy or keys.

### [Service Desk Intelligence](https://github.com/khaneilcampbell/service-desk-intelligence) · Streamlit and Docker

Ticket analytics for IT service desks: backlog, SLA health, recurring issues and workload, built on the metrics I managed for five years.

- **Problem:** service desk leads see ticket counts but rarely the trends that drive staffing and knowledge decisions.
- **Built:** a typed data model, a synthetic ticket generator so the dashboard runs with no real data, metric functions with written definitions, and a Streamlit front end. One command runs it in Docker.
- **Production evidence:** 26 tests, ruff, CodeQL, MIT licensed, documented data model and deployment guide, SLA targets defined per priority.
- **Next:** a Claude triage layer that summarizes recurring issues and drafts knowledge articles from resolved tickets.

---

## Security engineering

| Project | What it demonstrates |
|---|---|
| [**Splunk Brute Force Detection Lab**](https://github.com/khaneilcampbell/splunk-bruteforce-detection-lab) | SMB brute force from Kali Linux against Windows 11, detected by a Splunk threshold alert (81 failed logons), with case notes generated in Python through the Splunk REST API. CI runs tests and security guardrails |
| [**khaneilcampbell.com**](https://github.com/khaneilcampbell/khaneilcampbell.com) | Portfolio under a strict Content Security Policy with one first party script, a security audit, CodeQL, zizmor and link checks on every pull request |
| [**Security labs**](https://khaneilcampbell.com/labs.html) | Authentication log analysis, a phishing to malware response walkthrough, and access control and account lifecycle workflows |

Security is how the AI work stays deployable: every agent above runs with the least access it needs and a human on every irreversible action.

---

## How I build

1. **Define the failure modes first.** What happens when the model is wrong, the API is down or a retry fires twice. The design answers those before the happy path.
2. **Humans approve writes.** Agents read freely and propose; a person approves anything that spends money, merges code or publishes.
3. **Budget everything.** Token spend, API requests and daily actions are capped and visible.
4. **Verify, then ship.** Every pull request runs tests, linting and security scanning. `main` is protected in every repository.
5. **Document so it can be repeated.** Each repository has a README, SECURITY.md and CONTRIBUTING.md, and the systems report their own runs.

---

## Latest on GitHub

<!-- This section is regenerated daily by .github/workflows/update-readme.yml. Edits between the markers are overwritten. -->
<!-- AUTO:REPOS:START -->
**7** public repositories · **5** stars · Top languages: Python, TypeScript, Astro, HTML

| Repository | About | Language | Updated |
|---|---|---|---|
| [**service-desk-intelligence**](https://github.com/khaneilcampbell/service-desk-intelligence) | — | Python | 2026-10-31 |
| [**benjaire.com**](https://github.com/khaneilcampbell/benjaire.com) | Independent project: static website for Benjaire, a New York company, deployed on GitHub Pages and Cloudflare `accessibility` `cloudflare-pages` `github-pages` `html-css` | Astro | 2026-10-31 |
| [**ai-ops-atlas**](https://github.com/khaneilcampbell/ai-ops-atlas) ★1 | — | TypeScript | 2026-10-31 |
| [**splunk-bruteforce-detection-lab**](https://github.com/khaneilcampbell/splunk-bruteforce-detection-lab) ★1 | Security operations lab simulating SMB brute-force attacks, with Splunk detection engineering and automated case triage in Python `blue-team` `cybersecurity` `detection-engineering` `python` | Python | 2026-10-30 |
| [**multi-agent-commerce-pipeline**](https://github.com/khaneilcampbell/multi-agent-commerce-pipeline) ★2 | Multi-agent product pipeline: CrewAI agents on Claude, Canva MCP, and Shopify, deployed on a Linux VPS `ai-agents` `anthropic` `crewai` `mcp` | Python | 2026-10-30 |
| [**projects-intelligence-hub**](https://github.com/khaneilcampbell/projects-intelligence-hub) | — | Python | 2026-10-29 |
<!-- AUTO:REPOS:END -->

---

## Stack

| Area | Tools |
|---|---|
| **AI and agents** | Claude and the Anthropic API, Claude Code, Model Context Protocol (servers and connectors), CrewAI, n8n, prompt design and structured outputs |
| **Languages** | Python, TypeScript, Rust (Tauri), PowerShell, SQL |
| **Platforms** | Cloudflare Workers and Pages, GitHub Actions, Linux VPS with systemd, Docker, SQLite, Stripe, Streamlit |
| **Security** | Splunk (SPL), CodeQL, gitleaks, pip audit, zizmor, Content Security Policy, MITRE ATT&CK, NIST incident response |
| **Enterprise IT** | ServiceNow, ITIL 4, Knowledge Centered Service, Active Directory, Cisco Duo MFA |

## Certifications

CompTIA Security+ · ITIL 4 Foundation · HDI KCS Foundation · HDI Customer Service Representative · AI Literacy: Advanced Course for Developers, Columbia University

---

Independent work ships under [Benjaire](https://benjaire.com), whose Astro site runs on Cloudflare Workers with Turnstile, Stripe checkout and WCAG 2.2 AA checks on every pull request ([source](https://github.com/khaneilcampbell/benjaire.com)).
