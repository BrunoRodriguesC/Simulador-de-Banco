import os
from pyparsing import Char


class Cliente:
    global Saldo
    Saldo = 0

def Depositar():
    global Saldo
    global dinheiro
    dinheiro = float(input("Qual valor voce deseja depositar na sua conta R$: "))   # Colocar um verificar para returnar Depositar() caso seja inserido str
    os.system("cls")
    ChecarDeposito()

def DepositarNovamente():
            OutroDeposito = Char(input("Deseja realizar outra transacao ?""\n""Sim - 1""\n""Nao - 2""\n"))
            if OutroDeposito == "1":
                os.system("cls")
                return Depositar()
            elif OutroDeposito == "2":
                os.system("cls")
                return escolha()
            elif OutroDeposito !=  "1" and "2":
                os.system("cls")
                print("Comando invalido, tente novamente")
                print("\n")
                return DepositarNovamente()

def ChecarDeposito():
    global confirmacao
    global Saldo
    global dinheiro
    print(f"Confira os dados para fazer o deposito: R$: {dinheiro:.2f}")
    print("\n")
    confirmacao = Char(input("Enviar - 1""\n""Voltar - 2""\n"))
    os.system("cls")
    if confirmacao == "1":
        print("Dinheiro enviado com sucesso!")
        Saldo += dinheiro
        print(f"Seu Saldo atual é R${Saldo:.2f}")
        print("\n")
        DepositarNovamente()
    elif confirmacao == "2":
        os.system("cls")
        return Depositar()
    elif confirmacao != "1" and "2":
        os.system("cls")
        print("Comando invalido, tente novamente")
        print("\n")
        return ChecarDeposito()

def MostrarSaldo():
    global Saldo
    global OpcoesSaldo
    print(f"Saldo: R$ {Saldo:.2f}""\n")
    OpcoesSaldo = Char(input("1 - Saque""\n""2 - Deposito""\n""3 - Transferir""\n""4 - Voltar""\n"))
    if OpcoesSaldo == "1":
        os.system("cls")
                                                                    # return MostrarSaldo() Ir PARA O SAQUE
    elif OpcoesSaldo == "2":
        os.system("cls")
        return Depositar()                                          #fazer opcao de extrato mostrar no saldo as transacoes
    elif OpcoesSaldo == "3":
        os.system("cls")
                                                                    #return Depositar() IR PARA A TRANFERENCIA
    elif OpcoesSaldo == "4":
        os.system("cls")
        return escolha()
    elif OpcoesSaldo != "1" and "2" and "3" and "4":
        os.system("cls")
        print("Comando invalido, tente novamente")
        print("\n")
        return MostrarSaldo()


def escolha():
    print("-"*40,"Menu Inicial","-"*40)
    opcoes = Char(input("1 - Saldo""\n""2 - Saque""\n""3 - Deposito""\n""4 - Tranferencia""\n""5 - Sair""\n"))
    if opcoes == "1":
        os.system("cls")
        return MostrarSaldo() 
    elif opcoes == "2":
        print("Saque") 
    elif opcoes == "3":
        os.system("cls")
        return Depositar()
    elif opcoes == "4":
        print("Tranferencia")
    elif opcoes == "5":
        os.system("cls")
        exit()
    elif opcoes != "1" and "2" and  "3" and "4" and "5":
        os.system("cls")
        print("Comando invalido, tente novamente")
        print("\n")
        return escolha()
