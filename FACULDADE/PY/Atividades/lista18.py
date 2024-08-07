# Lista para armazenar os dados das pessoas
pessoas = []

# Loop para ler os dados das 4 pessoas
for i in range(4):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")

    # Adiciona os dados da pessoa à lista
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

# Calcula a média de idade do grupo
soma_idades = sum(pessoa["idade"] for pessoa in pessoas)
media_idade = soma_idades / len(pessoas)

# Encontra o homem mais velho
homens = [pessoa for pessoa in pessoas if pessoa["sexo"] == "M"]
homem_mais_velho = max(homens, key=lambda pessoa: pessoa["idade"])["nome"]

# Conta quantas mulheres têm menos de 20 anos
mulheres_jovens = len([pessoa for pessoa in pessoas if pessoa["sexo"] == "F" and pessoa["idade"] < 20])

# Imprime os resultados
print("Média de idade do grupo:", media_idade)
print("Nome do homem mais velho:", homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", mulheres_jovens)