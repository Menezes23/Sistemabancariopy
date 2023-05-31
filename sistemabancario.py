menu = """
 [d] depositar
 [s] sacar
 [e] extrato
 [q] sair\n
 =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito :R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("operação falhou, valor invalido")

    if opcao == "s":
        valor = float(input("informe o valor do saque:"))
        excedeu_valor = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_valor:
            print("operação falhou, saldo insuficiente")
        elif excedeu_limite:
            print("operação falhou, limite insuficiente")
        elif excedeu_saques:
            print("operação falhou, numero de saques excedido")
        elif saldo > 0:
            saldo -= valor
            extrato += f"Saque :R${valor:.2f}\n"
        else:
            print("operação falhou, valor invalido")
    elif opcao == "e":
        print("\n===============EXTRATO=================")
        print("Não fora realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo:R${saldo}")
        print("========================")
    elif opcao == "q":
        break
    
    else:
        print("operação invalida, por favor selecione uma opção")
        

