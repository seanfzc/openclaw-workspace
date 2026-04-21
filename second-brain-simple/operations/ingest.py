#!/usr/bin/env python3
"""
Ingest script for second brain system.
Downloads web content, saves to raw/ with metadata.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from urllib.parse import urlparse
import requests
import hashlib

# Configuration
BASE_DIR = Path(__file__).parent.parent
RAW_DIR = BASE_DIR / "raw"
ARTICLES_DIR = RAW_DIR / "articles"
NOTES_DIR = RAW_DIR / "notes"
CONVERSATIONS_DIR = RAW_DIR / "conversations"
ASSETS_DIR = RAW_DIR / "assets"

# Create directories
for d in [ARTICLES_DIR, NOTES_DIR, CONVERSATIONS_DIR, ASSETS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def sanitize_filename(url):
    """Create a safe filename from URL."""
    parsed = urlparse(url)
    # Combine netloc and path, replace problematic chars
    name = parsed.netloc + parsed.path
    name = name.replace("/", "_").replace(":", "_").replace("?", "_").replace("&", "_")
    # Limit length
    if len(name) > 100:
        name = name[:100]
    return name.strip("_")

def fetch_url(url):
    """Fetch URL content with simple requests."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_article(url, content, title=None, tags=None):
    """Save article to raw/articles/ with metadata."""
    if not content:
        return None
    
    # Generate unique ID
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    timestamp = int(time.time())
    safe_name = sanitize_filename(url)
    filename = f"{timestamp}_{url_hash}_{safe_name}.md"
    filepath = ARTICLES_DIR / filename
    
    # Create metadata
    metadata = {
        "url": url,
        "title": title or url,
        "fetched_at": timestamp,
        "fetched_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(timestamp)),
        "tags": tags or [],
        "source_type": "web_article",
        "filename": filename,
    }
    
    # Write markdown file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title or url}\n\n")
        f.write(f"**URL:** {url}\n")
        f.write(f"**Fetched:** {metadata['fetched_at_iso']}\n")
        f.write(f"**Tags:** {', '.join(tags or [])}\n\n")
        f.write("---\n\n")
        f.write(content)
    
    # Write metadata JSON
    metapath = ARTICLES_DIR / f"{filename}.meta.json"
    with open(metapath, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Saved article to {filepath}")
    return filepath

def main():
    parser = argparse.ArgumentParser(description="Ingest web content into second brain")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--title", help="Custom title")
    parser.add_argument("--tags", help="Comma-separated tags")
    
    args = parser.parse_args()
    
    tags = args.tags.split(",") if args.tags else []
    
    print(f"Fetching {args.url}...")
    content = fetch_url(args.url)
    if content:
        save_article(args.url, content, args.title, tags)
    else:
        print("Failed to fetch content")
        sys.exit(1)

if __name__ == "__main__":
    main()