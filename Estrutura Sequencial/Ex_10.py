#@author: Marktheo
#Tarefa: Desenvolva um programa que converta de Celsius para Fahrenheit

def converte(c):
    return ((float(c) * 9 / 5) + 32)

num = input("Digite a temperatura em Celsius: ")

print("Em Fahrenheit, a temperatura será de " + str(round(converte(num), 2)))