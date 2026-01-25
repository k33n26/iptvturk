import json, re

# İkonlar her grup için (istediğin emoji ile değiştirebilirsin)
ICONS = {
    "ULUSAL TV": "🇹🇷",
    "BELGESEL TV": "📚",
    "HABER TV": "📰",
    "YEREL TV": "🏘️",
    "SPOR TV": "⚽",
    "YASAM TV": "🏡",
    "SINEMA-DIZI TV": "🎬",
    "MUZIK TV": "🎵",
    "AVRUPA TV": "🌍"
}

stats = json.load(open("stats/stats.json", encoding="utf-8"))

# Kanal sayısına göre büyükten küçüğe sıralı
sorted_groups = sorted(stats["groups"].items(), key=lambda x: x[1], reverse=True)
lines = []
for g, c in sorted_groups:
    icon = ICONS.get(g, "📺")
    lines.append(f"- {icon} **{g}**: {c} kanal")

lines.append(f"\nGüncelleme: `{stats['updated']}`")
lines.append(f"Toplam Kanal: **{stats['total']}**")

block = "\n".join(lines)

readme = open("README.md", encoding="utf-8").read()
readme = re.sub(
    r"<!-- STATS-START -->(.*?)<!-- STATS-END -->",
    f"<!-- STATS-START -->\n{block}\n<!-- STATS-END -->",
    readme,
    flags=re.S
)

# Playlist latest link
readme = re.sub(
    r"https://cdn\.jsdelivr\.net/gh/.*/playlist\.m3u",
    f"https://cdn.jsdelivr.net/gh/k33n26/iptvturk@latest/playlist.m3u",
    readme
)

open("README.md", "w", encoding="utf-8").write(readme)
