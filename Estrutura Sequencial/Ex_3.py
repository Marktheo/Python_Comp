#@author: Marktheo
#Tarefa: Desenvolva um programa que que peça dois números e mostre: "O resultado da soma é: ..."

def soma(x, y):
    return (int(x) + int(y))

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

print("O resultado da soma é " + str(soma(num1, num2)))