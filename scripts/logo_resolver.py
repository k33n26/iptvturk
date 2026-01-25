import json, os, requests, urllib.parse

CACHE_FILE = "cache/logos.json"
os.makedirs("cache", exist_ok=True)

if os.path.exists(CACHE_FILE):
    cache = json.load(open(CACHE_FILE, encoding="utf-8"))
else:
    cache = {}

def save():
    json.dump(cache, open(CACHE_FILE, "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)

def wiki_logo(channel):
    try:
        q = channel.replace(" ", "_")
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{q}"
        r = requests.get(url, timeout=10).json()
        if "thumbnail" in r:
            return r["thumbnail"]["source"]
    except:
        pass
    return None

def clearlogo(channel):
    q = urllib.parse.quote(channel)
    return f"https://www.thelogodb.com/images/media/logo/{q}.png"

def fallback(channel):
    q = urllib.parse.quote(channel)
    return f"https://www.google.com/s2/favicons?sz=256&domain_url={q}"

def get_logo(channel):
    if channel in cache:
        return cache[channel]

    logo = wiki_logo(channel)
    if not logo:
        logo = clearlogo(channel)

    cache[channel] = logo or fallback(channel)
    save()
    return cache[channel]
