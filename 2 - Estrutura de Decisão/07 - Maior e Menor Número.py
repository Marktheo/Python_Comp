num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if(num1 > num2 and num1 > num3):
    print("O 1º número é o maior")

elif(num2 > num1 and num2 > num3):
    print("O 2º número é o maior")

elif(num3 > num1 and num3 > num2):
    print("O 3º número é o maior")

else:
    print("Os 3 números são iguais")

if(num1 < num2 and num1 < num3):
    print("O 1º número é o menor")

elif(num2 < num1 and num2 < num3):
    print("O 2º número é o menor")

elif(num3 < num1 and num3 < num2):
    print("O 3º número é o menor")

else:
    print("Os 3 números são iguais")