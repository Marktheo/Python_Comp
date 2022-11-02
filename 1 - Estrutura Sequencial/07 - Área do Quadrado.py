def area(l):
    return (l ** 2)

def dobro(d):
    return d * 2

num = float(input("Digite o lado do quadrado: "))

print("O dobro da área do quadrado é", round(dobro(area(num)), 2), "u.a.")