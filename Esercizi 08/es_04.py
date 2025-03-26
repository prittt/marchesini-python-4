from functools import reduce

def filter_scores_01(lst_scores: list[int], lst_names: list[str], thr: int) -> tuple[list[int], list[str]]:
    return (
        [s for s in lst_scores if s > thr],
        [n for s, n in zip(lst_scores, lst_names) if s > thr]
    )

def filter_scores_02(lst_scores: list[int], lst_names: list[str], thr: int) -> tuple[list[int], list[str]]:
    filtered = list(filter(lambda sn: sn[0] > thr, zip(lst_scores, lst_names)))
    # scores = [s for s, _ in filtered]
    # names = [n for _, n in filtered]        

    scores, names = zip(*filtered) if filtered else ([], [])
    return (list(scores), list(names))

def filter_scores_03(lst_scores: list[int], lst_names: list[str], thr: int) -> tuple[list[int], list[str]]:
    return reduce(
        lambda acc, sn: (
            acc[0] + [sn[0]] if sn[0] > thr else acc[0],
            acc[1] + [sn[1]] if sn[0] > thr else acc[1]
        ),
        zip(lst_scores, lst_names),
        ([], [])
    )


def run_tests():
    test_cases = [
        ([10, 20, 30, 40], ["a", "b", "c", "d"], 25, ([30, 40], ["c", "d"])),
        ([5, 15, 25], ["x", "y", "z"], 15, ([25], ["z"])),
        ([1, 2, 3], ["uno", "due", "tre"], 5, ([], [])),
        ([], [], 10, ([], [])),
        ([100, 90, 80, 70], ["a", "b", "c", "d"], 85, ([100, 90], ["a", "b"])),
    ]

    functions = [
        filter_scores_01,
        filter_scores_02,
        filter_scores_03,
    ]

    for func in functions:
        for i, (scores, names, thr, expected) in enumerate(test_cases):
            result = func(scores, names, thr)
            assert result == expected, f"{func.__name__} fallito nel test {i+1}"
    print("✅ Tutti i test superati con successo!")

if __name__ == "__main__":
    run_tests()