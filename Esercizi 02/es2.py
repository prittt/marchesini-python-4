def reverse_v1(l: list):
    ret = l[::-1]
    return ret
    # return l[::-1]

def reverse_v2(l: list):
    ret = l.copy() # ret = l[:] or ret = list(l)
    ret.reverse()
    return ret

def reverse_v3(l: list):
    ret = []
    for i in range(len(l) - 1, -1, -1):
        ret.append(l[i])
    return ret

def reverse_v4(l: list):
    ret = []
    for e in reversed(l):
        ret.append(e)
    return ret

def reverse_v5(l: list):
    return list(reversed(l))

l = [1, 2, 3, 4, 5, 6]
ret = reverse_v1(l)
print(l)
print(ret)

l = [1, 2, 3, 4, 5, 6]
ret = reverse_v3(l)
print(l)
print(ret)

l = [1, 2, 3, 4, 5, 6]
ret = reverse_v4(l)
print(l)
print(ret)

l = [1, 2, 3, 4, 5, 6]
ret = reverse_v2(l)
print(l)
print(ret)