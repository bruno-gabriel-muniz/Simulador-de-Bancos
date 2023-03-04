import the_bank_contas_cliente as clientes
import the_bank_contas_bancarias as contas_bank
import graficos as g
# importando o gatpass para utilizalo ao pedir as senhas para os usuários
# e os outros modulos do programa


def ver_saldo_banco():
    """
    Esta função vê qual é o total do saldo do banco
    """
    # falando que a lista contacadastro é global
    global lista_conta_bank
    # cauculando o saldo do banco
    # criando uma variável para conter o valor da soma
    soma_banco = 0
    # criando um range para percorre todos os índices das contas
    for i in range(1, len(lista_conta_bank)):
        # entrado na conta i e somando o valor do salado a
        # variavel que vai dizer quanto dinheiro o banco tem
        soma_banco += lista_conta_bank[i][2]
    # mostrando o saldo do banco
    print("\nO saldo do banco atualmente é: %.2f" % soma_banco)
# criando um função que cria uma conta para de saldo pçara o usuário


def rotina_cliente():
    """
    Função que roda todas as outras funções do programa e
    simula o atendimento ao cliente do banco
    """
    global lista_conta_bank, lista_clientes, num_anterior
    # contar quantos clientes foram atendidos
    cont_clientes = 0
    # verificar se é para o programa ainde ser rodado
    prosseguir = "s"
    while prosseguir == "s":
        # entrando na conta do cliente que será atendido
        usu, usu_senha = clientes.definir_conta_cliente(lista_clientes)
        # atualizando o número de clientes atendidos
        cont_clientes += 1
        # criar ciclo while para a escolha do cliente poder ser refeita caso
        # a entrada seja considerada invalida
        while True:
            # perguntar se o cliente quer abrir, verificar uma conta ou sair
            # do programa (0 para verificar uma conta) (1 para sair)
            # (2 para abrir uma conta)
            escolha_cli = input('''
Escolha se você vai querer:
Alterar uma conta ─> a;
Sair do programa ─> s; ou
Criar uma nova conta ─> c.
Para escolher digite uma das letras: ''').lower()
            # verificar se o usuário digitou 2 para criar uma conta em um if
            if escolha_cli == "c":
                # criando divisoria para ficar mais fácil
                # de visualizar o programa
                g.divisoria()
                # caso ele tenha decidido criar uma conta rodar o programa
                # de abrimento de contas
                # pedir para o usuário abrir uma conta com 6 digitos
                num_anterior = contas_bank.cria_cont_bank(
                    lista_conta_bank, usu, usu_senha, num_anterior,
                    lista_clientes)
            # verificar se o usuário digitou 0 para
            # alterar uma conta em um elif
            elif escolha_cli == "a":
                # criando uma divisória para ficar mais fácil a visualização
                g.divisoria()
                # perguntar o número da conta do cliente
                cont_cli_atual = int(input("\nDigite o número da sua conta: "))
                # mostrar o saldo da conta do cliente e perguntar sobre
                # alterações usando a função altera_cont
                contas_bank.altera_cont_bank(
                    lista_conta_bank, usu, cont_cli_atual, usu_senha)
            # verificar se o usuário decidio fechar o programa com um elif
            elif escolha_cli == "s":
                # criando uma divisória para ficar mais fácil a visualização
                g.divisoria()
                # caso ele tenha decidido sair
                # mostra uma mensagem de agradecimento
                print("\nObrigado pela a sua paciência. Fim do programa.")
                # encerrando este while loop para atender o próximo cliente
                break
            # caso nenhuma das alternativas anteriores ter sido comprida dar
            # uma mensagem de erro e repetir o programa
            else:
                # exibir mensagem de erro
                print("\nNenhuma escolha reconhecida tente novamente.")
            # criando uma divisória para ficar mais fácil a visualização
            g.divisoria()
        # pedindo a entrada para o administrador sobre
        # o atendimento do próximo cliente
        prosseguir = (
            input("\nProsseguir com o próximo cliente? sim-s/não-n: ").lower())
        # fazendo o tratamento de erro para caso ocorra um erro de digitação
        while prosseguir != "s" and prosseguir != "n":
            # avisando que a entrada não foi reconhecida
            print("\nEntrada não reconhacida tente novamente: ")
            # perguntando se para atender o próximo cliente.
            prosseguir = (
                input("\nProsseguir com o próximo cliente? sim-s/não-n: ")
                .lower())
        # imprimindo a divisória para atender o próximo cliente ou encerrar
        # o programa
        g.divisoria()


# criando o ultimo número de conta criada.
# Ps.: futuramente vou fazer uma fuinção que consuta o
# banco de dados e encontra o número da ultima conta criada
num_anterior = 99999
# Criando a lista que ira conter as contas bancárias e uma sublista que
# indica a ordem de cada elemento
# Ps.:Quando fiz isso ainda não tinha estudado sobre dicionários
lista_conta_bank = [["nome", "número da conta", "saldo da conta", "Senha"]]
# Criando a lista que ira conter as contas clientes e uma sublista que
# indica a ordem de cada elemento
# Ps.:Quando fiz isso ainda não tinha estudado sobre dicionários
lista_clientes = [["nome", "senha", "contas do cliente"]]
# rodando o que é, até agora a função principal do projeto
rotina_cliente()
# imprindo a listas para verificar se houve algum erro
# na execução do programa
print(lista_conta_bank, "\n", lista_clientes)
# testando a função que verificar o saldo do banco
ver_saldo_banco()
