# Skill Registry

**Delegator use only.** Any agent that launches sub-agents reads this registry to resolve compact rules, then injects them directly into sub-agent prompts. Sub-agents do NOT read this registry or individual SKILL.md files.

See `_shared/skill-resolver.md` for the full resolution protocol.

**Version**: 1.1.0 | **Last Updated**: 2026-04-18

## User Skills

| Trigger | Skill | Path | Version |
|---------|-------|------|---------|
| Django templates, HTMX, Alpine.js, Tailwind | django-htmx | /home/rag/.config/opencode/skills/django-htmx/SKILL.md | 1.0 |
| Django allauth setup, templates, configuration | django-allauth | /home/rag/.config/opencode/skills/django-allauth/SKILL.md | 1.0 |
| HTMX swap, events, OOB updates, indicators | htmx-patterns | /home/rag/.config/opencode/skills/htmx-patterns/SKILL.md | 1.0 |
| Creating new AI agent skills | skill-creator | /home/rag/.config/opencode/skills/skill-creator/SKILL.md | 1.0 |
| Finding or installing agent skills | skill-installer | /home/rag/.agents/skills/skill-installer/SKILL.md | - |

## Compact Rules

Pre-digested rules per skill. Delegators copy matching blocks into sub-agent prompts as `## Project Standards (auto-resolved)`.

### django-htmx
- Use HTMX attributes first — add JavaScript only when HTMX can't handle it
- Return partial fragments for HTMX requests, full page for regular requests
- Extract reusable HTML to `templates/components/*.html`
- Use DaisyUI v5 components via `@plugin "daisyui"` — no custom CSS when available
- Tailwind v4 uses CSS-first config — no tailwind.config.js
- Include `{% csrf_token %}` in all forms
- Django-allauth templates go in `templates/account/`
- Alpine.js `x-data` must be on parent element for reactivity

### django-allauth
- Templates inherit from `base.html`
- Use `allauth.account` app for authentication views
- Use `allauth.socialaccount` app for OAuth (Google, GitHub, etc.)
- Override templates in `templates/account/` — don't modify package files
- Include `{% load allauth %}` in templates that use allauth tags

### htmx-patterns
- Default swap is `outerHTML` — use `innerHTML` for content-only updates
- Use `hx-swap-oob` for out-of-band updates (multiple elements at once)
- HTMX events: `htmx:load`, `htmx:afterSwap`, `htmx:beforeRequest`, `htmx:afterRequest`
- Loading indicators: use `hx-indicator` attribute + `.htmx-indicator` CSS class
- Use `hx-vals` for inline JSON data, `hx-headers` for custom headers

## Project Conventions

| File | Path | Notes |
|------|------|-------|
| Project overview | /home/rag/proyectos/dj/htmx/AGENT.md | Defines stack and structure |
| Templates | /home/rag/proyectos/dj/htmx/templates/ | Root templates |
| Components | /home/rag/proyectos/dj/htmx/templates/components/ | Reusable UI components |
| Account templates | /home/rag/proyectos/dj/htmx/templates/account/ | allauth templates |
| Dashboard | /home/rag/proyectos/dj/htmx/templates/dashboard/ | App views |

Read the convention files listed above for project-specific patterns and rules. All referenced paths have been extracted — no need to read index files to discover more.
