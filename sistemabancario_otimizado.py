#função de depósito
def deposito(saldo, extrato, valor_dep):
    if valor_dep > 0:
        saldo += valor_dep
        extrato += f"Depósito = R$ {valor_dep:.2f}\n"
    else:
        print("Valor inválido! Tente novamente.")
    return saldo, extrato

#função de saque
def saque(saldo, extrato, num_saques, valor_saq, LIMITE, LIMITE_SAQUE):
    if valor_saq > saldo:
        print("A operação não foi concluída! Você não tem saldo suficiente.")
    elif valor_saq > LIMITE:
        print("A operação não foi concluída! O valor excede o limite de saque.")
    elif num_saques >= LIMITE_SAQUE:
        print("A operação não foi concluída! O número de saques foi excedido.")
    elif valor_saq > 0:
        saldo -= valor_saq
        extrato += f"Saque = R$ {valor_saq:.2f}\n"
        num_saques += 1
    return saldo, extrato, num_saques

#função de visualização de extrato
def extrato_conta(saldo, extrato=None):
    if extrato is None:
        extrato = ""
    
    print("========== EXTRATO ==========")
    print("Não há movimentações registradas" if not extrato else extrato)
    print(f"saldo = R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    cpf = input("insira o seu cpf (somente números): ")
    usuario = filtrar_user(cpf, usuarios)
    
    if usuario:
        print("Este cpf já foi registrado!")
        return
    
    nome = input("insira seu nome completo: ")
    data = input("insira sua data de nascimento no formato (dd-mm-aaaa): ")
    endereco = input("insira seu endereço no formato (logradouro, numero - bairro - cidade/sigla do estado): ")
    
    usuarios.append({"cpf": cpf, "nome": nome, "data de nascimento": data, "endereço": endereco})
    print("Seu usuário foi criado!")

def filtrar_user(cpf, usuarios):
    filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtrado[0] if filtrado else None

def criar_conta(agencia, num_contas, usuarios):
    cpf = input("insira o CPF do Usuário: ")
    usuario = filtrar_user(cpf, usuarios)
    
    if usuario:
        print("Conta registrada!")
        return {"agencia": agencia, "numero de conta": num_contas, "usuarios": usuario}
    
    print("Usuário não encontrado!")

def main():
    #constantes utilizadas
    LIMITE = 500
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    #variaveis
    saldo = 0
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []
    
    while True:
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [u] Registrar Usuário
        [c] Criar Conta
        
        ==> """
        
        opcao = input(menu)
        
        if opcao == "d":
            print("Depósito")
            valor_dep = float(input("Insira o valor que você deseja depositar: "))
            saldo, extrato = deposito(saldo, extrato, valor_dep)
            
        elif opcao == "s":
            print("Saque")
            valor_saq = float(input("Insira o valor que você deseja sacar: "))
            saldo, extrato, num_saques = saque(saldo=saldo, extrato=extrato, num_saques=num_saques, valor_saq=valor_saq, LIMITE=LIMITE, LIMITE_SAQUE=LIMITE_SAQUE)
        
        elif opcao == "e":
            extrato_conta(saldo, extrato)
        
        elif opcao == "u":
            criar_usuario(usuarios)
        
        elif opcao == "c":
            num_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, num_contas, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, tente novamente!")

if __name__ == "__main__":
    main()
