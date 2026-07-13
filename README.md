# send_webhook — send a message to a Discord webhook

This small utility posts the message "hello gng wsp" to a Discord webhook.

Usage
- Set the webhook via environment variable `DISCORD_WEBHOOK_URL`:

```
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..." python3 send_webhook.py
```

- Or pass the webhook URL as the first argument:

```
python3 send_webhook.py https://discord.com/api/webhooks/...
```

Optional convenience commands

- Save a webhook URL for reuse:

```
python3 send_webhook.py --set https://discord.com/api/webhooks/...
```

- Show the saved webhook:

```
python3 send_webhook.py --show
```

- Remove the saved webhook:

```
python3 send_webhook.py --unset
```

Build an executable

- On Windows: install Python, then run:

```
python -m pip install -r requirements.txt pyinstaller
pyinstaller --onefile send_webhook.py
```

- On Linux the same commands produce a Linux binary in `dist/`; to get a Windows `.exe` you must build on Windows or use cross-compilation tooling (not covered here).

Build a Windows `.exe` via GitHub Actions

1. Push this branch to GitHub.
2. Open the repository Actions tab and run the "Build Windows exe" workflow (or trigger via the `workflow_dispatch` event).
3. When the workflow completes, download the `send_webhook-windows` artifact which contains `send_webhook.exe`.

# not-shit-sherlock