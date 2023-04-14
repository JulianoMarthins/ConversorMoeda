def aumentar(preco=0, taxa=0): # Retorna o acrescimo de uma porcentagem do valor
    resposta = preco + (preco * taxa / 100)
    return moeda(resposta)


def diminuir(preco=0, taxa=0): # Retorna a subtração de uma porcentagem do valor
    resposta = preco - (preco * taxa / 100)
    return moeda(resposta)


def dobro(preco=0): # Retorna o dobro do valor
    resposta = preco * 2
    return moeda(resposta)


def metade(preco=0): # Retorna a metade do valor
    resposta = preco / 2
    return moeda(resposta)


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace(',', '.')

def resumo(preco=0, taxaaum=10, taxared=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'Com {taxaaum}% de aumento: {aumentar(preco, taxaaum)}')
    print(f'Com {taxared}% de redução: \t{diminuir(preco, taxared)}')
    print('-' * 30)