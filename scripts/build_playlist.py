import os

LISTS = "lists"
OUT = "playlist.m3u"

with open(OUT, "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")

    for file in sorted(os.listdir(LISTS)):
        if not file.endswith(".txt"):
            continue
        group = file.replace(".txt", "").replace("_", " ")
        for line in open(f"{LISTS}/{file}", encoding="utf-8"):
            parts = line.strip().split(",")
            if len(parts) < 2:
                continue
            name, url = parts[0], parts[1]
            out.write(f'#EXTINF:-1 group-title="{group}",{name}\n{url}\n')
