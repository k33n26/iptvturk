import json, re

stats = json.load(open("stats/stats.json", encoding="utf-8"))
version = open("VERSION.txt").read().strip()

rows = [
    f"- **Toplam Kanal:** **{stats['total']}**",
    f"- **Son Güncelleme:** `{stats['updated']}`",
    f"- **Sürüm:** `v{version}`\n",
    "| Grup | Kanal | Değişim |",
    "|------|-------|---------|"
]

for g, c in stats["groups"].items():
    d = stats["diff"][g]
    mark = f"▲ +{d}" if d > 0 else f"▼ {d}" if d < 0 else "—"
    rows.append(f"| {g} | {c} | {mark} |")

block = "\n".join(rows)

readme = open("README.md", encoding="utf-8").read()
readme = re.sub(
    r"<!-- STATS-START -->(.*?)<!-- STATS-END -->",
    f"<!-- STATS-START -->\n{block}\n<!-- STATS-END -->",
    readme,
    flags=re.S
)

readme = re.sub(
    r"https://cdn\.jsdelivr\.net/gh/.*/playlist\.m3u",
    f"https://cdn.jsdelivr.net/gh/k33n26/iptvturk@v{version}/playlist.m3u",
    readme
)

open("README.md", "w", encoding="utf-8").write(readme)
