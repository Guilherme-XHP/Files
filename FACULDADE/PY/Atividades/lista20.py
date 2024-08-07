def calcular_juros(deposito_inicial, taxa_juros):
    saldo = deposito_inicial
    total_juros = 0

    for mes in range(1, 25):
        juros = saldo * (taxa_juros / 100)
        saldo += juros
        total_juros += juros
        print(f"Mês {mes}: Saldo = R${saldo:.2f}, Juros = R${juros:.2f}")

    print(f"Total ganho com juros no período: R${total_juros:.2f}")

deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

calcular_juros(deposito_inicial, taxa_juros)