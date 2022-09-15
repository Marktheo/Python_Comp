#@author: Marktheo
#https://wiki.python.org.br/EstruturaDeDecisao

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
num3 = input("Digite outro número: ")

if(float(num1) > float(num2) and float(num1) > float(num3)):

    if(float(num2) > float(num3)):
        print("Ordem:", num1, ",", num2, ",", num3)
    else:
        print("Ordem:", num1, ",", num3, ",", num2)

elif(float(num2) > float(num1) and float(num2) > float(num3)):

    if(float(num1) > float(num3)):
        print("Ordem:", num2, ",", num1, ",", num3)
    else:
        print("Ordem:", num2, ",", num3, ",", num1)

elif(float(num3) > float(num1) and float(num3) > float(num2)):

    if(float(num2) > float(num1)):
        print("Ordem:", num3, ",", num2, ",", num1)
    else:
        print("Ordem:", num3, ",", num1, ",", num2)

else:
    print("Os 3 números são iguais")