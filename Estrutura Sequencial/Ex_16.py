#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

import math

def litros(m):
    return (float(m) / 3)


def latas(m):
    return (math.ceil(litros(m) / 18))

num = input("Informe a área a ser pintada em metros²: ")

print("Serão necessários " + str(round(litros(num), 2)) + " litros de tinta")
print("Será(ão) necessária(s) " + str(round(latas(num), 2)) + " lata(s) de tinta")
print("O valor total será de R$" + str(round(latas(num) * 80, 2)))