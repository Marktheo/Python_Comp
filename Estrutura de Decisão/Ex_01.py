#@author: Marktheo
#https://wiki.python.org.br/EstruturaDeDecisao

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if(float(num1) > float(num2)):
    print("O 1º número é o maior")

elif(float(num1) < float(num2)):
    print("O 2º número é o maior")

else:
    print("Os 2 números são iguais")