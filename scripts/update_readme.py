import json, re, subprocess
from datetime import datetime
from zoneinfo import ZoneInfo
from logo_resolver import get_logo

stats = json.load(open("stats/stats.json", encoding="utf-8"))

tz = ZoneInfo("Europe/Istanbul")
updated = stats["updated"]
commit_hash = subprocess.getoutput("git rev-parse --short HEAD")
version = open("VERSION.txt").read().strip()

# Her grup için tablo
groups = {}
for c in stats["channels"]:
    g = c["group"]
    if g not in groups:
        groups[g] = []
    groups[g].append(c)

table_blocks = []
for group, channels in groups.items():
    table_blocks.append(f"### {group}\n| Kanal | Ülke | Tür | Logo |")
    table_blocks.append("|------|------|-----|------|")
    for c in channels:
        logo = get_logo(c["name"])
        table_blocks.append(f'| {c["name"]} | {c["country"]} | {c["type"]} | <img src="{logo}" width="32"/> |')
    table_blocks.append(f"![{group} grafiği](stats/charts/{group}.png)\n")

block = f"- **Toplam Kanal:** **{stats['total']}** | **Sürüm:** `v{version}` | **Commit:** `{commit_hash}` | **Güncelleme:** `{updated}`\n\n" + "\n".join(table_blocks)

readme = open("README.md", encoding="utf-8").read()
readme = re.sub(
    r"<!-- STATS-START -->(.*?)<!-- STATS-END -->",
    f"<!-- STATS-START -->\n{block}\n<!-- STATS-END -->",
    readme, flags=re.S
)

# Playlist latest link
readme = re.sub(
    r"https://cdn\.jsdelivr\.net/gh/.*/playlist\.m3u",
    f"https://cdn.jsdelivr.net/gh/k33n26/iptvturk@latest/playlist.m3u",
    readme
)

open("README.md","w",encoding="utf-8").write(readme)
