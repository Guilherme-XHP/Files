import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    # Obter a escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    
    # Verificar se a escolha do usuário é válida
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Tente novamente.")
        return
    
    # Gerar a escolha aleatória do computador
    escolha_computador = random.choice(opcoes)
    
    # Mostrar as escolhas
    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")
    
    # Verificar o resultado do jogo
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

# Chamar a função para jogar
jogar()