#criar função verificadora de números disponiveis
def cria_cont(num,deposito=0):
    #chamar a lista como um valor global
    global conta_cadastro
    #criar variaveis de verificação do estado do cadastro
    erro=0
    #verificar se o número de entrada do úsuario tem 6 digitos
    if 100000<=num <=999999:
        #criando uma variavel para ver se a conta está disponivel
        veri=0
        #criando uma lista auxiliar para usar no for loop de verificação
        conta_cadastro_a=conta_cadastro.copy()
        #criando um for loop para percorre todos os valores da lista de cadastro
        for t in range(len(conta_cadastro_a)):
            #verificar se o número não bate com os números já cadastrados
            if conta_cadastro[t][0] == num:
                # se sim verificando que uma conta já existe
                veri=1
        #caso a onta esteja disponivel
        if veri ==0:
            #adicionar o valor na lista e perguntar o valor do deposito
            conta_cadastro.append([num,deposito])
            #devolver o valor de aceito
            erro=1
            return erro 
        #caso a conta não esteja disponivel
        else:
            print("conta já existente tente novamente.")
            return erro
    #caso não
    else:
        #retornar um valor de erro
        return erro 
#criar uma função de modificação de contas com o argumento sendo o número da conta
def altera_cont(num):
    global conta_cadastro
    #variavel para pasar pelos indices das listas
    cont=0
    #criando uma variavel verificadora para melhorar o porgrama com o while loop
    veri=0
    #criar um while loop que passe por todos os indices de contas
    while cont<len(conta_cadastro) and veri==0:
        #verificar se o número da conta está correto
        if conta_cadastro[cont][0]==num:
            veri=1
            #sair false variavel que verifica se o usuário quer sair da conta
            sair=0
            #criar um for loop de modificação na conta
            while not sair:
                #caso esteja mostrar a conta na tela do usuário e perguntar se ele deseja sacar ou fazer um deposito na conta ou sair
                print(conta_cadastro[cont])
                escolha=int(input("para sacar digite (1), para depositar digite (2) e para sair digite 0: "))
                #caso queira sacar if
                if escolha ==1:
                    #criar variavel da verificação
                    verifica=0
                    #criar um for loop em caso de erros
                    while not verifica:
                        #perguntar o valor do deposito
                        saque=float(input("digite o valor do saque: "))
                        #verificar se é positivo
                        if saque >0:
                            #caso seja realizar as operações e delvolver sem erro                
                            verifica=1
                            conta_cadastro[cont][1]-=saque
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
                            conta_cadastro[cont][1]+=deposito
                #caso queira sair da conta elif
                elif escolha ==0:
                    #sair true
                    sair=1
                #caso tenha ocorrido um erro else
                else:
                    #printar a mensagem de erro
                    print("entrada não reconhecida tente novamente: ")
        else:
            cont+=1
    if veri ==0: 
        print("erro conta não encontrada")
        #mostra mensagem de erro e sair do programa
#criar a lista global dos números e valores das contas  
def rotina_cliente():
    global conta_cadastro
    #contar quantos clientes foram atendidos
    cont_clientes=0
    #verificar se é para o programa ainde ser rodado
    prosseguir=1
    while prosseguir:
        cont_clientes+=1
        #criar variavel de verificação de erro
        erro=1
        #criar ciclo while para a escolha do cliente poder ser refeita caso a entrada seja considerada invalida
        while erro==1:
            #perguntar se o cliente quer abrir, verificar uma conta ou sair do programa (0 para verificar uma conta) (1 para sair) (2 para abrir uma conta)
            escolha_cli=int(input("esolha se você vai querer alterar uma conta(0), sair do programa(1) ou criar uma nova conta(2) digitando um destes números: "))
            #verificar se o usuário digitou 2 para criar uma conta em um if
            if escolha_cli==2:
                #verificar que o programa foi rodado para o ciclo while não pedir a escolha do usuário denovo
                erro=0
                #caso ele tenha decidido criar uma conta rodar o programa de abrimento de contas
                #criar v para verificar o sucesso do while loop
                v=0
                #entrar num wihile loop para pedir os seis digitos para o usuário 
                while not v:
                    #pedir para o usuário abrir uma conta com 6 digitos
                    v=cria_cont(int(input("escolha o número da nova conta que esteja entre 100000 e 999999: ")), int(input("caso querira fazer deposito na nova conta digite o valor se não você pode só digitar 0: ")))
            #verificar se o usuário digitou 0 para alterar uma conta em um elif
            elif escolha_cli==0:
                #verificar que o programa foi rodado para o ciclo while não pedir a escolha do usuário denovo
                erro=0
                #perguntar o número da conta do cliente
                cont_cli_atual=int(input("digite o número da sua conta: "))
                #mostrar o saldo da conta do cliente e perguntar sobre alterações usando a função altera_cont
                altera_cont(cont_cli_atual)
                #perguntar se o cliente quer realizar um deposito a retirara parate do dinheiro
                print("está ferramenta ainda está em desenvolvimento.")    
            #verificar se o usuário decidio fechar o programa com um elif
            elif escolha_cli==1:
                #verificar que o programa foi rodado para o ciclo while não pedir a escolha do usuário denovo
                erro=0
                #caso ele tenha decidido sair mostra uma mensagem de agradecimento
                print("Obrigado pela a sua paciencia. Fim do programa.")    
            #caso nenhuma das alternativas anteriores ter sido comprida dar uma mensagem de erro e repetir o programa
            else:
                #exibir mensagem de erro
                print("nenhuma escolha reconhecida tente novamente.")
        #perguntando se para atender o próximo cliente.
        prosseguir=int(input("prosseguir com o próximo cliente? sim(1) não(0): "))
conta_cadastro=[[0,0]]
rotina_cliente()
print(conta_cadastro)