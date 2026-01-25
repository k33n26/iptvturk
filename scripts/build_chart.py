import json, matplotlib.pyplot as plt

s = json.load(open("stats/stats.json", encoding="utf-8"))

plt.figure(figsize=(10,6))
plt.barh(list(s["groups"].keys()), list(s["groups"].values()))
plt.title("IPTV Kanal Dağılımı")
plt.xlabel("Kanal Sayısı")
plt.tight_layout()
plt.savefig("stats/chart.png", dpi=150)
plt.close()
