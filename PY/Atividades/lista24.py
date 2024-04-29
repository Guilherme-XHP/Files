from datetime import date

maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Informe o ano de nascimento da pessoa {i}: "))
    idade = date.today().year - ano_nascimento
    
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Quantidade de pessoas maiores de idade: {maiores}")
print(f"Quantidade de pessoas menores de idade: {menores}")