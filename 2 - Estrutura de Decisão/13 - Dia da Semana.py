semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

num = int(input("Digite o número de um dia da semana: "))

if(1 <= num <= 7):
	print("O dia da semana é:", semana[num-1])

else:
	print("Valor Inválido")
