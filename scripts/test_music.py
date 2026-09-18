"""Test music rendering without fetching or publishing third-party content."""
import unittest
from build_music import embed, render_categories


class MusicTests(unittest.TestCase):
    def category(self, entries):
        return {'categories': [{'id': 'songs', 'title': 'Songs', 'entries': entries}]}

    def test_empty_category_does_not_invent_entries(self):
        html = render_categories(self.category([]))
        self.assertIn('Selections to come.', html)
        self.assertNotIn('<iframe', html)

    def test_links_notes_and_optional_player(self):
        html = render_categories(self.category([{
            'title': 'Test <title>', 'artist': 'Test & artist',
            'music_url': 'https://example.com/listen',
            'lyrics_url': 'https://example.com/lyrics',
            'thoughts': 'First paragraph.\n\nSecond <paragraph>.'
        }]))
        self.assertIn('href="https://example.com/lyrics"', html)
        self.assertIn('<h3>What I think</h3>', html)
        self.assertIn('<p>First paragraph.</p><p>Second &lt;paragraph&gt;.</p>', html)
        self.assertIn('Test &lt;title&gt;', html)
        self.assertNotIn('<iframe', html)

    def test_embeds_are_inert_until_requested(self):
        html = render_categories(self.category([{
            'title': 'Test', 'artist': 'Test',
            'music_url': 'https://example.com/listen',
            'embed_url': 'https://www.youtube.com/embed/abcdefghijk?autoplay=1'
        }]))
        self.assertIn('<template><iframe', html)
        self.assertIn('www.youtube-nocookie.com/embed/abcdefghijk', html)
        self.assertNotIn('autoplay', html)
        self.assertIn('data-load-player hidden', html)
        self.assertIn('Notes to come.', html)

    def test_spotify_player_url(self):
        provider, url, height = embed('https://open.spotify.com/embed/track/' + 'a' * 22)
        self.assertEqual(provider, 'Spotify')
        self.assertEqual(height, 352)
        self.assertTrue(url.startswith('https://open.spotify.com/embed/track/'))

    def test_invalid_links_and_players_are_rejected(self):
        for url in ['javascript:alert(1)', 'http://example.com', 'https://user:pass@example.com']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                render_categories(self.category([{'title': 'T', 'artist': 'A', 'music_url': url}]))
        for url in ['https://evil.example/embed/abcdefghijk',
                    'https://open.spotify.com.evil.example/embed/track/' + 'a' * 22,
                    'https://www.youtube.com/watch?v=abcdefghijk']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                embed(url)

    def test_embed_requires_listening_fallback(self):
        with self.assertRaises(ValueError):
            render_categories(self.category([{'title': 'T', 'artist': 'A',
                'embed_url': 'https://www.youtube.com/embed/abcdefghijk'}]))


if __name__ == '__main__':
    unittest.main()
