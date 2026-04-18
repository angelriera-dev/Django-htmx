# Frontend Restructuring Plan

## Goal
Reduce template complexity aggressively by turning repeated page shells, cards, rows, and status layouts into reusable UI components.

## Current State
- The project already uses a shared base shell, dashboard shell, navbar, alert, badge, and `components/ui/*` inputs/buttons/links.
- Most remaining duplication lives in account status pages, dashboard settings/profile/subscription pages, and landing sections.
- No unused legacy templates remain that can be safely deleted without removing real routes.

## Strategy

### 1. Introduce reusable shell components
- Create a shared `components/ui/auth_shell.html` for centered account pages.
- Create a shared `components/ui/status_page.html` for success/warning/info/error pages.
- Create a shared `components/ui/page_header.html` for title + subtitle + actions.

### 2. Extract repeated dashboard blocks
- Split `dashboard/settings.html` into reusable rows:
  - notification toggle row
  - billing row
  - API key row
  - info row
- Split `dashboard/profile.html` into:
  - profile summary card
  - security row cards
  - destructive danger section
- Split `dashboard/subscription_plans.html` into:
  - plan card
  - billing section rows

### 3. Reduce account page duplication
- Convert all account success/error pages to the status page component.
- Convert login/signup/password pages to the auth shell component.
- Keep only page-specific fields and action labels in each file.

### 4. Simplify landing sections
- Extract repeated CTA/feature section patterns into small reusable landing components.
- Keep copy/content specific, but move wrappers and card structure into shared components.

### 5. Standardize semantic states
- Use one palette for:
  - success
  - warning
  - danger
  - info
- Apply them consistently across:
  - badges
  - alerts
  - destructive buttons
  - status pages

### 6. Tighten tests around structure
- Add template tests for new components.
- Keep smoke tests for dashboard and auth routes.
- Add visual regression later once the shells stabilize.

## Expected Outcome
- 20–35% less template markup in account/dashboard pages.
- Easier page refactors because the shell structure becomes shared.
- Fewer places to touch when design tokens or layout spacing change.
- More predictable light/dark behavior across all pages.

## Immediate Next Implementation Order
1. `components/ui/auth_shell.html`
2. `components/ui/status_page.html`
3. `components/ui/page_header.html`
4. Dashboard row/card extraction
5. Landing section extraction

