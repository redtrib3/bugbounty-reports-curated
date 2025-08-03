#!/usr/bin/env python3

import os
import yaml

def render_markdown(report):
    md = f"# {report.get('title', 'No Title')}\n\n"
    md += f"**Platform**: {report.get('platform', 'Unknown')}\n\n"
    md += f"**Bug Type**: {report.get('bug_type', 'Unknown')}\n\n"
    md += f"**Severity**: {report.get('severity', 'Unspecified')}\n\n"
    md += f"## Summary\n{report.get('summary', '').strip()}\n\n"
    md += f"## Steps to Reproduce\n{report.get('steps', '').strip()}\n\n"
    md += f"## Impact\n{report.get('impact', '').strip()}\n\n"
    md += f"## References\n{report.get('references', '').strip()}\n"
    return md

yaml_dir = "reports"
md_dir = "reports-in-md"

for filename in os.listdir(yaml_dir):
    if not filename.endswith(".yaml"):
        continue

    base = filename[:-5]  # strip .yaml
    md_path = os.path.join(md_dir, f"{base}.md")

    if os.path.exists(md_path):
        continue  # skip if md already exists

    yaml_path = os.path.join(yaml_dir, filename)
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    md = render_markdown(data)
    with open(md_path, "w") as f:
        f.write(md)
