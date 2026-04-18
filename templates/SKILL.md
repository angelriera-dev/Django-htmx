---
name: project-templates
description: >
  Project-specific template conventions and patterns for dj-htmx.
  Use when modifying any template in templates/ folder.
license: MIT
metadata:
  author: rag
  version: "2.0"
---

## When to Use

Use this skill when:
- Creating or modifying any template in `templates/`
- Adding new components to `templates/components/`
- Refactoring existing templates
- Applying consistent styling across templates

---

## Tech Stack (Current 2026)

| Technology | Version |
|------------|---------|
| HTMX | 2.0.x |
| Alpine.js | 3.15.x |
| Tailwind CSS | v4.x |
| DaisyUI | v5.x |
| Django | 6.x |

See `django-htmx` global skill for detailed patterns.

---

## Project Conventions

### Component Usage

All templates in this project use reusable components from `templates/components/`:

| Component | Purpose |
|-----------|---------|
| `components/ui/button.html` | Submit/action buttons |
| `components/ui/input.html` | Form input fields |
| `components/ui/link.html` | Anchor links |
| `error_block.html` | Form error display |

### Styling System

- **Tailwind CSS** with utility classes
- **DaisyUI** components preferred over custom CSS
- Color palette: `gray-900` (black), `gray-500` (gray), `red-500` (errors)

### Template Structure

```html
{% extends "base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
{% include "components/..." %}
{% endblock %}
```

---

## Available Components

### button.html

```html
{% include "components/ui/button.html" with text="Submit" icon="fa-solid fa-check" %}
```

Parameters: `text`, `icon`, `no_margin`

### input.html

```html
{% include "components/ui/input.html" with id="id_email" name="email" type="email" label="Email" placeholder="you@example.com" required=True %}
```

Parameters: `id`, `name`, `type`, `label`, `placeholder`, `required`, `no_margin`

### link.html

```html
{% include "components/ui/link.html" with url="account_login" text="Sign in" %}
```

Parameters: `url`, `text`

### error_block.html

```html
{% include "components/error_block.html" %}
```

Parameters: `no_margin`

---

## Current Templates

### Account (allauth)

- `login.html` — Sign in page
- `signup.html` — Registration page
- `password_reset.html` — Password reset

All use components for consistency.

### Dashboard

- `base.html` — Dashboard layout
- `home.html` — Overview page

---

## Adding New Components

1. Create in `templates/components/`
2. Single responsibility
3. Use Tailwind classes
4. Add to this skill document

---

## Reference

- Project README: `templates/README.md`
- Agent: `AGENT.md`
- Global skill: `django-htmx` (for detailed patterns)

---

## External Resources

- [HTMX Docs](https://htmx.org/docs/)
- [Alpine.js Docs](https://alpinejs.dev/)
- [Tailwind CSS v4](https://tailwindcss.com/docs)
- [DaisyUI v5](https://daisyui.com/)
