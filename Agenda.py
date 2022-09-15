#Programa desenvolvido para ser uma agenda pessoal
#Deve conter nome dos contatos, assim como e-mail e telefone
 

#Cria o Dicionário [Agenda]
agenda = {}


#Escolher Opção
def action():
    #Prints
    print("\n\nAções da agenda:")
    print("[A] - Adicionar")
    print("[B] - Busca")
    print("[E] - Excluir")
    print("[G] - Guardar")
    print("[S] - Sair")

    #Scanea o Teclado
    opt = input("Escolha sua opção: ")

    #Retorna a opção
    return opt


#Adicionar Contato
def add():
    #Scanea o Teclado
    name = input("\n\nDigite o nome do contato: ")
    email = input("Digite o e-mail do contato: ")
    phone = input("Digite o telefone do contato: ")

    #Adiciona o Contato
    contact = {name: [email,phone]}
    agenda.update(contact)


#Excluir Contato
def delete():
    #Scanea o Teclado
    name = input("\n\nDigite o nome do contato: ")

    #Exclui o Contato
    del agenda[name]


#Buscar Contato
def search():
    #Scanea o Teclado
    name = input("\n\nDigite o nome do contato: ")

    #Busca o Contato
    print("\n", agenda[name])


#Início do Programa
while(True):
    
    #Escolhe a ação
    opt = action()
    
    #Verifica a opção escolhida
    if(opt == 'A' or opt == 'a'):
        add()
    elif(opt == 'B' or opt == 'b'):
        search()
    elif(opt == 'E' or opt == 'e'):
        delete()
    elif(opt == 'G' or opt == 'g'):
        print("Contatos salvos")
        #save()
    elif(opt == 'S' or opt == 's'):
        print("\n\nObrigado! Até mais...")
        break
    else:
        print("\n\nTente novamente...")
