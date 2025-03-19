a = int(input("Inserire il primo numero:"))
b = int(input("Inserire il secondo numero:"))

# Euclide differenze
# MCD(a, b) = MCD(a - b, b) 
# MCD(9, 3) = MCD(6, 3) = MCD(3, 3) = 3

# 1. Scambio a e b se a < b;
# 2. Calcolo a - b e ripeto 1. con a - b e b;
# 3. Se a = b, ho trovato il MCD.
def MCDv1(a, b):
    while a != 0:
        # 1. 
        if a < b:
            a, b = b, a
        # 2.
        a = a - b

    return b

print(f"L'MCD tra {a} e {b} è {MCDv1(a,b)}")

# Euclide divisioni
# MCD(a, b) = MCD(b, a % b)
# MCD(3, 9) = MCD(9, 3) = MCD(3, 0) = 3
def MCDv2(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print(f"L'MCD tra {a} e {b} è {MCDv2(a,b)}")