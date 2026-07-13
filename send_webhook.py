#!/usr/bin/env python3
"""Send a fixed message to a Discord webhook.

Usage:
  - Set the `DISCORD_WEBHOOK_URL` environment variable, or
  - Pass the webhook URL as the first CLI argument.

Example:
  DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..." python3 send_webhook.py
  python3 send_webhook.py https://discord.com/api/webhooks/...
"""
import os
import sys
import json
import argparse
import urllib.request
import urllib.error

# Optional file-level default. Paste your webhook URL here if you prefer a hardcoded default.
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1517919859747459194/KJo6WPrbOoGM3RaUccvfSAzSMM52GSdTpkJiN_iGCccIuOBZqyithnoHGiZFtGc_x6kq"


def send_message(webhook_url: str, content: str) -> bool:
    payload = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.getcode()
            return 200 <= status < 300
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Request failed: {e}")
    return False


SAVE_FILE = ".webhook"


def load_saved_webhook(path: str = SAVE_FILE) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            url = f.read().strip()
            return url or None
    except FileNotFoundError:
        return None


def save_webhook(url: str, path: str = SAVE_FILE) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(url)


def remove_saved_webhook(path: str = SAVE_FILE) -> bool:
    try:
        os.remove(path)
        return True
    except FileNotFoundError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a fixed message to a Discord webhook.")
    parser.add_argument("webhook", nargs="?", help="Discord webhook URL (overrides saved or env)")
    parser.add_argument("--set", dest="set_url", help="Save given webhook URL to .webhook and exit")
    parser.add_argument("--unset", action="store_true", help="Remove saved webhook file")
    parser.add_argument("--show", action="store_true", help="Show saved webhook URL if any")
    args = parser.parse_args()

    if args.set_url:
        save_webhook(args.set_url)
        print("Saved webhook to .webhook")
        return 0

    if args.unset:
        removed = remove_saved_webhook()
        print("Removed saved webhook") if removed else print("No saved webhook to remove")
        return 0

    if args.show:
        saved = load_saved_webhook()
        if saved:
            print(saved)
            return 0
        else:
            print("No saved webhook")
            return 0

    # Determine webhook precedence: positional arg > env var > saved file > file-level default
    webhook = (
        args.webhook
        or os.environ.get("DISCORD_WEBHOOK_URL")
        or load_saved_webhook()
        or DISCORD_WEBHOOK_URL
    )

    if not webhook:
        print("Provide a Discord webhook URL via --set/argument/DISCORD_WEBHOOK_URL or save one with --set.")
        return 2

    content = "hello gng wsp"
    success = send_message(webhook, content)
    if success:
        print("Message sent successfully.")
        return 0
    else:
        print("Failed to send message.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
