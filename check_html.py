#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys

url = "http://192.168.2.6/"
print(f"Fetching {url}...")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all page sections
pages = soup.find_all('section', class_='page')
print(f"Found {len(pages)} page sections")

for page in pages:
    page_id = page.get('id', 'no-id')
    classes = page.get('class', [])
    is_active = 'active' in classes
    print(f"Page: {page_id}, active: {is_active}, classes: {classes}")

# Check nav links
nav_links = soup.select('.nav-links a')
print(f"\nFound {len(nav_links)} nav links")
for link in nav_links:
    data_page = link.get('data-page', 'none')
    is_active = 'active' in link.get('class', [])
    print(f"Nav link data-page='{data_page}', active: {is_active}")

# Check if any script tags have errors (can't check)
# Print the debug script if exists
debug_script = soup.find('script', string=lambda t: t and 'DEBUG' in t)
if debug_script:
    print("\nDebug script found")
    # print first few chars
    text = debug_script.string[:100] if debug_script.string else ''
    print(f"Script start: {text}...")

# Check if baseline page has required elements
baseline = soup.find('section', id='page-baseline')
if baseline:
    print("\nBaseline section found")
    file_input = baseline.find('input', id='baseline-file')
    print(f"Baseline file input: {'FOUND' if file_input else 'MISSING'}")
    upload_form = baseline.find('form', id='upload-baseline-form')
    print(f"Upload form: {'FOUND' if upload_form else 'MISSING'}")
    print_button = baseline.find('button', id='print-baseline')
    print(f"Print button: {'FOUND' if print_button else 'MISSING'}")
else:
    print("\nERROR: page-baseline section NOT FOUND")

# Check if dashboard is active
dashboard = soup.find('section', id='page-dashboard')
if dashboard and 'active' in dashboard.get('class', []):
    print("\n⚠️ Dashboard page is active (may override baseline)")
else:
    print("\nDashboard not active")

# Check hash simulation: if URL had #baseline, which page should be active?
print("\nIf URL hash is #baseline, expected active: page-baseline")
print("If navigation.js works, dashboard should NOT be active.")