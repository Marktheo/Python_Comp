#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def peso(h):
    return (72.7 * float(h) - 58)

num = input("Informe sua altura em metros: ")

print("Seu peso ideal é", round(peso(num), 2), "Kg")