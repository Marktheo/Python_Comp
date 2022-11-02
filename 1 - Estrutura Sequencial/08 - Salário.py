def salario(l, h):
    return (l * h)

num1 = float(input("Digite o lucro por hora: "))
num2 = float(input("Digite a carga horária mensal: "))

print("O salário é R$", round(salario(num1, num2), 2))