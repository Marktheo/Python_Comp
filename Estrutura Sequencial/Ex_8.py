#@author: Marktheo
#Tarefa: Desenvolva um programa que peça seu lucro por hora, a carga horária mensal e mostre: "Seu salário é: ..."

def salario(l, h):
    return (float(l) * float(h))

num1 = input("Digite seu lucro por hora: ")
num2 = input("Digite sua carga horária mensal: ")

print("Seu salário é R$ " + str(round(salario(num1, num2), 2)))