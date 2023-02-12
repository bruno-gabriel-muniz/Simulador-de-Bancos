from graficos import divisoria
import getpass


def definir_conta_cliente(lista_clientes):
    """
    Essa função pede para o usuário escolher entre criar ou entrar
    numa conta antes de entrar nas possibilidades de mexer ou
    alterar as contas bancarias.
    """
    # entrando em um whlie loop para garantir que a entrada seja válida
    while True:
        # perguntando se o usuário quer cria, sair ou entrar em uma conta
        escolha = input(
            '''Você deseja criar uma conta ou entrar em uma já existente?
(entrar=e/criar=c): ''').lower()
        # verificando se a entrada é válida
        if escolha == "e" or escolha == "c":
            # se sim saindo o while loop para não mostrar a mensagem
            # de erro atoa e continuar o programa
            break
        # caso não mostrando a mensagem de erro
        print("entrada não reconhecida, tente novamente.")
    # verificando se a escolha foi criar uma conta
    if escolha == "c":
        # imprimindo um divisoria para facilitar a visualização
        divisoria()
        # rodando o protocolo que cria a conta de um cliente
        return cria_conta_cliente(lista_clientes)
    # verificando se a escolha foi entrar em uma conta
    elif escolha == "e":
        # imprimindo uma divisoria para facilitar a visualização
        divisoria()
        # rodando o protocolo que entra na conta de um cliente
        return entra_conta_cliente(lista_clientes)
    # em caso de um erro
    else:
        print("Por favor tente novamente. Erro não reconhecido.")
        return definir_conta_cliente()


def entra_conta_cliente(lista_clientes):
    # usando uma variavel verificadora para ver se
    # a conta do cliente foi encontrada
    verificadora = 0
    # entrando em um ciclo while para verificar se a conta existe e
    # pedir a entrada do usuário denovo caso ela não exista
    while True:
        # pedindo para o cliente informar o nome da conta que ele quer entrar
        nome = input("Digite o nome da sua conta: ")
        # percorrendos todas as contas para encontrar a que
        # o cliente deseja, pois a conta vai ser uma sub
        # lista e por isso o método index não funcionaria
        for t in lista_clientes:
            # verificando se índice do nome da conta na lista (que representa
            # uma conta) bate com o nome passado pelo o usuário
            if t[0] == nome:
                # verificando para parar o for loop e o whille loop
                # já que a conta já foi encontrada
                verificadora = 1
                # gravando a lista da conta no programa
                conta_cliente = t
                # saindo do for loop
                break
        # verificando se a conta foi encontrada
        if verificadora == 1:
            # se sim saindo do whille loop que verifica se a conta
            # foi encontrada
            break
        # caso o programa não tenha encontrado a conta
        # ele estará avisando o cliente
        print("Conta não encontrada.")
        # perguntando se o usuário quer tentar novamente
        escolha = input(
            '''para sair digite 1.
E para continuar tentando digite qualquer coisa: ''')
        if escolha == "1":
            # imprimindo uma divisoria e sainda da função
            divisoria()
            return definir_conta_cliente()
    # caso tenha encontrado a conta vou pedir a senha
    # dando três chaces tentativa para o usuário
    for i in range(3)[2:0:-1]:
        # pedindo a senha para o usuário e verificando se ela
        # bate com a da lista da conta
        senha = getpass.getpass("Digite a sua senha: ")
        if senha == conta_cliente[1]:
            # se sim reconhecendo a senha
            print("Senha reconhecida. Entrando na conta...")
            divisoria()
            return conta_cliente, senha
        # fazendo a verificação erros enquanto a entrada do usuário
        while True:
            # perguntando se o usuário quer tentar mais uma vez e exibino
            # quantas chances ele tem
            escolha = input(
                '''senha não reconhecida. (Você tem mais %i chances)
Tentar novamente? (s-sim/n-não) ''' % i).lower()
            # verificando se a escolha é válida
            if escolha == "s" or escolha == "n":
                # se sim parando o while loop de veridicaçção de erros
                break
            # caso não explicando a cituação para o cliente
            print("Entrada não reconhecida, tente novamente: ")
        # verificando se a escolha do cliente foi não continuar tentano
        if escolha == "n":
            # se sim parando o for loop e acabando com a função
            break
    divisoria()
    # voltando para o definir conta cliente caso o usuário não tenha
    # consseguido se lembrar da senha
    return definir_conta_cliente()


def cria_conta_cliente(lista_clientes):
    """Esta função cria a conta de um clinte (ou seja uma conta_cliente: não é
    uma conta que possui salado. Mas sim que possui os números das contas que o
     cliente tem) pedindo as variáveis para o usuário sozinha."""
    # pedindo os dados para o usuário e verificando
    # se é para continuar ou reiniciar a operção
    while True:
        # verificando se o usuário desistiu de fazer uma conta_cliente
        sair = input(
            '''caso queira cancelar a criação da nova conta digite 1.
Se não digite qualquer outra coisa: ''')
        if sair == "1":
            # saindo se este for o caso
            break
        # se não prosseguindo com o protocolo
        # pedindo o nome
        nome = input("digite o nome do possuidor da conta: ")
        # criando uma variavel para saber se a conta já existe ou não
        verifica = 0
        # passando por cada nome de clientes do banco de dados
        for i in range(len(lista_clientes)):
            # caso o nome já exista
            if lista_clientes[i][0] == nome:
                # verificando para o while loop pergutar
                # o nome da conta de novo
                verifica = 1
                # saindo do for loop para polpar o processamento
                break
        # verificando que a conta não existe ainda
        if not verifica:
            # pedindo a senha da conta
            senha = getpass.getpass("digite a sua senha: ")
            # verificando a senha para garantir que ela estaja certa
            senha_verifica = getpass.getpass("digite a sua senha novamente: ")
            # verificando se as duas senhas são iguais
            while senha_verifica != senha:
                # se não são pedindo os dados de novo e explicando a
                # situação para o cliente
                print("As duas senhas não batem tente novamente")
                senha = getpass.getpass("digite a sua senha: ")
                senha_verifica = getpass.getpass(
                    "digite a sua senha novamente: ")
            # verificando se a entrada diz para prosseguir com a criação da
            #  conta, não prosseguir ou se é valida
            while True:
                # pedindo a verificação se o usuário quer continuar com a
                # criação com os dados mostrado
                prosseguir = int(input(
                    '''A conta_cliente que será criada terá esses dados:
nome: %s  - senha: %s
Deseja prosseguir?: 1-sim/0-não''' % (nome, senha)))
                if prosseguir == 1 or prosseguir == 0:
                    break
                # explicando que a entrada não foi
                # reconhecida e pedindo ela novamente
                print("Entrada não recoinhecida. Tente novamente.")
            # fazendo a criação da conta caso o
            # usuário tenha decidido prosseguir
            if prosseguir:
                # adcionando a conta na lista dos cadastro
                lista_clientes.append([nome, senha])
                print("Entrando na nova conta... ")
                # imprimindo a divisoria para melhorara a
                # visualisação do aplicativo
                divisoria()
                # retunando o nome e a senha do usuário
                return nome, senha
            # caso não seja para criar a conta perguntar os dados de novo
            else:
                print("os dados serão perguntados novamente.")
                divisoria()
        # avisando que a cointa já existe e perguntando novamente
        else:
            print("Conta já exitente. Tente novamente.")
    # caso o cliente não queira prosseguir com a criação da conta voltando
    # para o menu de entrada do sistema
    return definir_conta_cliente()