import random

quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

lista_composta = []

for _ in range(quantidade_jogos):
    jogo = []
    for _ in range(6):
        numero = random.randint(1, 60)
        jogo.append(numero)
    lista_composta.append(jogo)

print("Palpites gerados:")
for jogo in lista_composta:
    print(jogo)