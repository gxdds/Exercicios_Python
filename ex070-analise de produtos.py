stop = 'S'
tot = 0
contcaro = 0
contprod = 1
nome_menor = ''
preco_menor = float('inf')
while True:
    nome = input(f'Digite o nome do produto {contprod}: ')
    preço = float(input(f'Digite o preço do produto{contprod}: R$'))
    stop = input('Deseja adicionar mais produtos? [S/N]: ').upper()
    tot = tot + preço
    contprod +=1
    if preço > 1000:
        contcaro +=1
    if preço < preco_menor:
        nome_menor = nome
        preco_menor = preço
    if stop != 'S':
        break
print(f'{contcaro} é a quantidade de itens mais caros que R$1000.00 ')
print(f'O total gasto na compra é de R${tot:.2f}')
print(f'O nome do produto mais barato é {nome_menor} custando R${preco_menor:.2f}.')
