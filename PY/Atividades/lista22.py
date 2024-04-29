# Inicializando as variáveis de contagem
maiores_dezoito = 0
homens = 0
mulheres_menos_vinte = 0

while True:
    # Lendo os dados da pessoa
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")

    # Verificando as condições
    if idade > 18:
        maiores_dezoito += 1
    if sexo.upper() == "M":
        homens += 1
    if sexo.upper() == "F" and idade < 20:
        mulheres_menos_vinte += 1

    # Perguntando se deseja continuar
    continuar = input("Deseja cadastrar mais uma pessoa? (S/N): ")
    if continuar.upper() != "S":
        break

# Mostrando os resultados
print(f"Quantidade de pessoas com mais de 18 anos: {maiores_dezoito}")
print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_vinte}")