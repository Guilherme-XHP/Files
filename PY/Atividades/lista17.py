pessoas = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa (ou "sair" para encerrar): ')
    
    if pessoa['nome'].lower() == 'sair':
        break
    
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    
    pessoas.append(pessoa)
    soma_idade += pessoa['idade']

quantidade_pessoas = len(pessoas)
media_idade = soma_idade / quantidade_pessoas

mulheres = [pessoa for pessoa in pessoas if pessoa['nome'].lower().endswith('a')]
acima_media = [pessoa for pessoa in pessoas if pessoa['idade'] > media_idade]

print(f'Foram cadastradas {quantidade_pessoas} pessoas.')
print(f'A média de idade é {media_idade:.2f}.')
print('Lista de mulheres:')
for mulher in mulheres:
    print(mulher['nome'])
print('Lista de pessoas com idade acima da média:')
for pessoa in acima_media:
    print(pessoa['nome'])