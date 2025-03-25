def translate_v1(s: str, from_lst: str, to_lst: str) -> str:
    if len(from_lst) != len(to_lst):
        return s

    for i in range(len(from_lst)):
        s = s.replace(from_lst[i], to_lst[i])

    for f, t in zip(from_lst, to_lst):
        s = s.replace(f, t)

    # for i, c in enumerate(from_lst):
    #     s = s.replace(c, to_lst[i])
    
    return s


def translate_v2(s: str, from_lst: str, to_lst: str) -> str:
    if len(from_lst) != len(to_lst):
        return s  
    
    translation_table = str.maketrans(from_lst, to_lst)
    return s.translate(translation_table)

print(translate_v1("ciao", "abdc", "wxzy"))
print(translate_v2("ciao", "abdc", "wxzy"))
