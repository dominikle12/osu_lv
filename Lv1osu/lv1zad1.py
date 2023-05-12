def total_euro(hours, rate):
    total = hours * rate
    return total

hours = float(input("Unesite broj radnih sati: "))
rate = float(input("Unesite cijenu po satu: "))

total = total_euro(hours, rate)

print("Ukupna zarada: ", total, " eura !")