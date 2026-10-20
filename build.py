# Builds the static site into ./site  (python3 build.py)
import json, shutil, datetime, pathlib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from content import T, CONTACT, GRADES, PHOTOS, STEPS_MEDIA, PRIVACY_UPDATED

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "site"
V = datetime.datetime.now().strftime("%Y%m%d%H%M")
YEAR = datetime.date.today().year

env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))

if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(ROOT / "assets", OUT / "assets")
shutil.copytree(ROOT / "static", OUT, dirs_exist_ok=True)

def jsonld(t):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Aq Balyq",
        "url": CONTACT["site_url"] + t["path"],
        "logo": CONTACT["site_url"] + "/assets/img/og-logo.png",
        "description": t["meta_desc"],
        "email": CONTACT["email"],
        "telephone": CONTACT["phone"],
        "address": {"@type": "PostalAddress", "addressLocality": "Almaty", "addressCountry": "KZ"},
    }, ensure_ascii=False).replace("</", "<\\/")

for lang, t in T.items():
    ctx = dict(t=t, lang=lang, langs=T, c=CONTACT, grades=GRADES, photos=PHOTOS,
               steps_media=STEPS_MEDIA, v=V, year=YEAR, jsonld=jsonld(t))
    page = OUT / t["path"].strip("/") / "index.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(env.get_template("page.html").render(**ctx), encoding="utf-8")
    th = OUT / t["thanks_path"].strip("/") / "index.html"
    th.parent.mkdir(parents=True, exist_ok=True)
    th.write_text(env.get_template("thanks.html").render(**ctx), encoding="utf-8")
    pv = OUT / t["privacy_path"].strip("/") / "index.html"
    pv.parent.mkdir(parents=True, exist_ok=True)
    pv.write_text(env.get_template("legal.html").render(kind="privacy", title=t["privacy_title"], page_key="privacy_path",
                  updated=PRIVACY_UPDATED, noindex=False, **ctx), encoding="utf-8")

en = T["en"]
(OUT / "404.html").write_text(env.get_template("legal.html").render(
    kind="404", title=en["nf_title"], page_key=None, noindex=True, t=en, lang="en", langs=T, c=CONTACT, v=V, year=YEAR), encoding="utf-8")

expires = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)).strftime("%Y-%m-%dT00:00:00Z")
(OUT / ".well-known").mkdir(exist_ok=True)
(OUT / ".well-known" / "security.txt").write_text(
    f"Contact: mailto:{CONTACT['email']}\nExpires: {expires}\nPreferred-Languages: en, ru, kk\nCanonical: {CONTACT['site_url']}/.well-known/security.txt\n")

(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONTACT['site_url']}/sitemap.xml\n")
urls = "".join(f"<url><loc>{CONTACT['site_url']}{t[k]}</loc></url>" for t in T.values() for k in ("path", "privacy_path"))
(OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
print("built", OUT)
