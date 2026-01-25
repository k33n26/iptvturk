import os
import json
from datetime import datetime

LISTS_DIR = "lists"
OUTPUT_JSON = "stats/stats.json"

os.makedirs("stats", exist_ok=True)

stats = {
    "total_channels": 0,
    "groups": {},
    "last_update": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
}

def filename_to_group(name):
    name = name.replace(".txt", "")
    name = name.replace("_", " ")
    return name.upper()

for file in sorted(os.listdir(LISTS_DIR)):
    if not file.endswith(".txt"):
        continue

    path = os.path.join(LISTS_DIR, file)
    group_name = filename_to_group(file)
    count = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and "," in line:
                count += 1

    stats["groups"][group_name] = count
    stats["total_channels"] += count

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)
