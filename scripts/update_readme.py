import json
import re

README_FILE = "README.md"
STATS_FILE = "stats/stats.json"

with open(STATS_FILE, "r", encoding="utf-8") as f:
    stats = json.load(f)

total = stats["total_channels"]
date = stats["last_update"]

groups_md = "| Grup | Kanal Sayısı |\n|------|---------------|\n"
for group, count in stats["groups"].items():
    groups_md += f"| {group} | {count} |\n"

stats_block = f"""
## 📊 Kanal İstatistikleri

- **Toplam Kanal:** **{total}**
- **Son Güncelleme:** `{date}`

{groups_md}
""".strip()

with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- STATS-START -->(.*?)<!-- STATS-END -->",
    f"<!-- STATS-START -->\n{stats_block}\n<!-- STATS-END -->",
    content,
    flags=re.S
)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)
