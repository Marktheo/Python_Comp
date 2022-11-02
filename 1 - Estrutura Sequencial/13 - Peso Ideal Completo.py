def peso(h, s):

    if(s == 'm'):
        return ((72.7 * h) - 58)

    elif(s == 'f'):
        return ((62.1 * h) - 44.7)

    else:
        return 0

num = float(input("Informe sua altura em metros: "))
sex = input("Informe seu sexo ('m' ou 'f'): ")

print("Seu peso ideal é", round(peso(num, sex), 2), "Kg")