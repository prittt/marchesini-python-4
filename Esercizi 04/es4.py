def occorrenze_v1(sequenza):
    cnt = {}
    for e in sequenza:
        if e in cnt:
            cnt[e] += 1
        else:
            cnt[e] = 1
    return cnt

def occorrenze_v2(sequenza):
    cnt = {}
    for e in sequenza:
        cnt[e] = cnt.get(e, 0) + 1

    return cnt

from collections import Counter
def occorrenze_v3(sequenza):
    return dict(Counter(sequenza))

def occorrenze_v4(sequenza):
    return {e: list(sequenza).count(e) for e in set(sequenza)}

print(occorrenze_v1("banana"))       
print(occorrenze_v1([1, 2, 2, 3, 3]))
print(occorrenze_v2("banana"))       
print(occorrenze_v2([1, 2, 2, 3, 3]))
print(occorrenze_v3("banana"))       
print(occorrenze_v3([1, 2, 2, 3, 3]))
print(occorrenze_v4("banana"))       
print(occorrenze_v4([1, 2, 2, 3, 3]))

