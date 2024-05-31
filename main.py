extrato = 0
limite_valor_saque = 500.00
limite_qtd_saque = 3
num_saques = 0

while True:

    opcao = input("Escolha uma opção: \n"
                  "1 - Depósito\n"
                  "2 - Saque\n"
                  "3 - Extrato\n"
                  "0 - Sair\n")

    if opcao == "0":
        break

    elif opcao == "1":
        deposito = float(input("Digite o valor do seu depósito: "))
        if deposito < 0:
            deposito = 0
            print("Não é possível fazer o depósito, o depósito é de um valor negativo\n")
        else:
            extrato = extrato + deposito

            print("O valor do seu extrato é: R$", extrato, "\n")

    elif opcao == "2":

        valor_saque = float(input("Digite o valor do seu saque: "))
        if num_saques == limite_qtd_saque:
            print("Você não pode mais efetuar saques hoje o limite é de", limite_qtd_saque, "saques por dia")
        elif valor_saque > limite_valor_saque:
            print("Você não pode efetuar esse saque, pois o limite para um saque é de", limite_valor_saque, "\n")
        elif (extrato - valor_saque) < 0:
            print("Você não possui saldo o suficiente em conta\n")
        else:
            extrato = extrato - valor_saque
            num_saques += 1
            print("Seu novo saldo é R$", extrato, "\n")

    elif opcao == "3":
        print("O seu extrato é igual a R$", extrato, "\n")

    else:
        print("Opção inválida\n")
