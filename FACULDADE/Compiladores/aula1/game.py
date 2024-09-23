import random

num = random.randrange(1, 100)

ganhou = False

while not ganhou:
    palpite = int(input('Diga seu palpite: '))
    if palpite == num:
        print(f'Acertou, o numero era: {num}')
        ganhou = True
    elif palpite < num:
        print(f'Errado, meu numero e maior que: {palpite}')
    else:
        print(f'Errado, meu numero e menor que: {palpite}')
    