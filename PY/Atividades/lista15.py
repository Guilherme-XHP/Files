import datetime

def cadastrar_pessoa():
    pessoa = {}
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['ano_nascimento'] = int(input('Digite o ano de nascimento: '))
    pessoa['ctps'] = int(input('Digite o número da carteira de trabalho (0 se não tiver): '))

    if pessoa['ctps'] != 0:
        pessoa['ano_contratacao'] = int(input('Digite o ano de contratação: '))
        pessoa['salario'] = float(input('Digite o salário: '))

    pessoa['idade'] = datetime.datetime.now().year - pessoa['ano_nascimento']
    pessoa['anos_aposentadoria'] = 65 - (datetime.datetime.now().year - pessoa['ano_contratacao'])

    return pessoa

pessoa = cadastrar_pessoa()
print(pessoa)