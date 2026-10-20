# Aq Balyq export website

Static B2B presentation site for Aq Balyq (EN / RU / KZ). Netlify builds it on every push to `main`.

- `content.py`: all text, contacts and the privacy notice. Most edits happen here.
- `templates/`: page layouts (Jinja2).
- `assets/`: CSS, JS, self-hosted fonts (OFL), photos and video clips.
- `static/_headers`: security headers (CSP etc.) and cache rules, copied to the site root.
- `build.py`: renders everything into `site/` (not committed).

Local build: `pip install -r requirements.txt && python3 build.py`, then open `site/index.html` through any static server.

If you add any outside script, font, embed or analytics, update the Content-Security-Policy in `static/_headers` and the privacy notice in `content.py`, or it will be blocked.
