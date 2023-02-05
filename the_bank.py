#importando o gatpass para utilizalo ao pedir as senhas para os usuários
import getpass
#criando uma função que verifica o saldo total do banco.
def ver_saldo_banco():
    #falando que a lista contacadastro é global
    global lista_conta_bank
    #cauculando o saldo do banco
    #criando uma variável para conter o valor da soma
    soma_banco=0
    #criando um range para percorre todos os índices das contas
    for i in range(1,len(lista_conta_bank)):
        #entrado na conta i e somando o valor do salado a variavel que vai dizer quanto dinheiro o banco tem 
        soma_banco+=lista_conta_bank[i][2]
    #mostrando o saldo do banco
    print("o saldo do banco atualmente é: %.2f"%soma_banco)
#criando um função que cria uma conta para de saldo pçara o usuário
def cria_cont_bank(nome_usu,senha):
    #chamar a lista como um valor global
    global lista_conta_bank
    #pedindo o número da nova conta
    num=int(input("escolha o número da nova conta que esteja entre 100000 e 999999, ou seja, tenha 6 digitos: "))
    #entrando em um while que vai fazer o tratamento de erro enquanto o deposito
    while True:
        #perguntando se ira ter um deposito inicial
        dep_init_v=int(input("deseja fazer um deposito inicial na conta?: 1-sim/0-não "))
        #se tiver:
        if dep_init_v:
            #pedindo o valor do deposito para o usuário
            deposito=float(input("digite o valor do deposito: "))
            #saindo do while loop'do tartamento de erros
            break
        #se não tiver
        elif dep_init_v ==0:
            #colocando o valor do saldo como 0 inicialmente 
            deposito=0.0
            break
        else:
            #falando que a entrada não foi reconhecida e pedidndo para o usuário tentar novamente
            print("Entrada não reconhecida. Tente novamente")
    #verificar se o número de entrada do úsuario tem 6 digitos
    if 100000<=num <=999999:
        #criando uma variavel para ver se a conta está disponivel
        veri=0
        #criando uma lista auxiliar para usar no for loop de verificação
        lista_conta_bank_a=lista_conta_bank.copy()
        #criando um for loop para percorre todos os valores da lista de cadastro
        for t in range(len(lista_conta_bank_a)):
            #verificar se o número não bate com os números já cadastrados
            if lista_conta_bank[t][1] == num:
                # se sim verificando que uma conta já existe
                veri=1
        #caso a onta esteja disponivel
        if veri == 0:
            for t in range(3)[2:0:-1]:
                senha_verifica=getpass.getpass("Digite a sua senha para finalizar o processo: ")
                if senha_verifica==senha:
                    #adicionar o valor na lista e perguntar o valor do deposito
                    lista_conta_bank.append([nome_usu, num, deposito, senha])
                    #devolver o valor de aceito
                    return
                while True:
                    escolha=input("A senha não foi reconhecida. Você só tem mais %i chance(s). Você deseja continuar tentando? (s-sim/n-não): "%t)
                    if escolha == "s" or escolha == "n":
                        break
                if escolha=="n":
                    break
        #caso a conta não esteja disponivel
        else:
            print("este número de conta já existente. Tente novamente \n Ps.:O saque também não foi aceito.")
            return cria_cont_bank()
        print("voltando para o menu principal...")
        divisoria()
        return 
    #caso não
    else:
        #retornar um valor de erro e uma mensagem explicando a situação para o usuário
        print("o número não tem 6 digitos, ou seja ele não esta entre 100000 e 999999")
        return cria_cont_bank()
#criar uma função de modificação de contas com o argumento sendo o número da conta
def altera_cont_bank(usu,num,senha):
    global lista_conta_bank
    #variavel para pasar pelos indices das listas
    cont=0
    #criando uma variavel verificadora para melhorar o porgrama com o while loop
    veri=0
    #criar um while loop que passe por todos os indices de contas com uma verificação da conta ter sido encontrada
    while cont<len(lista_conta_bank) and veri==0:
        #verificar se o número da conta está correto
        if lista_conta_bank[cont][1]==num:
            #verificando que a conta foi encontrada
            veri=1
            #verificando se a conta é do usuário
            if lista_conta_bank[cont][0]==usu:
                #criando uma variavel que verifica se a senha está correta
                veri_senha=0
                for i in range(3)[2:0:-1]:
                    #pedindo a senha da conta para o usuário
                    senha_v=getpass.getpass("Digite a sua senha: ")
                    #verificando se a senha bate
                    if senha == senha_v:
                        #verificando que a senha está correta 
                        veri_senha=1
                        #criar um for loop de modificação na conta
                        while True:
                            #caso esteja mostrar a conta na tela do usuário e perguntar se ele deseja sacar ou fazer um deposito na conta ou sair
                            print(lista_conta_bank[cont])
                            escolha=int(input("para sacar digite 1, para depositar digite 2 e para sair digite 0: "))
                            #criando uma divisória para ficar mais fácil a visualização
                            divisoria()
                            #caso queira sacar if
                            if escolha ==1:
                                #criar variavel da verificação do valor do saque
                                verifica=0
                                #criar um for loop em caso de erros do valor do saque
                                while True:
                                    #perguntar o valor do deposito
                                    saque=float(input("digite o valor do saque: "))
                                    #verificar se é positivo para que não ocorram erros
                                    if saque >0:
                                        #caso seja realizar as operações                
                                        lista_conta_bank[cont][2]-=saque
                                        break
                                #criando uma divisória para ficar mais fácil a visualização
                                divisoria()
                            #caso queira depositar elif
                            elif escolha ==2:
                                #criar variavel da verificação
                                verifica=0
                                #criar um for loop em caso de erros
                                while not verifica:
                                    #perguntar o valor do deposito
                                    deposito=float(input("digite o valor do deposito: "))
                                    #verificar se é positivo
                                    if deposito >0:
                                        #caso seja realizar as operações e delvolver sem erro                
                                        verifica=1
                                        lista_conta_bank[cont][2]+=deposito
                                #criando uma divisória para ficar mais fácil a visualização
                                divisoria()
                            #caso queira sair da conta elif
                            elif escolha ==0:
                                #criando uma divisória para ficar mais fácil a visualização
                                divisoria()
                                #sair true
                                break
                            #caso tenha ocorrido um erro else
                            else:
                                #printar a mensagem de erro
                                print("Entrada não reconhecida tente novamente: ")
                            #crinado uma divisoria para ficar mais fácil de se visualizar
                            divisoria()
                        #parando o for loop da senha para o usuário voltar ao meno principal
                        break
                    #caso não bata
                    else:
                        #entrando em um while loop para fazer o tratamento de erro
                        while True:
                            #mostrando o atual estado sobre a senha e perguntando se é para o programa continuar tentando  
                            escolha=input("A senha está incorreta. Você tem mais %i chance(s). Deseja continuar tentando? (s-sim/n-não): ").lower()
                            #verificando se a entrada é valida
                            if escolha == "s" or escolha == "n":
                                #se sim saindo do tratamento de erros
                                break
                            #caso não seja informando ao usuário que a entrada não foi reconhecida
                            print("Entrada não reconhecida.")
                        #verificando se o usuário quer continuar tentando
                        if escolha== "n":
                            #caso não saindo do for loop
                            break
                    #verificando se a senha foi 
                    if veri_senha:
                        break
                if not veri_senha:
                    print("Senha não reconhecida.")
                    print("Voltando para o meno principal...")
                    divisoria()
            #informando que a conta não está no nome do usuário
            else:
                print("A conta está no nome de outra pessoa.")
                divisoria()
        #caso não seja a conta adicionando a variavel contadora para o programa ir para a próxima conta
        else:
            cont+=1
    #mostrando a mensagem de erro caso a conta não tenha sido encontrada-
    if veri ==0: 
        print("erro conta não encontrada")
        #mostra mensagem de erro e sair do programa
#criar a lista global dos números e valores das contas
def cria_conta_cliente():
    """Esta função cria a conta de um clinte (ou seja uma conta_cliente: não é uma conta que possui salado. Mas sim que 
    possui os números das contas que o cliente tem) pedindo as variáveis para o usuário sozinha."""
    #mostrando que a variavel lista_clientes que é o banco de dados do banco é um lista global
    global lista_clientes
    #pedindo os dados para o usuário e verificando se é para continuar ou reiniciar a operção
    while True:
        #verificando se o usuário desistiu de fazer uma conta_cliente
        sair=input("caso queira cancelar a criação da nova conta digite 1 se não digite qualquer outra coisa: ")
        if sair=="1":
            #saindo se este for o caso
            break
        #se não prosseguindo com o protocolo
        #pedindo o nome
        nome=input("digite o nome do possuidor da conta: ")
        #criando uma variavel para saber se a conta já existe ou não
        verifica=0
        #passando por cada nome de clientes do banco de dados
        for i in range(len(lista_clientes)):
            #caso o nome já exista
            if lista_clientes[i][0]==nome:
                #verificando para o while loop pergutar o nome da conta de novo
                verifica=1
                #saindo do for loop para polpar o processamento
                break
        #verificando que a conta não existe ainda
        if not verifica:
            #pedindo a senha da conta
            senha=getpass.getpass("digite a sua senha: ")
            #verificando a senha para garantir que ela estaja certa
            senha_verifica=getpass.getpass("digite a sua senha novamente: ")
            #verificando se as duas senhas são iguais
            while senha_verifica != senha:
                #se não são pedindo os dados de novo e explicando a situação para o cliente
                print("As duas senhas não batem tente novamente")
                senha=getpass.getpass("digite a sua senha: ")
                senha_verifica=getpass.getpass("digite a sua senha novamente: ") 
            #verificando se a entrada diz para prosseguir com a criação da conta, não prosseguir ou se é valida
            while True:
                #pedindo a verificação se o usuário quer continuar com a criação com os dados mostrado
                prosseguir=int(input("A conta_cliente que será criada terá esses dados: \nnome: %s  - senha: %s \nDeseja prosseguir?: 1-sim/0-não" %(nome,senha)))
                if prosseguir == 1 or prosseguir==0:
                    break
                #explicando que a entrada não foi reconhecida e pedindo ela novamente
                print("Entrada não recoinhecida. Tente novamente.")
            #fazendo a criação da conta caso o usuário tenha decidido prosseguir
            if prosseguir:
                #adcionando a conta na lista dos cadastro
                lista_clientes.append([nome,senha])
                print("Entrando na nova conta... ")
                #imprimindo a divisoria para melhorara a visualisação do aplicativo
                divisoria()
                #retunando o nome e a senha do usuário
                return nome, senha
            #caso não seja para criar a conta perguntar os dados de novo
            else:
                print("os dados serão perguntados novamente.")
                divisoria()
        #avisando que a cointa já existe e perguntando novamente 
        else:
            print("Conta já exitente. Tente novamente.")
    #caso o cliente não queira prosseguir com a criação da conta voltando para o menu de entrada do sistema
    return definir_conta_cliente()
def entra_conta_cliente():
    #falando que a lista cliente é global
    global lista_clientes
    #usando uma variavel verificadora para ver se a conta do cliente foi encontrada
    verificadora=0
    #entrando em um ciclo while para verificar se a conta existe e pedir a entrada do usuário denovo caso ela não exista
    while True:
        #pedindo para o cliente informar o nome da conta que ele quer entrar
        nome = input("Digite o nome da sua conta: ")
        #percorrendos todas as contas para encontrar a que o cliente deseja, pois a conta vai ser uma sub lista e por isso o método index não funcionaria 
        for t in lista_clientes:
            #verificando se índice do nome da conta na lista (que representa uma conta) bate com o nome passado pelo o usuário
            if t[0] == nome:
                #verificando para parar o for loop e o whille loop já que a conta já foi encontrada
                verificadora=1
                #gravando a lista da conta no programa 
                conta_cliente=t
                #saindo do for loop
                break
        #verificando se a conta foi encontrada
        if verificadora==1:
            #se sim saindo do whille loop que verifica se a conta foi encontrada
            break
        #caso o programa não tenha encontrado a conta ele estará avisando o cliente
        print("Conta não encontrada.")
        #perguntando se o usuário quer tentar novamente
        escolha=input("para sair digite 1 e para continuar tentando digite qualquer coisa: ")
        if escolha == "1":
            #imprimindo uma divisoria e sainda da função
            divisoria()
            return definir_conta_cliente()
    #caso tenha encontrado a conta vou pedir a senha dando três chaces tentativa para o usuário
    for i in range(3)[2:0:-1]:
        #pedindo a senha para o usuário e verificando se ela bate com a da lista da conta
        senha=getpass.getpass("Digite a sua senha: ")
        if senha == conta_cliente[1]:
            #se sim reconhecendo a senha
            print("Senha reconhecida. Entrando na conta...")
            divisoria()
            return conta_cliente, senha
        #fazendo a verificação erros enquanto a entrada do usuário
        while True:
            #perguntando se o usuário quer tentar mais uma vez e exibino quantas chances ele tem
            escolha=input("senha não reconhecida. (Você tem mais %i chances) Tentar novamente? (s-sim/n-não) "%i).lower()
            #verificando se a escolha é válida
            if escolha == "s" or escolha == "n":
                #se sim parando o while loop de veridicaçção de erros
                break
            #caso não explicando a cituação para o cliente
            print("Entrada não reconhecida, tente novamente: ")
        #verificando se a escolha do cliente foi não continuar tentano
        if escolha == "n":
            #se sim parando o for loop e acabando com a função
            break
    divisoria()
    #voltando para o definir conta cliente caso o usuário não tenha consseguido se lembrar da senha
    return definir_conta_cliente()
def definir_conta_cliente():
    """Essa função pede para o usuário escolher entre criar ou entrar numa conta antes de entrar nas
    possibilidades de mexer ou alterar as contas bancarias."""
    #entrando em um whlie loop para garantir que a entrada seja válida
    while True:
        #perguntando se o usuário quer cria, sair ou entrar em uma conta
        escolha=input("Você deseja criar uma conta ou entrar em uma já existente? (entrar=e/criar=c)").lower()
        #verificando se a entrada é válida
        if escolha == "e" or escolha=="c":
            #se sim saindo o while loop para não mostrar a mensagem de erro atoa e continuar o programa
            break
        #caso não mostrando a mensagem de erro
        print("entrada não reconhecida, tente novamente.")
    #verificando se a escolha foi criar uma conta 
    if escolha == "c":
        #imprimindo um divisoria para facilitar a visualização
        divisoria()
        #rodando o protocolo que cria a conta de um cliente
        return cria_conta_cliente()
    #verificando se a escolha foi entrar em uma conta
    elif escolha=="e":
        #imprimindo uma divisoria para facilitar a visualização
        divisoria()
        #rodando o protocolo que entra na conta de um cliente
        return entra_conta_cliente()
    #em caso de um erro
    else:
        print("Por favor tente novamente. Erro não reconhecido.")
        return definir_conta_cliente()
def rotina_cliente():
    global lista_conta_bank, lista_clientes
    #contar quantos clientes foram atendidos
    cont_clientes=0
    #verificar se é para o programa ainde ser rodado
    prosseguir=1
    while prosseguir:
        #entrando na conta do cliente que será atendido
        usu,usu_senha=definir_conta_cliente()
        #atualizando o número de clientes atendidos
        cont_clientes+=1
        #criar ciclo while para a escolha do cliente poder ser refeita caso a entrada seja considerada invalida
        while True:
            #perguntar se o cliente quer abrir, verificar uma conta ou sair do programa (0 para verificar uma conta) (1 para sair) (2 para abrir uma conta)
            escolha_cli=int(input('''Escolha se você vai querer:
Alterar uma conta(0);
Sair do programa(1); ou 
Criar uma nova conta(2).
Para escolher digite um dos números: '''))
            #verificar se o usuário digitou 2 para criar uma conta em um if
            if escolha_cli==2:
                #criando divisoria para ficar mais fácil de visualizar o programa
                divisoria()
                #caso ele tenha decidido criar uma conta rodar o programa de abrimento de contas
                #pedir para o usuário abrir uma conta com 6 digitos
                cria_cont_bank(usu,usu_senha)
            #verificar se o usuário digitou 0 para alterar uma conta em um elif
            elif escolha_cli==0:
                #criando uma divisória para ficar mais fácil a visualização
                divisoria()
                #perguntar o número da conta do cliente
                cont_cli_atual=int(input("digite o número da sua conta: "))
                #mostrar o saldo da conta do cliente e perguntar sobre alterações usando a função altera_cont
                altera_cont_bank(usu,cont_cli_atual,usu_senha)  
            #verificar se o usuário decidio fechar o programa com um elif
            elif escolha_cli==1:
                #criando uma divisória para ficar mais fácil a visualização
                divisoria()
                #caso ele tenha decidido sair mostra uma mensagem de agradecimento
                print("Obrigado pela a sua paciência. Fim do programa.")
                #encerrando este while loop para atender o próximo cliente
                break                
            #caso nenhuma das alternativas anteriores ter sido comprida dar uma mensagem de erro e repetir o programa
            else:
                #exibir mensagem de erro
                print("nenhuma escolha reconhecida tente novamente.")
            #criando uma divisória para ficar mais fácil a visualização
            divisoria()
        #pedindo a entrada para o administrador sobre o atendimento do próximo cliente
        prosseguir=int(input("prosseguir com o próximo cliente? sim(1) não(0): "))
        #fazendo o tratamento de erro para caso ocorra um erro de digitação 
        while prosseguir !=0 and prosseguir != 1:
            #avisando que a entrada não foi reconhecida
            print("entrada não reconhacida tente novamente: ")
            #perguntando se para atender o próximo cliente.
            prosseguir=int(input("prosseguir com o próximo cliente? sim(1) não(0): "))
        divisoria()
def divisoria():
    #criando divisoria para ficar mais fácil de visualizar o programa
    print("\n","="*30,"\n")
lista_conta_bank=[["nome","número da conta","saldo da conta","Senha"]]
lista_clientes=[["nome","senha","contas do cliente"]] 
rotina_cliente()
print(lista_conta_bank,"\n",lista_clientes)
ver_saldo_banco()