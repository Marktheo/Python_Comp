#@author: Marktheo
#Tarefa: Desenvolva um programa que peça a altura do usuário e mostre: "Seu peso ideal é: ..."

def peso(h):
    return (72.7 * float(h) - 58)

num = input("Informe sua altura em metros: ")

print("Seu peso ideal é " + str(round(peso(num), 2)) + " Kg")