#!/usr/bin/env python3
import os
from datetime import date

# Directory containing YAML reports
REPORTS_DIR = "../reports"
# Base URL for sitemap
BASE_URL = "https://bountyread.redtrib3.in/reports"

# Get today's date in YYYY-MM-DD format
today = date.today().isoformat()

# Get all YAML files
files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".yaml") or f.endswith(".yml")]
files.sort()  # optional, for consistent ordering

# Start writing sitemap
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    
    # Add homepage
    f.write("  <url>\n")
    f.write(f"    <loc>{BASE_URL.replace('/reports','')}</loc>\n")
    f.write(f"    <lastmod>{today}</lastmod>\n")
    f.write("  </url>\n")
    
    # Add each report
    for file_name in files:
        slug = os.path.splitext(file_name)[0]  # remove .yaml/.yml
        f.write("  <url>\n")
        f.write(f"    <loc>{BASE_URL}/{slug}/</loc>\n")
        f.write(f"    <lastmod>{today}</lastmod>\n")
        f.write("  </url>\n")
    
    f.write("</urlset>\n")

print(f"Sitemap generated with {len(files)} reports in sitemap.xml (lastmod: {today})")
