menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """
saldo = 0
LIMITE = 500
extrato = ""
saque = 0
LIMITE_SAQUE = 3
num_saques = 0

while True:

    opção = input(menu)

    if opção == "d":
        print("Depósito")
        valor_dep = float(input("Insira o valor que você deseja depositar: "))

        if valor_dep > 0:
            saldo += valor_dep
            extrato +=  (f"Depósito = R$ {valor_dep:.2f}\n")
        else:
            print("Valor inválido! Tente novamente.")

    elif opção == "s":
        print("Saque")
        valor_saq = float(input("Insira o valor que você deseja sacar: "))

        if valor_saq > saldo:
            print("A operação não foi concluída! Você não tem saldo suficiente.")

        elif valor_saq > LIMITE:
            print("A operação não foi concluída! O valor excede o limite de saque.")

        elif num_saques >= LIMITE_SAQUE:
            print("A operação não foi concluída! O número de saques foi excedido.")

        elif valor_saq > 0:
            saldo -= valor_saq
            extrato +=  (f"Saque = R$ {valor_saq:.2f}\n")
            num_saques += 1

        else:
            print("Operação inválida, tente novamente!")

    elif opção == "e":
        print("========== EXTRATO ==========")
        print("Não há movimentações registradas" if not extrato else extrato)
        print(f"Saldo = R$ {saldo:.2f}")
        print("=============================")

    elif opção == "q":
        break

    else:
        print("Operação inválida, tente novamente!")
