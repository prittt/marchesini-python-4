from functools import reduce

def filter_scores_01(lst: list[int], thr: int) -> list[int]:
    return [x for x in lst if x > thr]

def filter_scores_02(lst: list[int], thr: int) -> list[int]:
    return list(filter(lambda x: x > thr, lst))

def filter_scores_03(lst: list[int], thr: int) -> list[int]:
    return reduce(lambda acc, x: acc + [x] if x > thr else acc, lst, [])

def run_tests():
    test_cases = [
        ([10, 20, 30, 40], 25, [30, 40]),
        ([5, 15, 25], 15, [25]),
        ([1, 2, 3], 5, []),
        ([], 10, []),
        ([100, 90, 80, 70], 85, [100, 90]),
    ]

    functions = [
        filter_scores_01,
        filter_scores_02,
        filter_scores_03,

    ]

    for func in functions:
        for i, (lst, thr, expected) in enumerate(test_cases):
            result = func(lst, thr)
            assert result == expected, f"{func.__name__} fallito nel test {i+1}"
    
    print("✅ Tutti i test superati con successo!")

if __name__ == "__main__":
    run_tests()