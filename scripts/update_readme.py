#!/usr/bin/env python3
"""Refresh the auto-generated parts of README.md from my public GitHub repositories.

Only the text between the AUTO markers is rewritten. Everything else in the
README stays hand-written. Uses the Python standard library only.

Usage:
    python3 scripts/update_readme.py                 # fetch from the GitHub API
    python3 scripts/update_readme.py --repos-json f  # use saved API output instead
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

USER = os.environ.get("PROFILE_USER", "khaneilcampbell")
README = Path(__file__).resolve().parent.parent / "README.md"

# Repositories that never appear in the generated sections.
EXCLUDE = {USER}
RECENT_COUNT = 6
TOP_LANGUAGES = 5

START = "<!-- AUTO:REPOS:START -->"
END = "<!-- AUTO:REPOS:END -->"


def fetch_repos(user, token=None):
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/users/{user}/repos?type=owner&per_page=100&page={page}"
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            batch = json.load(resp)
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def visible(repos):
    return [
        r for r in repos
        if not r.get("fork") and not r.get("archived") and not r.get("private")
        and r["name"] not in EXCLUDE
    ]


def cell(text):
    """Keep user text from breaking the Markdown table."""
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render(repos):
    repos = visible(repos)
    langs = Counter(r["language"] for r in repos if r.get("language"))
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    top = ", ".join(name for name, _ in langs.most_common(TOP_LANGUAGES)) or "n/a"

    lines = [
        f"**{len(repos)}** public repositories · **{stars}** stars · Top languages: {top}",
        "",
        "| Repository | About | Language | Updated |",
        "|---|---|---|---|",
    ]
    recent = sorted(repos, key=lambda r: r.get("pushed_at") or "", reverse=True)[:RECENT_COUNT]
    for r in recent:
        about = cell(r.get("description")) or "—"
        topics = r.get("topics") or []
        if topics:
            about += " " + " ".join(f"`{t}`" for t in topics[:4])
        star = f" ★{r['stargazers_count']}" if r.get("stargazers_count") else ""
        lines.append(
            f"| [**{cell(r['name'])}**]({r['html_url']}){star} | {about} "
            f"| {cell(r.get('language')) or '—'} | {(r.get('pushed_at') or '')[:10]} |"
        )
    return "\n".join(lines)


def splice(readme, block):
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        raise SystemExit(f"README is missing the {START} / {END} markers")
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", readme, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-json", help="read repositories from this file instead of the API")
    args = ap.parse_args()

    if args.repos_json:
        repos = json.loads(Path(args.repos_json).read_text())
    else:
        repos = fetch_repos(USER, os.environ.get("GITHUB_TOKEN"))

    old = README.read_text()
    new = splice(old, render(repos))
    if new == old:
        print("README already up to date")
        return 0
    README.write_text(new)
    print("README updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
