# Solicita a quantidade de km percorridos
km_percorridos = float(input("Digite a quantidade de km percorridos: "))

# Solicita a quantidade de dias de aluguel
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

# Calcula o preço a pagar
preco_km = km_percorridos * 0.15
preco_dias = dias_aluguel * 60
preco_total = preco_km + preco_dias

# Exibe o preço a pagar
print("O preço a pagar é: R$", preco_total)