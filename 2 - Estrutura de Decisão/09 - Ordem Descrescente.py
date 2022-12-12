num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if(num1 > num2 and num1 > num3):

    if(num2 > num3):
        print("Ordem:", num1, ",", num2, ",", num3)

    else:
        print("Ordem:", num1, ",", num3, ",", num2)

elif(num2 > num1 and num2 > num3):

    if(num1 > num3):
        print("Ordem:", num2, ",", num1, ",", num3)

    else:
        print("Ordem:", num2, ",", num3, ",", num1)

elif(num3 > num1 and num3 > num2):

    if(num2 > num1):
        print("Ordem:", num3, ",", num2, ",", num1)

    else:
        print("Ordem:", num3, ",", num1, ",", num2)

else:
    print("Os 3 números são iguais")