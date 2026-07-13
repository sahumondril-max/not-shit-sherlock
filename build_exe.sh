#!/usr/bin/env bash
set -euo pipefail

# Installs dependencies locally and builds a single-file executable using PyInstaller.
# On Windows run these commands in an elevated or normal Command Prompt / PowerShell.

python3 -m pip install --user -r requirements.txt pyinstaller
pyinstaller --onefile send_webhook.py
echo "Built: dist/send_webhook"
