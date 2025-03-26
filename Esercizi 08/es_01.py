from functools import reduce

def list_upper_01(lst: list[str]) -> list[str]:
    return [s.upper() for s in lst]

def list_upper_02(lst: list[str]) -> list[str]:
    return list(map(str.upper, lst))

def list_upper_03(lst: list[str]) -> list[str]:
    return reduce(lambda acc, s: acc + [s.upper()], lst, [])

def run_tests():
    test_cases = [
        (["ciao", "mondo"], ["CIAO", "MONDO"]),
        (["Python", "è", "fantastico"], ["PYTHON", "È", "FANTASTICO"]),
        ([], []),
        (["", "a", "B"], ["", "A", "B"])
    ]

    functions = [
        list_upper_01,
        list_upper_02,
        list_upper_03,
    ]

    for func in functions:
        for i, (inp, expected) in enumerate(test_cases):
            result = func(inp)
            assert result == expected, f"{func.__name__} fallito nel test {i+1}"

    print("✅ Tutti i test superati con successo!")

if __name__ == "__main__":
    run_tests()