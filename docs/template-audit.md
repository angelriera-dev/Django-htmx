# Template Audit

## Purpose
Track template files that are unused or only retained as future building blocks so the frontend can stay lean and easy to refactor.

## Removed in This Pass
- `config/templates/base.html`
- `config/templates/navbar.html`
- `templates/layout/navbar.html`
- `templates/layout/navbar_landing.html`
- `templates/layout/sidebar.html`
- `templates/components/auth_container.html`
- `templates/components/auth_form.html`
- `templates/components/card_stat.html`
- `templates/components/field.html`
- `templates/components/form_field.html`
- `templates/components/input_field.html`
- `templates/components/quick_actions.html`
- `templates/components/section_card.html`
- `templates/components/setting_row.html`
- `templates/components/ui/field.html`
- `templates/components/ui/form_field.html`
- `templates/components/ui/input_field.html`
- `templates/components/ui/quick_actions.html`
- `templates/components/button.html`
- `templates/components/avatar.html`

## Still Present but Not Yet Used Directly
- `templates/account/auth_base.html` — useful auth shell, but not yet adopted by the current account templates.
- `templates/components/modal.html` — reusable modal component, kept for future refactors.
- `templates/components/ui/list.html` — navigation/list helper ready for sidebar/menu reuse.
- `templates/components/ui/menu.html` — sectioned menu helper ready for future reuse.
- `templates/components/ui/table.html` — table helper for future list/detail screens.
- `templates/components/ui/tabs.html` — tabs helper for future settings/detail screens.

## Notes
- The active component set now centers on `templates/components/ui/button.html`, `templates/components/ui/input.html`, `templates/components/ui/link.html`, `templates/components/error_block.html`, `templates/components/badge.html`, `templates/components/navbar.html`, `templates/components/alert.html`, and `templates/components/ui/avatar.html`.
- Before deleting any remaining file, first confirm whether a future page will need it as a reusable global component.

