from apps import Path, Snapshot, AchFile

p = Path('.')
s = Snapshot(p)

print(p.path())


# ach = [AchFile(f) for f in s.files]

for f in s.files:
    print(f)