import os
from logo_resolver import get_logo

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
            country, kind = parts[2] if len(parts) > 2 else "", parts[3] if len(parts) > 3 else ""
            logo = get_logo(name)
            out.write(
                f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}" country="{country}" type="{kind}",{name}\n{url}\n'
            )
