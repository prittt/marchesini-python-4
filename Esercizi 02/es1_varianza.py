import statistics

def media_v2(l : list) -> float:
    return sum(l) / len(l)

def varianza_v1(l: list):
    media = media_v2(l)
    acc = 0
    for e in l:
        acc += (e - media) ** 2
    return acc / len(l)

def varianza_v2(l: list):
    media = sum(l) / len(l)
    elems = [(e - media) ** 2 for e in l]
    return sum(elems) / len(l)

def varianza_v3(l: list):
    return statistics.pvariance(l)

l = [1, 2, 3, 4, 5, 6]
print(varianza_v1(l))
print(varianza_v2(l))
print(varianza_v3(l))