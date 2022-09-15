#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

import math

def area(r):
    return ((float(r) ** 2) * math.pi)

num = input("Digite o raio do círculo: ")

print("A área do círculo é", round(area(num), 2), "u.a.")