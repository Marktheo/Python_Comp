#@author: Marktheo
#Tarefa: Desenvolva um programa que converta de metros para centímetros

def converte(m):
    return (float(m) * 100)

num = input("Digite o comprimento em metros: ")

print("Em centímetros, o comprimento será de " + str(converte(num)))