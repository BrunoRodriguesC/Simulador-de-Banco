import os
import re
from pyparsing import Char
import requests
import Pagina_Central

def NovoCadastro():
    print("Insira as informacoes a seguir")
    print(30*"-")

    def Nome():
        NomeCompleto = input("Nome Completo: ")
        NomeCompleto = [str(char) for char in NomeCompleto if char.isdigit()]
    def Nascimento():
                DatadeNascimento = input("Data de Nascimento: ")
                DatadeNascimento = [int(char) for char in DatadeNascimento if char.isdigit()]
                os.system("cls")
    def RegistrarCpf():
        print("Insira as informacoes a seguir")
        print(30*"-",'\n')
        Cpf = input("CPF: ")
        Cpf = [int(char) for char in Cpf if char.isdigit()]  #  Obtém os números do CPF e ignora outros caracteres
        if len(Cpf) != 11:                                   #  Verifica se o CPF tem 11 dígitos
            print("Cpf invalido, Digite novamente")
            return RegistrarCpf()

        if Cpf == Cpf[::-1]:                                 #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
            Cpf = input("Cpf invalido, Digite novamente: ")
            return RegistrarCpf()
    def NumeroTelefone():
        Telefone = input("Telefone: ")
        Telefone = [int(char) for char in Telefone if char.isdigit()]  #  Obtém os números do CPF e ignora outros caracteres
        if len(Telefone) != 11:                                   #  Verifica se o CPF tem 11 dígitos
            print("Telefone invalido, Digite novamente")
            return NumeroTelefone()

        if Telefone == Telefone[::-1]:                                 #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
            Telefone = input("Telefone invalido, Digite novamente: ")
            return NumeroTelefone()
    def Cep():
                Endereco = input("Cep: ")
                if len(Endereco) != 8:
                    print("Quantidade de digitos invalida!")
                    return Endereco()
                request = requests.get(f"https://viacep.com.br/ws/{Endereco}/json/")
                
                data_endereco = request.json()
                
                print('\n'f"Rua: {data_endereco['logradouro']}")
                print(f"Bairro: {data_endereco['bairro']}")
                print(f"Estado: {data_endereco['uf']}""\n")
                TentardnvCep = int(input("Esta correto: ""\n""sim - 1""\n""Nao - 2""\n"))
                if TentardnvCep == 2:
                    os.system("cls")
                    return Cep()
                os.system("cls")
    def Email():
        global email
        print("Insira as informacoes a seguir")
        print(30*"-")
        VerifiEmail = '^[a-zA-Z0-9._]+[a-zA-Z0-9._]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        email = input("Email: ")
        if re.search(VerifiEmail, email):
            pass
        else:
            print("Email Invalido!")
            return Email() 
    def Senha():
        global Novasenha
        Novasenha = input("Digite uma senha de 6 Digitos: ")
        if len(Novasenha) != 6:
            print("senha invalida, Digite novamente")
            return Senha()
    Nome()
    Nascimento()
    RegistrarCpf()
    NumeroTelefone()
    Cep()
    Email()
    Senha()
    os.system("cls")
    return Cadastrojexistente()
    
def Cadastrojexistente():
    global email
    global Senha
    global Novasenha
    print("Por favor Insira seu Email e Senha""\n")
    Usuario = input("Digite seu Email: ")
    Senha = input("Digite sua Senha: ")
    if Usuario == email and Senha == Novasenha:
        os.system("cls")
        return Pagina_Central.escolha()

    elif Usuario != email:
        os.system("cls")
        print("Email ou senha errado, digite novamente")
        print(1 * '\n')
        return Cadastrojexistente()

    elif Senha != Novasenha:
        os.system("cls")
        print("Email ou senha errado, digite novamente")
        print(1 * '\n')
        return Cadastrojexistente()

def PerguntaInicial():
    
    print("-"*40, "Bem Vindo ao seu App de Banco", "-"*40)
    print(1 * '\n')
    PrimeiraPergunta = Char(input("1 - Criar um novo usuario\n2 - Fazer Login\n3 - sair\n"))
    if PrimeiraPergunta == "1":
        os.system("cls")
        return NovoCadastro()    

    elif PrimeiraPergunta == "2":
        Cadastrojexistente()
        """ PRECISO SALVAR O EMAIL E A SENHA PARA A PROXIMA VEZ QUE ALGUEM ENTRAR, OU VAI DAR ERRO AQUI"""

    elif PrimeiraPergunta == "3":
        os.system("cls")
        exit()

    else:
        os.system("cls")
        print("Essa opcao nao e valida, Tente novamente")
        return PerguntaInicial()

PerguntaInicial()
