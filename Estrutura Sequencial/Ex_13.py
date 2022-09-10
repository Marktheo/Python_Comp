#@author: Marktheo
#Tarefa: Desenvolva um programa que peça a altura do usuário e mostre: "Seu peso ideal é: ..."

def peso(h, s):

    if(s == 'm'):
        return (72.7 * float(h) - 58)

    else:
        return (62.1 * float(h) - 44.7)
    

num = input("Informe sua altura em metros: ")
sex = input("Informe seu sexo ('m' ou 'f'): ")

print("Seu peso ideal é " + str(round(peso(num, sex), 2)) + " Kg")