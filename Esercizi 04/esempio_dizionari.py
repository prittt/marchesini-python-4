prodotti = [
    {"nome": "Laptop", "prezzo": 1000, "categoria": "elettronica"},
    {"nome": "Mouse", "prezzo": 50, "categoria": "elettronica"},
    {"nome": "Sedia", "prezzo": 150, "categoria": "arredamento"},
    {"nome": "Lampada", "prezzo": 80, "categoria": "arredamento"},
    {"nome": "Monitor", "prezzo": 300, "categoria": "elettronica"}
]

def applica_sconto(prodotto, percentuale):
    nuovo = prodotto.copy()
    nuovo["prezzo"] *= (1 - percentuale)
    return nuovo

from functools import partial, reduce

# Sconto del 10%
sconto_10 = partial(applica_sconto, percentuale=0.10)
prodotti_scontati = list(map(sconto_10, prodotti))

# Solo elettronica
elettronica = list(filter(lambda p: p["categoria"] == "elettronica", prodotti_scontati))

# Ordinati per prezzo
ordinati = sorted(elettronica, key=lambda p: p["prezzo"])

# Totale spesa
totale = reduce(lambda acc, p: acc + p["prezzo"], ordinati, 0)

print(f"Totale spesa per prodotti elettronici scontati: {totale:.2f}€")
