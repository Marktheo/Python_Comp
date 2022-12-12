def media(a, b):
    return ((float(a) + float(b)) / 2)

num1 = input("Digite a nota do 1º semestre: ")
num2 = input("Digite a nota do 2º semestre: ")

med = media(num1, num2)

if(med <= 4):
    print("Conteito: E")

if(4 < med <= 6):
    print("Conteito: D")

elif(6 < med <= 7.5):
    print("Conteito: C")

elif(7.5 < med <= 9):
    print("Conteito: B")

else:
    print("Conteito: A")