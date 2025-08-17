# PP4 – Outstanding Tasks Tracker

## ✅ Completed

- Favicons integrated (confirmed live)
- Mobile overflow fixes with `fixes.css`
- Auth fixes: Login/Signup/Logout contrast, redirects, and URL settings
- Logout redirect → homepage
- Sticky footer implemented site-wide
- My Bookings empty state CTA added
- "Book Now" button always visible (separate PR deployed & tested)
- Datetime bug fixed (`make_aware` in `forms.py`)

---

## 🟡 Still Outstanding

### Navigation & UX

- [ ] Menu detail page → add “Back” button for navigation clarity
- [ ] Signup form → improve styling/contrast (currently plain Allauth with Bootstrap injected)
- [ ] General styling polish → adjust button colours to match theme (auth buttons especially harsh right now)

### Form & Data Integrity

- [x] Restrict forms so users cannot edit admin-only fields (`status`, `table`)
- [x] Ensure update form resets `status` back to _pending_

### Admin

- [ ] Add “Confirm selected bookings” bulk action in Django admin

### Documentation & Testing

- [ ] Final README version with:
  - UX write-up
  - Manual testing cases (happy path + failure)
  - Screenshots (UI + test results)
  - Deployment instructions
- [ ] Run and screenshot unit tests (`python manage.py test`)
- [ ] Confirm Heroku config var `DEBUG=0` (production)
- [ ] Add superuser credentials for assessor (in README/testing doc, **not public repo**)

---
