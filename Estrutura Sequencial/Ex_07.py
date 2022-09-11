#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def area(l):
    return (float(l) ** 2) * 2

num = input("Digite o lado do quadrado: ")

print("O dobro da área do quadrado é " + str(round(area(num), 2)) + " u.a.")