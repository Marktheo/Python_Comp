#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def salario(l, h):
    return (float(l) * float(h))

num1 = input("Digite seu lucro por hora: ")
num2 = input("Digite sua carga horária mensal: ")

print("Seu salário bruto é R$", round(salario(num1, num2), 2))
print("IR (11%): R$", round(salario(num1, num2) * 11 / 100, 2))
print("INSS (8%): R$", round(salario(num1, num2) * 8 / 100, 2))
print("Sindicato (5%): R$", round(salario(num1, num2) * 5 / 100, 2))
print("Seu salário líquido é R$", round(salario(num1, num2) * 76 / 100, 2))