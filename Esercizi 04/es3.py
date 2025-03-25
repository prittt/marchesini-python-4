def generate_dict_v1(d, func):
    return {k: func(v) for k, v in d.items()}

def generate_dict_v2(d, func):
    new_d = {}
    for k, v in d.items():
        new_d[k] = func(v)
    return new_d

def generate_dict_v3(d, func):
    # print(map(func, d.values()))

    return dict(zip(d.keys(), list(map(func, d.values()))))

if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    def func(x):
        return x ** 2
    print(generate_dict_v1(d, func))
    print(generate_dict_v1(d, func))
    print(generate_dict_v3(d, func))

