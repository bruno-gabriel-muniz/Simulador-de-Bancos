import getpass
from graficos import divisoria


def altera_cont_bank(lista_conta_bank, usu, num, senha):
    """
    Função que modifica as contas existentes do usuário
    """
    # variavel para pasar pelos indices das listas
    cont = 0
    # criando uma variavel verificadora para
    # melhorar o porgrama com o while loop
    veri = 0
    # criar um while loop que passe por todos os indices de
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
                            # caso esteja mostrar a conta na tela do
                            # usuário e perguntar se ele deseja sacar
                            # ou fazer um deposito na conta ou sair
                            print(lista_conta_bank[cont])
                            escolha = int(
                                input(
                                    '''para sacar digite 1;
para depositar digite 2; e
para sair digite 0: '''))
                            # criando uma divisória para ficar
                            #  mais fácil a visualização
                            divisoria()
                            # caso queira sacar if
                            if escolha == 1:
                                # criar variavel da
                                # verificação do valor do saque
                                verifica = 0
                                # criar um for loop em caso de erros do
                                #  valor do saque
                                while True:
                                    # perguntar o valor do deposito
                                    saque = float(
                                        input("digite o valor do saque: "))
                                    # verificar se é positivo para que não
                                    #  ocorram erros
                                    if saque > 0:
                                        # caso seja realizar as operações
                                        lista_conta_bank[cont][2] -= saque
                                        break
                                # criando uma divisória para ficar
                                # mais fácil a visualização
                                divisoria()
                            # caso queira depositar elif
                            elif escolha == 2:
                                # criar variavel da verificação
                                verifica = 0
                                # criar um for loop em caso de erros
                                while not verifica:
                                    # perguntar o valor do deposito
                                    deposito = float(
                                        input("digite o valor do deposito: "))
                                    # verificar se é positivo
                                    if deposito > 0:
                                        # caso seja realizar as operações
                                        # e delvolver sem erro
                                        verifica = 1
                                        lista_conta_bank[cont][2] += deposito
                                # criando uma divisória para ficar
                                # mais fácil a visualização
                                divisoria()
                            # caso queira sair da conta elif
                            elif escolha == 0:
                                # criando uma divisória para ficar
                                # mais fácil a visualização
                                divisoria()
                                # sair true
                                break
                            # caso tenha ocorrido um erro else
                            else:
                                # printar a mensagem de erro
                                print(
                                    "Entrada não reconhecida tente novamente:")
                            # crinado uma divisoria para ficar
                            # mais fácil de se visualizar
                            divisoria()
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
                            escolha = input(
                                '''A senha está incorreta.
Você tem mais %i chance(s).
Deseja continuar tentando? (s-sim/n-não): ''').lower()
                            # verificando se a entrada é valida
                            if escolha == "s" or escolha == "n":
                                # se sim saindo do tratamento de erros
                                break
                            # caso não seja informando ao usuário que a
                            # entrada não foi reconhecida
                            print("Entrada não reconhecida.")
                        # verificando se o usuário quer continuar tentando
                        if escolha == "n":
                            # caso não saindo do for loop
                            break
                    # verificando se a senha foi
                    if veri_senha:
                        break
                if not veri_senha:
                    print("Senha não reconhecida.")
                    print("Voltando para o meno principal...")
                    divisoria()
            # informando que a conta não está no nome do usuário
            else:
                print("A conta está no nome de outra pessoa.")
                divisoria()
        # caso não seja a conta adicionando a variavel contadora para o
        # programa ir para a próxima conta
        else:
            cont += 1
    # mostrando a mensagem de erro caso a conta não tenha sido encontrada-
    if veri == 0:
        print("erro conta não encontrada")
        # mostra mensagem de erro e sair do programa


def cria_cont_bank(lista_conta_bank, nome_usu, senha):
    # pedindo o número da nova conta
    num = int(input(
        '''Escolha o número da nova conta que esteja entre 1 e 999999, ou seja,
tenha 6 digitos: '''))
    # entrando em um while que vai
    # fazer o tratamento de erro enquanto
    # o deposito
    while True:
        # perguntando se ira ter um deposito inicial
        dep_init_v = int(
            input("deseja fazer um deposito inicial na conta?: 1-sim/0-não "))
        # se tiver:
        if dep_init_v:
            # pedindo o valor do deposito para o usuário
            deposito = float(input("digite o valor do deposito: "))
            # saindo do while loop'do tartamento de erros
            break
        # se não tiver
        elif dep_init_v == 0:
            # colocando o valor do saldo como 0 inicialmente
            deposito = 0.0
            break
        else:
            # falando que a entrada não foi reconhecida e pedidndo para o
            # usuário tentar novamente
            print("Entrada não reconhecida. Tente novamente")
    # verificar se o número de entrada do úsuario tem 6 digitos
    if 100000 <= num <= 999999:
        # criando uma variavel para ver se a conta está disponivel
        veri = 0
        # criando uma lista auxiliar para usar no for loop de verificação
        lista_conta_bank_a = lista_conta_bank.copy()
        # criando um for loop para percorre todos os
        # valores da lista de cadastro
        for t in range(len(lista_conta_bank_a)):
            # verificar se o número não bate com os números já cadastrados
            if lista_conta_bank[t][1] == num:
                # se sim verificando que uma conta já existe
                veri = 1
        # caso a conta esteja disponivel
        if veri == 0:
            for t in range(3)[2:0:-1]:
                senha_verifica = getpass.getpass(
                    "Digite a sua senha para finalizar o processo: ")
                if senha_verifica == senha:
                    # adicionar o valor na lista e
                    # perguntar o valor do deposito
                    lista_conta_bank.append([nome_usu, num, deposito, senha])
                    # devolver o valor de aceito
                    return
                while True:
                    escolha = input('''A senha não foi reconhecida.
                    Você só tem mais %i chance(s).
                    Você deseja continuar tentando? (s-sim/n-não): ''' % t)
                    if escolha == "s" or escolha == "n":
                        break
                if escolha == "n":
                    break
        # caso a conta não esteja disponivel
        else:
            print(
                '''este número de conta já existente. Tente novamente
Ps.:O saque também não foi aceito.''')
            return cria_cont_bank()
        print("voltando para o menu principal...")
        divisoria()
        return
    # caso não
    else:
        # retornar um valor de erro e uma mensagem
        # explicando a situação para o usuário
        print("o número não está entre 100000 e 999999")
        return cria_cont_bank(nome_usu, senha)
