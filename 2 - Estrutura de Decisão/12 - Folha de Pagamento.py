def salario(l, h):
    return (l * h)

num1 = float(input("Digite seu lucro por hora: "))
num2 = float(input("Digite sua carga horária mensal: "))

sal = salario(num1, num2)

if(sal <= 900):
	desc = 0

elif(900 < sal <= 1500):
	desc = 5

elif(1500 < sal <= 2500):
	desc = 10

else: 
	desc = 20

total = (100 - desc - 24)

print("\nSeu salário bruto é R$", round(sal, 2))
print("IR (0 - 20%): R$", round(sal * desc / 100, 2))
print("FGTS (11%): R$", round(sal * 11 / 100, 2))
print("INSS (10%): R$", round(sal * 10 / 100, 2))
print("Sindicato (3%): R$", round(sal * 3 / 100, 2))
print("O total de descontos é R$", round(sal * (100 - total) / 100, 2))
print("Seu salário líquido é R$", round(sal * total / 100, 2))