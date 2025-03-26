from functools import reduce

# ------------------------------
# Versioni della funzione sum
# ------------------------------

def sum_01(lst: list[int]) -> int:
    return sum(lst)

def sum_02(lst: list[int]) -> int:
    return reduce(lambda acc, x: acc + x, lst, 0)

def sum_03(lst: list[int]) -> int:
    return sum(map(int, lst))

def run_tests():
    test_cases = [
        ([1, 2, 3], 6),
        ([0, 0, 0], 0),
        ([], 0),
        ([10, -5, 7], 12),
        ([-1, -2, -3], -6),
    ]

    functions = [
        sum_01,
        sum_02,
        sum_03,
    ]

    for func in functions:
        for i, (inp, expected) in enumerate(test_cases):
            result = func(inp)
            assert result == expected, (
                f"❌ Errore in {func.__name__} al test {i+1}:\n"
                f"  input: {inp}\n"
                f"  atteso: {expected}\n"
                f"  ottenuto: {result}"
            )
            print(f"✅ {func.__name__} test {i+1} passato")

if __name__ == "__main__":
    run_tests()
