# Beauty Salon Static Website V1

A responsive static landing page for a beauty salon.

## Files
- `index.html` — page structure/content
- `styles.css` — responsive styling
- `script.js` — mobile navigation, scroll reveals, date minimum and booking demo

## Run locally
Open `index.html` directly in a browser, or use the VS Code Live Server extension.

## V1 scope
- Responsive navigation
- Hero section
- Salon trust indicators
- Services and starting prices
- About section
- Gallery
- Testimonials
- Appointment booking form UI
- Contact/location details
- Responsive mobile design

The booking form is intentionally frontend-only. It does not persist data.

## Django V2 path
The existing HTML can later be split into Django templates:
- `base.html`
- `home.html`
- reusable service/testimonial components
- booking form connected to Django models/views

Likely first models: `Service`, `Staff`, `StaffService`, `Availability`, and `Appointment`.
