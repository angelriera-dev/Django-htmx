# dj-htmx Agent

## Project Overview

Fullstack Django monolith using HTMX, Alpine.js, Tailwind CSS, and DaisyUI for modern SaaS applications.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 6.x |
| Auth | django-allauth |
| Frontend | HTMX + Alpine.js |
| CSS | Tailwind CSS + DaisyUI |
| DB | SQLite (dev) / PostgreSQL (prod) |

## Project Structure

```
dj-htmx/
├── apps/
│   ├── users/          # User management + allauth
│   └── dashboard/      # Main app views
├── templates/
│   ├── components/    # Reusable UI components
│   ├── account/      # allauth templates
│   └── dashboard/    # App templates
├── config/
│   └── settings/     # Django settings
└── requirements.txt
```

## Skills

- **Project Templates** — See `templates/SKILL.md` for template conventions
- **Global Frontend** — Use `django-htmx` skill for HTMX/Alpine.js patterns