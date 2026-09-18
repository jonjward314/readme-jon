# Site structure and review plan

Eight-page site for GitHub Pages, with Favorite Quotes awaiting selections.

CSS is locked at the user's request. Reuse the existing styles for new content;
do not change the styling without explicit authorization (see AGENTS.md).

## Home
- The compressed version is misleading.
- Stay with the question.
- An incomplete index.

The revised local design uses a notebook layout with a contents rail, marginal
notes, and expandable questions that link to relevant sections on other pages.
This redesign was approved for publication after local visual review.

## About
- The mind behind the work.
- The mind, not the résumé.
- How I think.
- What matters to me.
- Conversation protocol.

## Projects
- Making sense. Making things.
- What I work on.
- Software & information architecture.
- Manufacturing systems.
- Making & experimentation.
- Have a problem to untangle?

This page describes areas of practice. It does not claim to contain completed
case studies. Add named projects, screenshots, and outcomes when those materials
are available.

## Methods
- Trust & verification online.
- Ten individually collapsible steps within a collapsible method.

The supplied text is preserved, with lists and trust levels formatted for reading.
Native disclosure controls work with keyboard navigation and without JavaScript.

## Favorite Quotes
- Favorite quotes.
- To be determined.
- A few words worth keeping.

The quotes page at /quotes/ is a placeholder until Jon selects the quotes.
Study links and the featured Psalm 19 section have been removed. Original study
source files are retained locally and excluded from the GitHub Pages build.

## Favorite Movies
- Hard Lessons: Lord of War, Hotel Rwanda, Blood Diamond, Schindler's List.
- Loves: Star Wars I–VI, The Lord of the Rings extended editions, Avatar (first
  film only), anything Miyazaki and most Studio Ghibli work, Weathering with You,
  Fast & Furious.

Both categories are collapsible and reuse the existing disclosure styles.

## Music
- Songs and Albums, each collapsible; categories are editable.
- Entries include listening and lyrics links, an optional player, and “What I think.”
- Spotify and YouTube embeds load on request; ordinary links work without JavaScript.
- Selections await user input. No favorites or opinions are invented.

Edit `music/entries.json` and run `python scripts/build_music.py` to update the
static page. See `scripts/MUSIC.md` for entry fields and embed instructions.

## Contact
- Bring the real question.
- What's on your mind?
- Find me on Discord.

## Design and behavior
- Eight directly addressable pages with consistent navigation and current-page state.
- Ink-dark background, warm paper text, and restrained brass accents.
- Literary serif typography, compact navigation, marginal notes, and ruled indexes.
- Responsive reading layouts, expandable questions and project details, and a mobile menu.
- A Discord username copy button with success and failure feedback.
- Keyboard focus, skip links, reduced-motion support, and usable navigation without JavaScript.
- Study source files retained locally, excluded from publication.
- No family information or private source documents added.

## Local checks
Run `python scripts/check_site.py` for local link and page-structure checks.
Run `python -m http.server 8765 --bind 127.0.0.1` to preview the eight HTML pages.
All eight public pages are static HTML and work with a plain HTTP server.
GitHub Pages uses the configuration to exclude the retired study source files.

The main pages are plain HTML with shared CSS and JavaScript. Their header/footer
markup must be kept consistent with the study includes when navigation changes.
