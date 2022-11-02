def converte(f):
    return (5 * (f - 32) / 9)

num = float(input("Digite a temperatura em Fahrenheit: "))

print("Em Celsius, a temperatura será de", round(converte(num), 2))