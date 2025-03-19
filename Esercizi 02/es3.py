def potenze(base:int, maxexp:int) ->list:
    return [base**i for i in range(1, maxexp + 1)]

l = potenze(2, 10)
print(l)