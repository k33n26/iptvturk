import json, re

s = json.load(open("stats/stats.json", encoding="utf-8"))

rows = [
    f"- **Toplam Kanal:** **{s['total']}**",
    f"- **Son Güncelleme:** `{s['updated']}`\n",
    "| Grup | Kanal | Değişim |",
    "|------|-------|---------|"
]

for g, c in s["groups"].items():
    d = s["diff"][g]
    mark = f"▲ +{d}" if d > 0 else f"▼ {d}" if d < 0 else "—"
    rows.append(f"| {g} | {c} | {mark} |")

block = "\n".join(rows)

r = open("README.md", encoding="utf-8").read()
r = re.sub(r"<!-- STATS-START -->(.*?)<!-- STATS-END -->",
           f"<!-- STATS-START -->\n{block}\n<!-- STATS-END -->",
           r, flags=re.S)
open("README.md","w",encoding="utf-8").write(r)
