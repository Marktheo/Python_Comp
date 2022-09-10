#@author: Marktheo
#Tarefa: Desenvolva um programa que peça 4 notas bimestrais e mostre: "A média final é: ..."

def media(a, b, c, d):
    return (float(a) + float(b) + float(c) + float(d))/4

num1 = input("Digite a 1ª média: ")
num2 = input("Digite a 2ª média: ")
num3 = input("Digite a 3ª média: ")
num4 = input("Digite a 4ª média: ")

print("A média final é " + str(media(num1, num2, num3, num4)))