#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def excesso(k):
    return (float(k) - 50)


def multa(k):
    return (excesso(k) * 4)


num = input("Informe o peso em kilos: ")

print("O excesso em kilos foi de " + str(round(excesso(num), 2)))
print("O valor da multa é de R$" + str(round(multa(num), 2)))