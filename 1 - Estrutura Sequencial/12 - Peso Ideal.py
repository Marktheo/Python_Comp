def peso(h):
    return ((72.7 * h) - 58)

num = float(input("Informe sua altura em metros: "))

print("\nSeu peso ideal é", round(peso(num), 2), "Kg")