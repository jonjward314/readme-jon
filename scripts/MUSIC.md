# Editing Music

Edit `music/entries.json`, then run `python scripts/build_music.py`.
Commit the JSON and regenerated `music/index.html` together. GitHub Pages serves
the generated HTML; it does not need Python or a backend.

Categories may be renamed or added. Each needs a unique lowercase `id`, a `title`,
an optional `description`, and an `entries` array.

Each entry accepts these fields:

| Field | Purpose |
| --- | --- |
| `title` | Song or album title; required |
| `artist` | Artist; required |
| `music_url` | Full HTTPS listening link to any service |
| `lyrics_url` | Full HTTPS link to the lyrics |
| `embed_url` | Optional Spotify or YouTube player URL, not iframe HTML |
| `thoughts` | Your “What I think” text; separate paragraphs with `\n\n` |

Omit optional fields until ready. No personal favorites have been invented.
Missing thoughts display “Notes to come.” Lyrics are linked, not copied.

For Spotify, copy the `src` URL from Share → Embed. It should start with
`https://open.spotify.com/embed/track/`, `/album/`, or `/playlist/`.
For YouTube, use `https://www.youtube.com/embed/VIDEO_ID` or its
`www.youtube-nocookie.com` equivalent. The builder uses the latter for playback.
Do not paste an entire iframe. A player entry must also include `music_url` so
visitors can listen if the embed is unavailable or JavaScript is disabled.

Players load only after a visitor clicks their load button. No player autoplays.
Some tracks may have regional, account, or embedding restrictions; the ordinary
listening link remains available. Other services can always be used as links.

Official embed references:
- https://developer.spotify.com/documentation/embeds/tutorials/creating-an-embed
- https://support.google.com/youtube/answer/171780

Run `python scripts/test_music.py` and `python scripts/check_site.py` after editing.
Keep the CSS locked; use the existing page structure and classes.
