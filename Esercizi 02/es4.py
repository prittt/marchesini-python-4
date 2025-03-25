def nodup_v1(l: list):
    ret = []
    for e in l:
        if e not in ret:
            ret.append(e)
    return ret


def nodup_v2(l: list):
    s = set(l)
    ret = list(s)
    return ret
    #return list(set(l))


def nodup_v3(l: list):
    ret = []
    for e in l:
        if ret.count(e) == 0:
            ret.append(e)
    return ret


def nodup_v4(l: list):
    l = sorted(l)
    ret = [l[0]] # Sbagliata
    ret = l[0:1]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            ret.append(l[i])
    return ret


def nodup_v5(l: list):
    d = {}
    for e in l:
        d[e] = None
    return list(d.keys())


def nodup_v6(l: list):
    return list(dict.fromkeys(l))


# import random
# l = [random.randint(0, 100) for _ in range(1000)]
# l_nodup = list(set(l))    
# l_sorted = sorted(l)


l = [4, 1, 1, 4, 7, 9, 7]
print(nodup_v1(l))
print(nodup_v2(l))
print(nodup_v3(l))
print(nodup_v4(l))
print(nodup_v5(l))
print(nodup_v6(l))
