#@author: Marktheo
#https://wiki.python.org.br/EstruturaSequencial

def tempo(t, v):
    return (float(t) * 8 / float(v) / 60)


num1 = input("Informe o tamanho em MB do arquivo: ")
num2 = input("Informe a velocidade em Mbps da internet: ")

print("O tempo de download será de " + str(round(tempo(num1, num2), 2)) + " minutos")