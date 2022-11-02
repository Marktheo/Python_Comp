#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def ops(x, y, z, op):

    if(op == 1):
        return (int(x) * int(y))

    elif(op == 2):
        return ((3 * int(x)) + float(z))

    elif(op == 3):
        return (float(z) ** 3)

    else:
        return "Operação não encontrada"


num1 = input("Digite um número inteiro: ")
num2 = input("Digite outro número inteiro: ")
num3 = input("Digite um número real: ")

print("O resultado 1 é", round(ops(num1, num2, num3, 1), 2))
print("O resultado 2 é", round(ops(num1, num2, num3, 2), 2))
print("O resultado 3 é", round(ops(num1, num2, num3, 3), 2))