soma = 0

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        soma += numero

print("A soma dos números pares é:", soma)