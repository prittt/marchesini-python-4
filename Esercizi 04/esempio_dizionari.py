d = {"a": 1, "b": 2, "c": 3}
print(d)

d["d"] = 4
print(d["d"])
print(d)

# l = list(d.keys())
# print(l[0])
for k in d.keys():
    print(d[k])

for k in d:
    print(d[k])