import os
from datetime import datetime


def limpar_terminal():
    os.system("clear")


def data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        limpar_terminal()

        valor_deposito = 0.00
        date_time = data_hora()

        while True:

            valor_deposito = float(input("Informe o valor do depósito: "))

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato.append(f"D - {date_time} - R$ {valor_deposito:.2f}")
                limpar_terminal()
                break
            else:
                limpar_terminal()
                print(f"Valor informado deve ser maior que zero!\n")

    elif opcao == "s":
        limpar_terminal()

        if numero_saques < LIMITE_SAQUES:
            date_time = data_hora()

            while True:
                print("Digite zero para encerrar operação.\n")
                
                valor_saque = float(input("Informe o valor do saque:\n"))

                saldo_suficiente = valor_saque <= saldo
                limite_saque = valor_saque <= limite
                saque_maior_zero = valor_saque > 0

                if saldo_suficiente and limite_saque and saque_maior_zero:
                    saldo -= valor_saque
                    extrato.append(f"S - {date_time} - R$ {valor_saque:.2f}")
                    numero_saques += 1
                    break
                elif not saldo_suficiente:
                    limpar_terminal()
                    print(
                        f"Saldo R$ {saldo:.2f} insuficiente para saque R$ {valor_saque:.2f}.\n"
                    )
                elif valor_saque == 0:
                    limpar_terminal()
                    break
                elif not limite_saque:
                    limpar_terminal()
                    print(
                        f"Limite por saque excedido, limite atual é R$ {limite:.2f} por saque.\n"
                    )
                elif not saque_maior_zero:
                    limpar_terminal()
                    print(f"Valor do saque deve ser maior que zero!\n")

                else:
                    limpar_terminal()
                    print("Opção inválida.\n")
        else:
            print("Limite de saques excedido. Tente novamente amanhã.")

    elif opcao == "e":
        limpar_terminal()

        print("Extrato".center(16, "#") + "\n")

        for line in extrato:
            print(line)

        print(f"\nSaldo atual: R$ {saldo:.2f}. \n")

    elif opcao == "q":
        limpar_terminal()
        print("Encerrando o sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
