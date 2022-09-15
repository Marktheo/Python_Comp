#@author: Marktheo
#https://wiki.python.org.br/EstruturaDeDecisao

num1 = input("Digite o preço do produto 1: ")
num2 = input("Digite o preço do produto 2: ")
num3 = input("Digite o preço do produto 3: ")

if(float(num1) < float(num2) and float(num1) < float(num3)):
    print("O 1º produto é o mais barato. Portanto, você deve comprá-lo")

elif(float(num2) < float(num1) and float(num2) < float(num3)):
    print("O 2º produto é o mais barato. Portanto, você deve comprá-lo")

elif(float(num3) < float(num1) and float(num3) < float(num2)):
    print("O 3º produto é o mais barato. Portanto, você deve comprá-lo")

else:
    print("Os 3 produtos tem o mesmo preço. Fique a vontade para escolher qualquer um deles")