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
            if "," not in line:
                continue
            name, url = line.strip().split(",", 1)
            logo = get_logo(name)

            out.write(
                f'#EXTINF:-1 tvg-name="{name}" '
                f'tvg-logo="{logo}" group-title="{group}",{name}\n'
                f'{url}\n'
            )
