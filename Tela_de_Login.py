import os
import requests
import re

class Cadastro():

    def NovoCadastro():
        def Telinha():
            print("Insira as informacoes a seguir")
            print(30*"-")
        def LimparTela():
            os.system("cls")
        def InformacoesPessoais():
            Telinha()
            def Nome():
                NomeCompleto = input("Nome Completo: ")
                NomeCompleto = [str(char) for char in NomeCompleto if char.isdigit()]
            def Nascimento():
                DatadeNascimento = input("Data de Nascimento: ")
                DatadeNascimento = [int(char) for char in DatadeNascimento if char.isdigit()]
                LimparTela()
                Telinha()
            def Genero():
                print("\n""Masculino - 1""\n""Feminino - 2""\n""Outro - 3""\n")
                Genero = int(input("Genero: "))
                LimparTela()
                Telinha()
            def Endereco():
                Endereco = input("Cep: ")
                if len(Endereco) != 8:
                    print("Quantidade de digitos invalida!")
                    return Endereco()
                request = requests.get(f"https://viacep.com.br/ws/{Endereco}/json/")
                
                data_endereco = request.json()

                print(f"Rua: {data_endereco['logradouro']}")
                print(f"Bairro: {data_endereco['bairro']}")
                print(f"Estado: {data_endereco['uf']}""\n")
                TentardnvCep = int(input("Esta correto: ""\n""sim - 1""\n""Nao - 2""\n"))
                if TentardnvCep == 2:
                    return Endereco()
                LimparTela()
                Telinha()
            Nome()
            Nascimento()
            Genero()
            Endereco()
        def RegistrarCpf():
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
            LimparTela()   
            Telinha()
        def Email_Senha():
            def Email():
                VerifiEmail = '^[a-zA-Z0-9._]+[a-zA-Z0-9._]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
                email = input("Email: ")
                if re.search(VerifiEmail, email):
                    pass
                else:
                    print("Email Invalido!")
                    return Email()      
            def Senha():
                Novasenha = input("Digite uma senha de 6 Digitos: ")
                if len(Novasenha) != 6:
                    print("senha invalida, Digite novamente")
                    return Senha()
                LimparTela()
                return Cadastrojexistente()   #Ainda vou fazer
            Email()
            Senha()

        InformacoesPessoais()
        RegistrarCpf()
        NumeroTelefone()
        Email_Senha()
    NovoCadastro()
