# Notes for maintaining this site

- Live site: https://aqbalyq-export.netlify.app (Netlify project `aqbalyq-export`, deploys on every push to `main`).
- Build: `pip install -r requirements.txt && python3 build.py` renders `site/` (git-ignored). Check pages locally before pushing.
- All text lives in `content.py`. EN, RU and KZ must stay in sync: any key added to one language goes into all three.
- Copy style: no em dashes, plain direct language, only claims the owner can prove (no HACCP, years of experience, or delivery countries unless confirmed).
- `static/_headers` has a strict CSP (self only, no inline styles or scripts). Do not add third-party scripts, fonts, embeds or `style=""` attributes; if something outside is truly needed, update the CSP and the privacy notice together.
- The inquiry form is a Netlify Form named `inquiry` with a honeypot and a required consent checkbox. Keep `name`, `data-netlify`, `form-name` and the thanks paths intact.
- Never commit business documents, passports, contracts, invoices, price lists or buyer names. Media must have metadata stripped.
- `site_url` in `content.py` must match the live address; change it if the domain changes. Do not point a `.kz` domain at Netlify (.kz hosting must be in Kazakhstan).
- `security.txt` expiry is set one year from build; rebuild at least yearly.
