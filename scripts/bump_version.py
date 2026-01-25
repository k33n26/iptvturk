v = open("VERSION.txt").read().strip()
major, minor, patch = map(int, v.split("."))

patch += 1
new = f"{major}.{minor}.{patch}"

open("VERSION.txt", "w").write(new)
print(new)
