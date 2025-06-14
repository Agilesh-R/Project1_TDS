#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Install playwright browser binaries (Chromium etc.)
python -m playwright install

# Set cache path (just to be safe)
export PLAYWRIGHT_BROWSERS_PATH=/opt/render/.cache/ms-playwright
