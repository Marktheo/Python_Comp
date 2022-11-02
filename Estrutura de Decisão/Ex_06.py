#@author: Marktheo
#https://wiki.python.org.br/EstruturaDeDecisao

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
num3 = input("Digite outro número: ")

if(float(num1) > float(num2) and float(num1) > float(num3)):
    print("O 1º número é o maior")

elif(float(num2) > float(num1) and float(num2) > float(num3)):
    print("O 2º número é o maior")

elif(float(num3) > float(num1) and float(num3) > float(num2)):
    print("O 3º número é o maior")

else:
    print("Os 3 números são iguais")