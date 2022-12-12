def ops(x, y, z, op):

    if(op == 1):
        return (x * y)

    elif(op == 2):
        return ((3 * x) + z)

    elif(op == 3):
        return (z ** 3)

    else:
        return "Operação não encontrada"


num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

print("\nO resultado 1 é", round(ops(num1, num2, num3, 1), 2))
print("O resultado 2 é", round(ops(num1, num2, num3, 2), 2))
print("O resultado 3 é", round(ops(num1, num2, num3, 3), 2))