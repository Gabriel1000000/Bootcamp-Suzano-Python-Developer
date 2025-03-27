import os
print("****Bem vindo ao Banco Python****")

menu=""" 
    |****Menu do banco****|
    |    [0] Depósitar    |
    |    [1] Sacar        |
    |    [2] Extrato      |
    |    [3] Sair         |
    |*********************|
"""
saldo=0
limite=500
extrato=""
numero_saques=0
LIMITES_SAQUES=3

while True:
    # os.system("cls")
    print(menu)
    op=input("> ")

    if op=="0":
        print("Informe o valor do depódito")
        valor=float(input(">"))
        if valor>0:
            saldo+=valor
            extrato+=f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! Valor de depósito invalido!")
    
    elif op=="1":
        print("Informe o valor do Saque")
        valor=float(input("> "))
        if valor>saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
        elif valor>limite:
            print("Operação falhou! Valor pedido excedeu o limito permitido dessa conta!")
        elif numero_saques>=LIMITES_SAQUES:
            print("Operação falhou! Você já fez o maximo de saques permitidos dessa conta!")
        elif valor>0:
            saldo-=valor
            extrato+=f"Saque: R${valor:.2f}\n"
            numero_saques+=1
        else:
            print("Operação falhou! Valor de saque invalido!")

    elif op=="2":
        print("\n********************************EXTRATO********************************")
        print("Não foram realizados movimentações na conta." if not extrato else extrato)
        print(f"\n Salto da conta: R${saldo:.2f}")
        print("*************************************************************************")

    elif op=="3":
        break
    else:
        print('Selecione as opções mostradas no menu.')
        