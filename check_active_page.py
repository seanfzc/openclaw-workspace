#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.6/#baseline"
print(f"Fetching {url}...")

# Note: #baseline won't be sent to server, server sees just /
response = requests.get("http://192.168.2.6/")
soup = BeautifulSoup(response.text, 'html.parser')

# Find all page sections
pages = soup.find_all('section', class_='page')
print(f"Found {len(pages)} page sections")

for page in pages:
    page_id = page.get('id', 'no-id')
    classes = page.get('class', [])
    is_active = 'active' in classes
    print(f"Page: {page_id}, active: {is_active}, classes: {classes}")

# Check baseline specific elements
baseline_section = soup.find('section', id='page-baseline')
if baseline_section:
    print(f"\nBaseline section exists: id={baseline_section.get('id')}")
    
    # Check for baseline file input
    file_input = baseline_section.find('input', id='baseline-file')
    print(f"Baseline file input exists: {file_input is not None}")
    
    # Check for upload form
    upload_form = baseline_section.find('form', id='upload-baseline-form')
    print(f"Upload form exists: {upload_form is not None}")
    
    # Check for print button
    print_btn = baseline_section.find('button', id='print-baseline')
    print(f"Print button exists: {print_btn is not None}")

# Check script tags
scripts = soup.find_all('script', src=True)
print(f"\nFound {len(scripts)} script tags with src")
for script in scripts[:10]:  # First 10
    src = script.get('src', '')
    print(f"  {src}")

# Check if any page has active class
active_pages = [p for p in pages if 'active' in p.get('class', [])]
if not active_pages:
    print("\n⚠️ WARNING: No page has 'active' class!")
    print("This means navigation.js isn't working or JavaScript hasn't run yet.")
else:
    print(f"\n✅ Active page(s): {[p.get('id') for p in active_pages]}")