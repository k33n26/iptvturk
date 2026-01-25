import os
import json
import requests
import urllib.parse

LISTS_DIR = "lists"
CACHE_DIR = "cache"
CACHE_FILE = f"{CACHE_DIR}/logos.json"
OUTPUT = "playlist.m3u"

DEFAULT_LOGO = "https://upload.wikimedia.org/wikipedia/commons/1/1f/IPTV_logo.png"

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

os.makedirs(CACHE_DIR, exist_ok=True)

if os.path.isfile(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        logo_cache = json.load(f)
else:
    logo_cache = {}

def wiki_logo(name):
    try:
        title = urllib.parse.quote(name)
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json().get("thumbnail", {}).get("source")
    except:
        pass
    return None

def clearlogo(name):
    try:
        q = urllib.parse.quote(name)
        url = f"https://thelogodb.com/api/json/v1/1/search.php?s={q}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            channels = r.json().get("channels")
            if channels:
                return channels[0].get("strLogoWide") or channels[0].get("strLogo")
    except:
        pass
    return None

def fanart(name):
    try:
        q = urllib.parse.quote(name)
        url = f"https://theaudiodb.com/api/v1/json/2/search.php?s={q}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            artists = r.json().get("artists")
            if artists:
                return artists[0].get("strArtistThumb")
    except:
        pass
    return None

def get_logo(name):
    if name in logo_cache:
        return logo_cache[name]

    for fn in (wiki_logo, clearlogo, fanart):
        logo = fn(name)
        if logo:
            logo_cache[name] = logo
            return logo

    logo_cache[name] = DEFAULT_LOGO
    return DEFAULT_LOGO

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")

    for file, group in GROUPS.items():
        path = os.path.join(LISTS_DIR, file)
        if not os.path.isfile(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "," not in line:
                    continue

                name, url = line.split(",", 1)
                logo = get_logo(name)

                out.write(
                    f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n'
                )
                out.write(url + "\n")

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(logo_cache, f, indent=2, ensure_ascii=False)
