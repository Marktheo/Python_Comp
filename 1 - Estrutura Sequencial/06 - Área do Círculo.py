import math

def area(r):
    return ((r ** 2) * math.pi)

num = float(input("Digite o raio do círculo: "))

print("A área do círculo é", round(area(num), 2), "u.a.")