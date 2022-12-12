def media(a, b):
    return ((float(a) + float(b)) / 2)

num1 = input("Digite a nota do 1º semestre: ")
num2 = input("Digite a nota do 2º semestre: ")

if(media(num1, num2) == 10):
    print("Aprovado com Distinção")

elif(media(num1, num2) >= 7):
    print("Aprovado")

else:
    print("Reprovado")