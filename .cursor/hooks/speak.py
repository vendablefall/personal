#!/usr/bin/env python3
"""Read every agent reply aloud with macOS `say`.

Toggle: create the file `.cursor/hooks/mute` to silence it, delete it to turn it back on.
Voice: change VOICE below (run `say -v '?'` to list installed voices).
"""
import json
import os
import re
import subprocess
import sys

VOICE = "Karen"  # en_AU - closest to a Kiwi accent that ships with macOS
RATE = "185"     # words per minute

HERE = os.path.dirname(os.path.abspath(__file__))
MUTE_FILE = os.path.join(HERE, "mute")


def strip_markdown(text: str) -> str:
    # fenced code blocks -> short placeholder
    text = re.sub(r"```.*?```", " code block. ", text, flags=re.S)
    # inline code
    text = re.sub(r"`([^`]*)`", r"\1", text)
    # images / links -> link text
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    # headings, bold, italics, strikethrough
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"(\*\*|__)(.*?)\1", r"\2", text)
    text = re.sub(r"(\*|_)(.*?)\1", r"\2", text)
    text = re.sub(r"~~(.*?)~~", r"\1", text)
    # bullets, numbered lists, blockquotes, hr
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = re.sub(r"^\s*([-*_]\s*){3,}$", "", text, flags=re.M)
    # arrows and symbols that read badly
    text = text.replace("→", " to ").replace("—", ", ").replace("–", ", ")
    return re.sub(r"\n{2,}", "\n", text).strip()


def main() -> None:
    if os.path.exists(MUTE_FILE):
        return
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    text = strip_markdown(payload.get("text") or "")
    if not text:
        return

    # Stop any reply still being read out so they don't overlap.
    subprocess.run(["pkill", "-x", "say"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Detach so the hook returns immediately while speech continues.
    subprocess.Popen(
        ["say", "-v", VOICE, "-r", RATE, text],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


if __name__ == "__main__":
    main()
