turno = input("Digite em qual horário você estuda ('M', 'V' ou 'N'): ")

if(turno == 'M' or turno == 'm'):
    print("Bom dia!")

elif(turno == 'V' or turno == 'v'):
    print("Boa Tarde!")

elif(turno == 'N' or turno == 'n'):
    print("Boa Noite!")

else:
    print("Valor Inválido")