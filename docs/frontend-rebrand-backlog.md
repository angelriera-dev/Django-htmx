# Frontend Rebrand Backlog

## Objective
Modernize the UI of the Django + HTMX app so that navigation, theme handling, dashboard, and auth screens share a consistent design system.

## Scope
- Global shell and theme persistence
- Navigation and sidebar structure
- Shared UI components
- Dashboard pages
- Account/auth pages
- Visual regression testing

## Backlog

### P0 — Foundation
- [ ] Bootstrap theme on `<html>` before first paint
- [ ] Remove duplicated navigation logic
- [ ] Define the dashboard shell and sidebar
- [ ] Normalize shared component styling

### P1 — Core Screens
- [ ] Modernize dashboard home
- [ ] Modernize dashboard settings
- [ ] Modernize subscription plans
- [ ] Modernize dashboard profile
- [ ] Modernize login / signup / logout / password flows

### P1 — Quality Gates
- [ ] Add integration smoke tests for main routes
- [ ] Add visual regression baseline plan
- [ ] Validate light/dark theme persistence
- [ ] Validate responsive navigation alignment

### P2 — Cleanup
- [ ] Remove legacy inline styles
- [ ] Consolidate duplicate templates/components
- [ ] Document UI conventions for future pages

## Success Criteria
- Theme persists across all routes
- Navbar/sidebar alignment is consistent
- Dashboard and account pages share a coherent design system
- Old visual style fragments are removed from key screens
- Core routes render successfully under test

