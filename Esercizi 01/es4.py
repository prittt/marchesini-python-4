n = int(input("Inserire un numero:"))

# i = 2
# while i < n:
#     if n % i == 0:
#         print(f"{n} non è primo")
#         break
#     i += 1
# else:
#     print(f"{n} è un numero primo")
# 

#for(int i = 2; i < n; ++i)
# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} non è primo")
#         break
# else:
#     print(f"{n} è un numero primo")    

# for i in range(n - 1, 1, -1)

def is_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            
    return True    

status = "primo" if is_primo(n) else "non primo"
status = (is_primo(n) and "primo") or "non primo"
print(f"Il numero {n} è {status}")