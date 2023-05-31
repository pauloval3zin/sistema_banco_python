import datetime
menu = """

    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair

    => """

saldo = 0
limite = 500
extrato_deposito = []
extrato_saque = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        print("Deposito")
        valor_a_depositar = float(input("Digite um valor para deposito: "))

        if (valor_a_depositar > 0):
            saldo += valor_a_depositar
            extrato_deposito.append((valor_a_depositar, datetime.datetime.now()))
            print(f"Valor depositado: R${valor_a_depositar:,.2f}")
        else:
            print("Não foi possivel realizar o deposito.")
    
    elif opcao == "1":
        print("Sacar")
        valor_a_sacar = float(input("Qual valor para sacar? "))

        if valor_a_sacar <= saldo and numero_saques < LIMITE_SAQUES and valor_a_sacar <= limite and valor_a_sacar > 0:
            saldo -= valor_a_sacar
            extrato_saque.append((valor_a_sacar, datetime.datetime.now()))
            numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Não foi possível realizar o saque.")
    
    elif opcao == "2":
        print("Extrato")
        if not extrato_saque and not extrato_deposito:
            print("Não foi realizado nenhuma movimentação")
        else:
            print("Depositos: ")
            for valor, data_hora in extrato_deposito:
                data_formatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Valor: R${valor:,.2f} - Data/Hora {data_formatada}")
            
            print("Saques:")
            for valor_do_saque, data_hora in extrato_saque:
                data_formatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Valor: R${valor_do_saque:,.2f} - Data/Hora {data_formatada}")
            print(f"Saldo Atual: R${saldo:,.2f}")
    
    elif opcao == "3":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
