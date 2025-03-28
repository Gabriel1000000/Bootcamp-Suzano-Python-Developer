import os
import textwrap
print("****Bem vindo ao Banco Python****")

menu=""" 
    |****Menu do banco****|
    |    [0] Depósitar    |
    |    [1] Sacar        |
    |    [2] Extrato      |
    |    [3] Sair         |
    |*********************|
"""

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato+=f"Depósito: R${valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
       print("Operação falhou! Valor de depósito invalido!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente!")

    elif valor > limite:
        print("Operação falhou! Valor pedido excedeu o limito permitido dessa conta!")

    elif numero_saques >= limite_saques:
        print("Operação falhou! Você já fez o maximo de saques permitidos dessa conta!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n*** Saque realizado com sucesso! ***")

    else:
        print("Operação falhou! Valor de saque invalido!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n********************************EXTRATO********************************")
    print("Não foram realizados movimentações na conta." if not extrato else extrato)
    print(f"\n Salto da conta: R${saldo:.2f}")
    print("*************************************************************************")

   
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    print("Informe a data de nascimento (dd-mm-aaaa):")
    data_nascimento = input("> ")
    print("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")
    endereco = input("> ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("*** Usuário criado com sucesso! ***")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        # os.system("cls")
        print(menu)
        op=input("> ")

        if op=="0":
            print("Informe o valor do depódito")
            valor=float(input(">")) 
            saldo, extrato = depositar(saldo, valor, extrato)   
        elif op=="1":
            print("Informe o valor do Saque")
            valor=float(input("> "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif op=="2":
            exibir_extrato(saldo, extrato=extrato)
        elif op == "nu":
            criar_usuario(usuarios)

        elif op == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif op == "lc":
            listar_contas(contas)
        elif op=="3":
            break
        else:
            print('Selecione as opções mostradas no menu.')
        

 


if __name__ == "__main__":
    main()