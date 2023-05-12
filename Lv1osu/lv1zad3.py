
lista = []
while True:
    y=input("Unesite broj: ")
    if y == "Done":
        break
    try:
        broj = float(y)
        lista.append(broj)
    except ValueError:
        print("Neispravan unos broja!!")
count = len(lista)
sredina = sum(lista)/count
maks = max(lista)
minimal = min(lista)
lista.sort()
print("Uneseno je: ", count, "brojeva, aritmeticka sredina je: ", sredina, ", najveci broj je: ", maks, ", najmanji broj je: ", minimal, "\nSortirana lista je: ", lista)