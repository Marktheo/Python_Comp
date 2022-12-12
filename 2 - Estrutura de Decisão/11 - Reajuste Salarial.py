num = float(input("Informe seu salário: "))

if(num <= 280):
    rate = 120

elif(280 < num <= 700):
    rate = 115

elif(700 < num <= 1500):
    rate = 110

else:
    rate = 105

print("O salário antes do reajuste era R$",num)
print("O percentual de aumento foi de", rate - 100,"porcento")
print("O aumento foi de R$", (rate - 100) / 100 * num)
print("O novo salário é de R$", round(rate / 100 * num))