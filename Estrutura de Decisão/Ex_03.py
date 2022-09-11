#@author: Marktheo
#https://wiki.python.org.br/EstruturaDeDecisao

num = input("Digite a letra correspondente ao seu sexo: ")

if(num == 'M' or num == 'm'):
    print("Masculino")

elif(num == 'F' or num == 'f'):
    print("Feminino")

else:
    print("Sexo inválido")