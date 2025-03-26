from functools import reduce

def filter_palindromes_01(lst: list[str]) -> list[str]:
    return [s for s in lst if s == s[::-1]]

def filter_palindromes_02(lst: list[str]) -> list[str]:
    return list(filter(lambda s: s == s[::-1], lst))

def filter_palindromes_03(lst: list[str]) -> list[str]:
    return reduce(lambda acc, s: acc + [s] if s == s[::-1] else acc, lst, [])


def run_tests():
    test_cases = [
        (["anna", "casa", "otto", "radar"], ["anna", "otto", "radar"]),
        (["pal", "pip", "xyzzyx", "abc"], ["pip", "xyzzyx"]),
        (["", "a", "aa", "aba", "abc"], ["", "a", "aa", "aba"]),
        ([], []),
        (["python", "java"], []),
    ]

    functions = [
        filter_palindromes_01,
        filter_palindromes_02,
        filter_palindromes_03,
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