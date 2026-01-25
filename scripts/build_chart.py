import os, json, matplotlib.pyplot as plt

os.makedirs("stats/charts", exist_ok=True)

s = json.load(open("stats/stats.json", encoding="utf-8"))

# Tüm gruplar için mini grafik
for group, count in s["groups"].items():
    plt.figure(figsize=(4,2))
    plt.barh([group],[count], color="skyblue")
    plt.title(group)
    plt.tight_layout()
    plt.savefig(f"stats/charts/{group}.png", dpi=100)
    plt.close()

# Tüm kanal dağılım grafiği
plt.figure(figsize=(10,6))
plt.barh(list(s["groups"].keys()), list(s["groups"].values()), color="skyblue")
plt.title("IPTV Kanal Dağılımı")
plt.xlabel("Kanal Sayısı")
plt.tight_layout()
plt.savefig("stats/chart.png", dpi=150)
plt.close()
