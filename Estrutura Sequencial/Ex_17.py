#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

import math

def litros(m):
    return (float(m) / 6)


def latas(m):
    return (litros(m) / 18)


def galoes(m):
    return ((litros(m) - math.floor(latas(m)) * 18) / 3.6)

num = input("Informe a área a ser pintada em metros²: ")

print("Serão necessários", round(litros(num), 2), "litros de tinta")
print("Será(ão) necessária(s)", round(math.floor(latas(num)), 2), "lata(s) de tinta")
print("Será(ão) necessário(s)", round(math.ceil(galoes(num)), 2), "galão(ões) de tinta")
print("O valor total será de R$", round(math.floor(latas(num)) * 80 + (math.ceil(galoes(num)) * 25), 2))