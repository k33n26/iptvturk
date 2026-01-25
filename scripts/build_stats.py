import os
import json
from datetime import datetime

LISTS_DIR = "lists"
OUTPUT_JSON = "stats/stats.json"

GROUPS = {
    "ulusal.txt": "ULUSAL TV",
    "belgesel.txt": "BELGESEL TV",
    "haber.txt": "HABER TV",
    "yerel.txt": "YEREL TV",
    "spor.txt": "SPOR TV",
    "yasam.txt": "YASAM TV",
    "sinema_dizi.txt": "SINEMA-DIZI TV",
    "muzik.txt": "MUZIK TV",
    "avrupa.txt": "AVRUPA TV"
}

os.makedirs("stats", exist_ok=True)

stats = {
    "total_channels": 0,
    "groups": {},
    "last_update": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
}

for file, group in GROUPS.items():
    path = os.path.join(LISTS_DIR, file)
    count = 0

    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "," in line:
                    count += 1

    stats["groups"][group] = count
    stats["total_channels"] += count

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)
