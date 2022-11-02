import math

def litros(m):
    return (m / 3)


def latas(m):
    return (math.ceil(litros(m) / 18))

num = float(input("Informe a área a ser pintada em metros²: "))

print("\nSerão necessários", round(litros(num), 2), "litros de tinta")
print("Será(ão) necessária(s)", round(latas(num), 2), "lata(s) de tinta")
print("O valor total será de R$", round(latas(num) * 80, 2))