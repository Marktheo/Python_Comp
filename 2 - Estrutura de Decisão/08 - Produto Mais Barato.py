num1 = float(input("Digite o preço do produto 1: "))
num2 = float(input("Digite o preço do produto 2: "))
num3 = float(input("Digite o preço do produto 3: "))

if(num1 < num2 and num1 < num3):
    print("O 1º produto é o mais barato. Portanto, você deve comprá-lo")

elif(num2 < num1 and num2 < num3):
    print("O 2º produto é o mais barato. Portanto, você deve comprá-lo")

elif(num3 < num1 and num3 < num2):
    print("O 3º produto é o mais barato. Portanto, você deve comprá-lo")

else:
    print("Os 3 produtos tem o mesmo preço. Fique a vontade para escolher qualquer um deles")