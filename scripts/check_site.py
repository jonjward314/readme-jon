"""Check the five public pages and their local links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "about/index.html", "projects/index.html",
         "quotes/index.html", "contact/index.html"]


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.assets, self.current = [], [], [], []
        self.h1 = 0
        self.description = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "a":
            self.links.append(a.get("href", ""))
            if a.get("aria-current") == "page":
                self.current.append(a["href"])
        if tag in ("script", "img") and "src" in a:
            self.assets.append(a["src"])
        if tag == "link" and a.get("rel") == "stylesheet":
            self.assets.append(a["href"])
        if tag == "meta" and a.get("name") == "description":
            self.description = bool(a.get("content"))


routes = {}
for name in PAGES:
    routes["/" + name.removesuffix("index.html")] = ROOT / name

errors = []
for route, path in list(routes.items()):
    if path.suffix != ".html":
        continue
    page = Page(path.read_text(encoding="utf-8"))
    if page.h1 != 1 or not page.description:
        errors.append(f"{route}: needs one h1 and a description")
    if len(page.ids) != len(set(page.ids)):
        errors.append(f"{route}: duplicate IDs")
    if page.current != [route]:
        errors.append(f"{route}: incorrect active navigation {page.current}")
    for link in page.links + page.assets:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        if not parsed.path:
            if parsed.fragment and unquote(parsed.fragment) not in page.ids:
                errors.append(f"{route}: missing anchor {link}")
        elif parsed.path not in routes and not (ROOT / parsed.path.lstrip("/")).is_file():
            errors.append(f"{route}: missing local destination {link}")

study_nav = Page((ROOT / "_includes/site-nav.html").read_text(encoding="utf-8"))
if study_nav.current != ["/quotes/"]:
    errors.append("Study navigation must highlight Favorite Quotes")
for href in study_nav.links:
    if href != "#main" and href not in routes:
        errors.append(f"Study navigation: missing destination {href}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(PAGES)} pages; headings, metadata, active navigation, anchors, assets, and local routes.")
