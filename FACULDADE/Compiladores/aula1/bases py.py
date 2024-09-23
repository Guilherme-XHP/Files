idade = input('Insira sua idade: ')
nome = input('Insira seu nome: ')
salario = float(input('Insira seu salario: '))

if salario <= 3000:
    print(f'Seu nome e: {nome}/n tem {idade} anos /n eu recebe por mes um total de R${salario}.')
else:
    print(f'O seu mentiroso do caralho, tu nn recebe R${salario} nn')