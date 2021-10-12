from apps import Path, Snapshot, AchFile, Put, Sentinel

p = Path('C:\Apps\TESTDIR')
drop = Path('C:\Apps\TESTDUMP')

s = Sentinel(p, drop)

comps = s.changes()

for status, files in comps.items():
    print(status)
    for f in files:
        print(f)


# ach = [AchFile(f) for f in s.files]

# for f in s.files:
#     put = Put(f, drop)
#     put.put()

