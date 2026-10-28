import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import update_readme as ur  # noqa: E402


def repo(name, **kw):
    base = {
        "name": name,
        "html_url": f"https://github.com/khaneilcampbell/{name}",
        "description": f"{name} description",
        "language": "Python",
        "stargazers_count": 0,
        "pushed_at": "2026-01-01T00:00:00Z",
        "topics": [],
        "fork": False,
        "archived": False,
        "private": False,
    }
    base.update(kw)
    return base


class RenderTests(unittest.TestCase):
    def test_filters_and_orders(self):
        out = ur.render([
            repo("old", pushed_at="2025-01-01T00:00:00Z"),
            repo("new", pushed_at="2026-10-01T00:00:00Z", stargazers_count=3),
            repo("forked", fork=True),
            repo("gone", archived=True),
            repo(ur.USER),
        ])
        self.assertIn("**2** public repositories · **3** stars", out)
        self.assertLess(out.index("**new**"), out.index("**old**"))
        self.assertIn("★3", out)
        for hidden in ("forked", "gone", f"[**{ur.USER}**]"):
            self.assertNotIn(hidden, out)

    def test_escapes_pipes(self):
        out = ur.render([repo("a", description="x | y")])
        self.assertIn("x \\| y", out)

    def test_splice_keeps_surrounding_text(self):
        text = f"intro\n{ur.START}\nstale\n{ur.END}\noutro\n"
        out = ur.splice(text, "fresh")
        self.assertEqual(out, f"intro\n{ur.START}\nfresh\n{ur.END}\noutro\n")

    def test_splice_requires_markers(self):
        with self.assertRaises(SystemExit):
            ur.splice("no markers", "x")


if __name__ == "__main__":
    unittest.main()
