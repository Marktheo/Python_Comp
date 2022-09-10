#@author: Marktheo
#Tarefa: Desenvolva um programa que peça o raio de um círculo e mostre: "A área do círculo é: ..."

import math

def area(r):
    return ((float(r) ** 2) * math.pi)

num = input("Digite o raio do círculo: ")

print("A área do círculo é " + str(round(area(num), 2)) + " u.a.")