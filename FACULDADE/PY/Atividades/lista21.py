numeros = []
soma = 0

while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))
    if numero == 999:
        break
    numeros.append(numero)
    soma += numero

quantidade_numeros = len(numeros)

print("Quantidade de números digitados:", quantidade_numeros)
print("Soma dos números digitados:", soma)