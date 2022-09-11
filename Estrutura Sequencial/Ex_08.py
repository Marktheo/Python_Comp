#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def salario(l, h):
    return (float(l) * float(h))

num1 = input("Digite seu lucro por hora: ")
num2 = input("Digite sua carga horária mensal: ")

print("Seu salário é R$" + str(round(salario(num1, num2), 2)))