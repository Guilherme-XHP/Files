import random

# Gera um número aleatório entre 0 e 5
numero_aleatorio = random.randint(0, 5)

# Solicita ao usuário para adivinhar o número
tentativa = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))

# Verifica se a tentativa do usuário está correta
if tentativa == numero_aleatorio:
    print("Parabéns! Você acertou o número.")
else:
    print(f"Você errou. O número escolhido pelo computador foi {numero_aleatorio}.")