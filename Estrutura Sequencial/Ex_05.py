#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def converte(m):
    return (float(m) * 100)

num = input("Digite o comprimento em metros: ")

print("Em centímetros, o comprimento será de " + str(converte(num)))