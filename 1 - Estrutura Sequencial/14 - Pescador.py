def excesso(k):
    return (k - 50)

def multa(k):
    return (excesso(k) * 4)

num = float(input("Informe o peso em kilos: "))

print("\nO excesso foi de", round(excesso(num), 2), "kilos")
print("O valor da multa é de R$", round(multa(num), 2))