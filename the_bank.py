import the_bank_contas_cliente as clientes
import the_bank_contas_bancarias as contas_bank
import graficos as g
# importando o gatpass para utilizalo ao pedir as senhas para os usuários
# criando uma função que verifica o saldo total do banco.


def ver_saldo_banco():
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
    print("O saldo do banco atualmente é: %.2f" % soma_banco)
# criando um função que cria uma conta para de saldo pçara o usuário


def rotina_cliente():
    global lista_conta_bank, lista_clientes
    # contar quantos clientes foram atendidos
    cont_clientes = 0
    # verificar se é para o programa ainde ser rodado
    prosseguir = 1
    while prosseguir:
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
            escolha_cli = int(input(
                '''Escolha se você vai querer:
Alterar uma conta(0);
Sair do programa(1); ou
Criar uma nova conta(2).
Para escolher digite um dos números: '''))
            # verificar se o usuário digitou 2 para criar uma conta em um if
            if escolha_cli == 2:
                # criando divisoria para ficar mais fácil
                # de visualizar o programa
                g.divisoria()
                # caso ele tenha decidido criar uma conta rodar o programa
                # de abrimento de contas
                # pedir para o usuário abrir uma conta com 6 digitos
                contas_bank.cria_cont_bank(lista_conta_bank, usu, usu_senha)
            # verificar se o usuário digitou 0 para
            # alterar uma conta em um elif
            elif escolha_cli == 0:
                # criando uma divisória para ficar mais fácil a visualização
                g.divisoria()
                # perguntar o número da conta do cliente
                cont_cli_atual = int(input("digite o número da sua conta: "))
                # mostrar o saldo da conta do cliente e perguntar sobre
                # alterações usando a função altera_cont
                contas_bank.altera_cont_bank(
                    lista_conta_bank, usu, cont_cli_atual, usu_senha)
            # verificar se o usuário decidio fechar o programa com um elif
            elif escolha_cli == 1:
                # criando uma divisória para ficar mais fácil a visualização
                g.divisoria()
                # caso ele tenha decidido sair
                # mostra uma mensagem de agradecimento
                print("Obrigado pela a sua paciência. Fim do programa.")
                # encerrando este while loop para atender o próximo cliente
                break
            # caso nenhuma das alternativas anteriores ter sido comprida dar
            # uma mensagem de erro e repetir o programa
            else:
                # exibir mensagem de erro
                print("nenhuma escolha reconhecida tente novamente.")
            # criando uma divisória para ficar mais fácil a visualização
            g.divisoria()
        # pedindo a entrada para o administrador sobre
        # o atendimento do próximo cliente
        prosseguir = int(
            input("prosseguir com o próximo cliente? sim(1) não(0): "))
        # fazendo o tratamento de erro para caso ocorra um erro de digitação
        while prosseguir != 0 and prosseguir != 1:
            # avisando que a entrada não foi reconhecida
            print("entrada não reconhacida tente novamente: ")
            # perguntando se para atender o próximo cliente.
            prosseguir = int(
                input("prosseguir com o próximo cliente? sim(1) não(0): "))
        g.divisoria()


lista_conta_bank = [["nome", "número da conta", "saldo da conta", "Senha"]]
lista_clientes = [["nome", "senha", "contas do cliente"]]
rotina_cliente()
print(lista_conta_bank, "\n", lista_clientes)
ver_saldo_banco()
