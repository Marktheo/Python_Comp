def tempo(t, v):
    return (t * 8 / v / 60)


num1 = float(input("Informe o tamanho em MB do arquivo: "))
num2 = float(input("Informe a velocidade em Mbps da internet: "))

print("\nO tempo de download será de", round(tempo(num1, num2), 2), "minutos")