def converte(m):
    return (m * 100)

num = float(input("Digite o comprimento em metros: "))

print("\nEm centímetros, o comprimento será de", format(converte(num), ".1f"))