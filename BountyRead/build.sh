#!/bin/bash

# run this script to build the static files.
# this runs all prerequisites such as sitemap generation

echo "[+] Generating sitemap"
/usr/bin/python3 gen_sitemap.py

echo "[+] Starting build: Generating _site"
npx eleventy

echo "Build over."

