# Site structure and review plan

Five-page site for GitHub Pages, with Favorite Quotes awaiting selections.

## Home
- Engineer. Writer. Systems thinker.
- Explore.
- Start a conversation.

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

## Favorite Quotes
- Favorite quotes.
- To be determined.
- A few words worth keeping.

The quotes page at /quotes/ is a placeholder until Jon selects the quotes.
Study links and the featured Psalm 19 section have been removed. Original study
source files are retained locally and excluded from the GitHub Pages build.

## Contact
- Bring the real question.
- What's on your mind?
- Find me on Discord.

## Design and behavior
- Five directly addressable pages with consistent navigation and current-page state.
- Dark green, cream, and warm accent colors; readable prose and larger headings.
- Responsive cards and reading layouts, expandable project details, and a mobile menu.
- A Discord username copy button with success and failure feedback.
- Keyboard focus, skip links, reduced-motion support, and usable navigation without JavaScript.
- Study source files retained locally, excluded from publication.
- No family information or private source documents added.

## Local checks
Run `python scripts/check_site.py` for local link and page-structure checks.
Run `python -m http.server 8765 --bind 127.0.0.1` to preview the five HTML pages.
All five public pages are static HTML and work with a plain HTTP server.
GitHub Pages uses the configuration to exclude the retired study source files.

The main pages are plain HTML with shared CSS and JavaScript. Their header/footer
markup must be kept consistent with the study includes when navigation changes.
