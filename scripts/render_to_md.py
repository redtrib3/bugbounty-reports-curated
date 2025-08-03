#!/usr/bin/env python3

import os
import yaml


def render_markdown(report):
    md = f"# {report.get('title', 'No Title')}\n\n"
    md += f"**Target**: {report.get('target', 'Unknown')}\n\n"
    md += f"**Reported on**: {report.get('reported_platform', 'Unknown')}\n\n"
    md += f"**Bug Type**: {report.get('bug_type', 'Unknown')}\n\n"
    md += f"**Severity**: {report.get('severity', 'Unspecified')}\n\n"
    md += f"**Report URL**: {report.get('report_url', 'Unspecified')}\n\n"
    md += f"## Summary\n{report.get('summary', '').strip()}\n\n"
    md += f"## Bounty received ($)\n{report.get('bounty', 'Unspecified')}\n\n"

    references = report.get('references', "Unspecified")
    tags = report.get('tags', "None")

    if isinstance(references, list):
        md += "## References\n" + "\n".join(f"- {ref}" for ref in references) + "\n"
    else:
        md += f"## References\n{references.strip()}\n"

    if isinstance(tags, list):
        md += "## Tags\n" + "\n".join(f"- {tag}" for tag in tags) + "\n"
    else:
        md += f"## Tags\n{tags}\n"

    return md


testing = "/home/redtrib3/Desktop/bugbounty-reports-curated/"
yaml_dir = testing + "reports"
md_dir = testing + "reports-in-md"

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
