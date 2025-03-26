from functools import reduce

def list_round_01(lst: list[float]) -> list[float]:
    return [round(x, i) for i, x in enumerate(lst)]

def list_round_02(lst: list[float]) -> list[float]:
    return list(map(lambda t: round(t[1], t[0]), enumerate(lst)))

def list_round_03(lst: list[float]) -> list[float]:
    return reduce(lambda acc, t: acc + [round(t[1], t[0])], enumerate(lst), [])

def run_tests():
    test_cases = [
        ([1.2345, 2.3456, 3.4567, 4.5678], [1.0, 2.3, 3.46, 4.568]),
        ([0.9999, 0.1234], [1.0, 0.1]),
        ([], []),
        ([5.678], [6.0]),
        ([1.1111, 2.2222, 3.3333], [1.0, 2.2, 3.33]),
    ]

    functions = [
        list_round_01,
        list_round_02,
        list_round_03,
    ]

    for func in functions:
        for i, (inp, expected) in enumerate(test_cases):
            result = func(inp)
            assert result == expected, f"{func.__name__} fallito nel test {i+1}"
    
    print("✅ Tutti i test superati con successo!")

if __name__ == "__main__":
    run_tests()