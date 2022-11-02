def converte(c):
    return ((c * 9 / 5) + 32)

num = float(input("Digite a temperatura em Celsius: "))

print("\nEm Fahrenheit, a temperatura será", round(converte(num), 2), "graus")