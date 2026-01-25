import json

with open("stats/stats.json", "r", encoding="utf-8") as f:
    stats = json.load(f)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

groups_md = ""
for group, count in stats["groups"].items():
    groups_md += f"| {group} | {count} |\n"

readme = readme.replace("{{TOTAL}}", str(stats["total_channels"]))
readme = readme.replace("{{DATE}}", stats["last_update"])
readme = readme.replace("{{GROUPS}}", groups_md)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
