#@author: Marktheo
#Tarefa: Desenvolva um programa que peça o lado de um quadrado e mostre: "O dobro da área do quadrado é: ..."

def area(l):
    return (float(l) ** 2) * 2

num = input("Digite o lado do quadrado: ")

print("O dobro da área do quadrado é " + str(round(area(num), 2)) + " u.a.")