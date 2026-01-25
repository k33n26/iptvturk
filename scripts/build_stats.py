import os, json
from datetime import datetime
from zoneinfo import ZoneInfo

LISTS = "lists"
os.makedirs("stats", exist_ok=True)

tz = ZoneInfo("Europe/Istanbul")
now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S (TR)")

stats = {"total": 0, "groups": {}, "diff": {}, "updated": now, "channels": []}

prev = {}
if os.path.exists("stats/prev.json"):
    prev = json.load(open("stats/prev.json")).get("groups", {})

for f in os.listdir(LISTS):
    if not f.endswith(".txt"):
        continue
    group = f.replace(".txt", "").replace("_", " ")
    lines = [l.strip() for l in open(f"{LISTS}/{f}", encoding="utf-8") if "," in l]
    stats["groups"][group] = len(lines)
    stats["diff"][group] = len(lines) - prev.get(group, 0)
    stats["total"] += len(lines)
    for l in lines:
        parts = l.split(",")
        stats["channels"].append({
            "name": parts[0],
            "url": parts[1],
            "country": parts[2] if len(parts)>2 else "",
            "type": parts[3] if len(parts)>3 else "",
            "group": group
        })

json.dump(stats, open("stats/stats.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
json.dump(stats, open("stats/prev.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
