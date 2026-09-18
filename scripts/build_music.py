"""Render music/entries.json to static HTML for GitHub Pages. Standard library only."""
from html import escape
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def https_url(value):
    if not isinstance(value, str):
        raise ValueError('Links must be strings')
    url = urlsplit(value)
    if (url.scheme != 'https' or not url.hostname or url.username or url.password
            or any(c.isspace() for c in value)):
        raise ValueError('Use a complete HTTPS link without credentials')
    return escape(value, quote=True)


def embed(value):
    https_url(value)
    url = urlsplit(value)
    if url.port not in (None, 443):
        raise ValueError('Unsupported embed port')
    if url.hostname == 'open.spotify.com' and re.fullmatch(
            r'/embed/(track|album|playlist)/[A-Za-z0-9]{22}', url.path):
        provider, height = 'Spotify', 352
    elif url.hostname in ('www.youtube.com', 'www.youtube-nocookie.com') and re.fullmatch(
            r'/embed/[A-Za-z0-9_-]{11}', url.path):
        provider, height = 'YouTube', 240
    else:
        raise ValueError('Use a Spotify or YouTube embed URL, or keep this as a music link')
    host = 'www.youtube-nocookie.com' if provider == 'YouTube' else 'open.spotify.com'
    # Keep player loading explicit. Drop autoplay/tracking query parameters.
    return provider, f'https://{host}{url.path}', height


def paragraphs(text):
    return ''.join(f'<p>{escape(p)}</p>' for p in text.split('\n\n') if p.strip())


def render_categories(data):
    rendered = []
    ids = set()
    for number, category in enumerate(data['categories'], 1):
        cid = category['id']
        if not re.fullmatch(r'[a-z][a-z0-9-]*', cid) or cid in ids:
            raise ValueError('Category IDs must be unique lowercase slugs')
        ids.add(cid)
        entries = []
        for entry in category['entries']:
            title, artist = entry['title'].strip(), entry['artist'].strip()
            if not title or not artist:
                raise ValueError('Each entry needs a title and artist')
            eid = f"{cid}-entry-{len(entries) + 1}"
            if eid in ids:
                raise ValueError('Duplicate entry ID')
            ids.add(eid)
            links = []
            for key, label in [('music_url', 'Listen'), ('lyrics_url', 'Lyrics')]:
                if entry.get(key):
                    links.append(f'<a class="text-link" href="{https_url(entry[key])}">{label}</a>')
            player = ''
            if entry.get('embed_url'):
                if not entry.get('music_url'):
                    raise ValueError('Embedded entries need a music_url as a fallback')
                provider, src, height = embed(entry['embed_url'])
                player = (
                    f'<div class="music-player"><button class="button" data-load-player hidden '
                    f'aria-controls="{eid}-player">Load {provider} player</button>'
                    f'<template><iframe src="{src}" title="{escape(title, quote=True)} — {provider} player" '
                    f'width="100%" height="{height}" loading="lazy" '
                    'allow="encrypted-media; fullscreen; picture-in-picture" '
                    'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></template>'
                    f'<div id="{eid}-player" class="music-player-slot"></div>'
                    '<p class="copy-status" role="status"></p></div>')
            thoughts = paragraphs(entry.get('thoughts', '')) or '<p>Notes to come.</p>'
            entries.append(
                f'<details class="method-step" id="{eid}"><summary><span class="method-number">'
                f'{len(entries)+1:02}</span><span>{escape(title)} — {escape(artist)}</span>'
                '<span aria-hidden="true">+</span></summary><div class="method-step-body">'
                f'<h3>Listen &amp; lyrics</h3><p>{" · ".join(links) or "Links to come."}</p>'
                f'{player}<h3>What I think</h3>{thoughts}</div></details>')
        inner = '\n'.join(entries) or '<p class="muted">Selections to come.</p>'
        rendered.append(
            f'<details class="method" id="{cid}" open><summary class="method-summary">'
            f'<span class="method-number">{number:02}</span><span><strong>{escape(category["title"])}</strong>'
            f'<small>{escape(category.get("description", ""))}</small></span><span aria-hidden="true">+</span>'
            f'</summary><div class="method-content">{inner}</div></details>')
    return '\n'.join(rendered)


def build():
    data = json.loads((ROOT / 'music/entries.json').read_text(encoding='utf-8'))
    path = ROOT / 'music/index.html'
    source = path.read_text(encoding='utf-8')
    output, count = re.subn(r'<!-- music:start -->.*?<!-- music:end -->',
        lambda match: '<!-- music:start -->\n' + render_categories(data) + '\n<!-- music:end -->',
        source, flags=re.S)
    if count != 1:
        raise ValueError('Expected exactly one music content region')
    path.write_text(output, encoding='utf-8')


if __name__ == '__main__':
    build()
    print('Built music/index.html')
