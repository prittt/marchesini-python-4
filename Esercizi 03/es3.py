def conta_parole_v1(s: str) -> int:
    return len(s.split())


def conta_parole_v2(s: str) -> int:
    count = 0
    in_word = False
    for char in s:
        if char != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count


print(conta_parole_v1("  Questa e' una stringa lunga 45 caratteri.  "))
print(conta_parole_v1("1 2 3 a b c"))
print(conta_parole_v1("! @?$ ciao,prova"))

print(conta_parole_v2("  Questa e' una stringa lunga 45 caratteri.  "))
print(conta_parole_v2("1 2 3 a b c"))
print(conta_parole_v2("! @?$ ciao,prova"))
