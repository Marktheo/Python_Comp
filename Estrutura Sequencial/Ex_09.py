#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def converte(f):
    return (5 * ((float(f) - 32) / 9))

num = input("Digite a temperatura em Fahrenheit: ")

print("Em Celsius, a temperatura será de", round(converte(num), 2))