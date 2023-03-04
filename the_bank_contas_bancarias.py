import getpass
from graficos import divisoria
# importando o gatpass para utilizalo ao pedir as senhas para os usuários
# e os gráficos do programa


def altera_cont_bank(lista_conta_bank, usu, num, senha):
    """
    Função que modifica as contas existentes do usuário.
    """
    # variavel para pasar pelos indices das listas
    cont = 0
    # criando uma variavel verificadora para
    # melhorar o porgrama com o while loop
    veri = 0
    # criar um while loop que passe por todos os índices das
    # contas com uma verificação da conta ter sido encontrada
    while cont < len(lista_conta_bank) and veri == 0:
        # verificar se o número da conta está correto
        if lista_conta_bank[cont][1] == num:
            # verificando que a conta foi encontrada
            veri = 1
            # verificando se a conta é do usuário
            if lista_conta_bank[cont][0] == usu:
                # criando uma variavel que verifica se a senha está correta
                veri_senha = 0
                for i in range(3)[2:0:-1]:
                    # pedindo a senha da conta para o usuário
                    senha_v = getpass.getpass("Digite a sua senha: ")
                    # verificando se a senha bate
                    if senha == senha_v:
                        # verificando que a senha está correta
                        veri_senha = 1
                        # criar um for loop de modificação na conta
                        while True:
                            # criando uma divisoria para
                            # facilitar a visualização
                            divisoria()
                            # criando uma lista dos nomes itens que
                            # serão exibidos no menu
                            nome_item_exibido = ["Nome: ", "Número da conta: ",
                                                 "Saldo da conta: "]
                            # passando por "todos" os itens em um for lop para
                            # a impreção
                            for i in range(2):
                                # imprimindo os dados com uma
                                # divisória entre eles
                                print("%s %s - " % (
                                    nome_item_exibido[i],
                                    lista_conta_bank[cont][i]), end="")
                            # imprimindo o ultimo dado sem a divisória
                            print("%s %i" % (
                                nome_item_exibido[i+1],
                                lista_conta_bank[cont][1+i]), end="")
                            # mostrando a conta na tela do
                            # usuário e perguntar se ele deseja sacar
                            # ou fazer um deposito na conta ou sair
                            escolha = input('''
Para sacar digite: s;
para depositar digite: d; e
para sair digite: sair
''').lower()
                            # criando uma divisória para ficar
                            #  mais fácil a visualização
                            divisoria()
                            # caso queira sacar
                            if escolha == "s":
                                # criar variavel da
                                # verificação do valor do saque
                                verifica = 0
                                # criar um for loop em caso de erros do
                                #  valor do saque
                                while True:
                                    # perguntar o valor do deposito
                                    saque = float(
                                        input("\nDigite o valor do saque: "))
                                    # verificar se é positivo para que não
                                    #  ocorram erros
                                    if saque > 0:
                                        # caso seja realizar as operações
                                        lista_conta_bank[cont][2] -= saque
                                        break
                            # caso queira depositar elif
                            elif escolha == "d":
                                # criar variavel da verificação
                                verifica = 0
                                # criar um for loop em caso de erros
                                while not verifica:
                                    # perguntar o valor do deposito
                                    deposito = float(
                                        input("""
Digite o valor do deposito: """))
                                    # verificar se é positivo
                                    if deposito > 0:
                                        # caso seja realizar as operações
                                        # e delvolver sem erro
                                        verifica = 1
                                        lista_conta_bank[cont][2] += deposito
                            # caso queira sair da conta elif
                            elif escolha == "sair":
                                # saindo
                                break
                            # caso tenha ocorrido um erro else
                            else:
                                # printar a mensagem de erro
                                print("""
Entrada não reconhecida tente novamente:""")
                        # parando o for loop da senha para o
                        # usuário voltar ao meno principal
                        break
                    # caso não bata
                    else:
                        # entrando em um while loop para
                        # fazer o tratamento de erro
                        while True:
                            # mostrando o atual estado sobre a senha e
                            # perguntando se é para o programa
                            # continuar tentando
                            escolha = input('''
A senha está incorreta.
Você tem mais %i chance(s).
Deseja continuar tentando? (s-sim/n-não): ''' % i).lower()
                            # verificando se a entrada é valida
                            if escolha == "s" or escolha == "n":
                                # se sim saindo do tratamento de erros
                                break
                            # caso não seja informando ao usuário que a
                            # entrada não foi reconhecida
                            print("\nEntrada não reconhecida.")
                        # verificando se o usuário quer continuar tentando
                        if escolha == "n":
                            # caso não saindo do for loop
                            break
                    # verificando se a senha foi reconhecida como a certa
                    if veri_senha:
                        # se sim parando o for loop que pede a senha
                        break
                # erificando se o usuário acertou a senha
                if not veri_senha:
                    # caso não tenha exibindo uma mensagem explicando
                    print("\nSenha não reconhecida.")
                    # e voltando para o menu principal
                    print("\nVoltando para o meno principal...")
            # informando que a conta não está no nome do usuário
            else:
                print("\nA conta está no nome de outra pessoa.")
                break
        # caso não seja a conta adicionando a variavel contadora para o
        # programa ir para a próxima conta
        else:
            cont += 1
    # mostrando a mensagem de erro caso a conta não tenha sido encontrada-
    if veri == 0:
        print("\nErro conta não encontrada")
        # mostra mensagem de erro e sair do programa


def cria_cont_bank(lista_conta_bank, nome_usu, senha, num_anterior,
                   lista_clientes):
    """
    função que cria uma conta bancária e pede:
    lista que contem todas as contas bancárias
    o nome do usuário
    a senha dele
    e o ultimo número dado a uma conta
    """
    # consultando o ultimo número da conta usado e
    # adicionando 1 para criar a nova conta
    num_anterior += 1
    # entrando em um while que vai
    # fazer o tratamento de erro enquanto
    # o deposito
    while True:
        # perguntando se irá ter um deposito inicial
        dep_init_v = (
            input(
                "\nDeseja fazer um deposito inicial na conta?: s-sim/n-não ")
            .lower())
        # se tiver:
        if dep_init_v == "s":
            # pedindo o valor do deposito para o usuário
            deposito = float(input("\nDigite o valor do deposito: "))
            # saindo do while loop'do tartamento de erros
            break
        # se não tiver
        elif dep_init_v == "n":
            # colocando o valor do saldo como 0 inicialmente
            deposito = 0.0
            break
        else:
            # falando que a entrada não foi reconhecida e pedidndo para o
            # usuário tentar novamente
            print("\nEntrada não reconhecida. Tente novamente")
    # mostrando os dados que a conta vai ter para o usuário
    # poder acessar ela depois
    print("\nA conta terá estes dados:")
    # criando a lista com as legendas dos dados
    metadados_da_conta = ["Nome do propietário", "Número da conta", "Saldo"]
    # criando a lista que vai mostrar os dados
    dados_da_conta = [nome_usu, num_anterior, deposito]
    # criando uma variavel contadora para passar pelos dados da conta
    cont = 0
    # entrando no for loop que vai imprimir os dados e as legendas
    for mostra_dado in metadados_da_conta:
        # imprimindo
        print("%5s: %5s" % (mostra_dado, dados_da_conta[cont]))
        # adicionando a variavel contadora para mostrar o próximo dado
        cont += 1
    # passando por um for loop que vai pedir a senha para o usuário
    # que caso erre terá duas chances
    for t in range(3)[2:0:-1]:
        # pedindo a senha para o usuário
        senha_verifica = getpass.getpass(
            "\nDigite a sua senha para finalizar o processo: ")
        # verificando se a senha está correta
        if senha_verifica == senha:
            # criando uma variável que vai verificar se a conta
            # já foi encontrada
            veri = 0
            # entrando em um while loop que vai passar por todas as contas
            # até que encotre a conta certa
            cont = 0
            while cont < len(lista_clientes) and veri == 0:
                # verificar se o nome da conta está correto
                if lista_clientes[cont][0] == nome_usu:
                    # verificando que a conta foi encontrada
                    veri = 1
                    # adicionando o número da nova conta bancária do cliente
                    lista_clientes[cont][2].append(num_anterior)
                cont += 1
            # adicionar o valor na lista e
            # perguntar o valor do deposito
            lista_conta_bank.append([nome_usu, num_anterior, deposito, senha])
            # devolver o valor de aceito
            return num_anterior
        # fazendo o tratamento de erros enquanto a escolha do
        # usuário de continuar tentando acertar a senha ou não
        while True:
            # informando o usuário
            escolha = input('''
A senha não foi reconhecida.
────────────────────────────
Você só tem mais %i chance(s).
Você deseja continuar tentando? (s-sim/n-não): ''' % t)
            # verificando se a escolha esta entre as aceitas
            if escolha == "s" or escolha == "n":
                break
            # mostrando para o usuário que a entrada não foi
            # reconhecida
            print("\nEntrada não reconhecida. Tente novamente")
        # verificando se o usuáriop decidio parar de tentar
        if escolha == "n":
            # se sim saindo do for loop de verificação de senha
            break
