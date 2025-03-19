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
     

l = [4, 1, 1, 4, 7, 9, 7]
print(nodup_v1(l))
print(nodup_v2(l))
print(nodup_v3(l))
print(nodup_v4(l))

