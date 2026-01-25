import os, json
from datetime import datetime
from zoneinfo import ZoneInfo

LISTS = "lists"
os.makedirs("stats", exist_ok=True)

tz = ZoneInfo("Europe/Istanbul")
now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S (TR)")

stats = {"total": 0, "groups": {}, "updated": now}

prev = {}
if os.path.exists("stats/prev.json"):
    prev = json.load(open("stats/prev.json"))

for f in os.listdir(LISTS):
    if not f.endswith(".txt"):
        continue
    group = f.replace(".txt", "").replace("_", " ")
    count = sum(1 for l in open(f"{LISTS}/{f}", encoding="utf-8") if "," in l)
    stats["groups"][group] = count
    stats["total"] += count

json.dump(stats, open("stats/stats.json", "w", encoding="utf-8"), indent=2)
json.dump(stats, open("stats/prev.json", "w", encoding="utf-8"), indent=2)
