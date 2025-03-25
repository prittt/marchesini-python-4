

d = {"a": 1, "b": 2}

for k in d.keys():
    print(d[k])

for v in d.values():
    print(v)

for item in d.items():
    # print(k, v)
    k = item[0]
    v = item[1]

for k, v in d.items():
    print(k, v)
    