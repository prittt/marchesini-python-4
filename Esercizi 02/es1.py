import statistics

def media_v1(l : list) -> float:
    sum = 0
    for e in l:
        sum += e
    return sum / len(l)

def media_v2(l : list) -> float:
    return sum(l) / len(l)

def media_v3(l : list) -> float:
    return statistics.mean(l)

l = [1, 2, 3, 4, 5, 6]
print(media_v1(l))
print(media_v2(l))
print(media_v3(l))
pass
