def dict_invert(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        new_d[v] = k

    return new_d

if __name__ == "__main__":
    d = {
        'Theodore': 10,
        'Mathew': 11,
        'Roxanne': 9,
    }
    reversed_d = dict_invert(d)
    print(d, reversed_d)