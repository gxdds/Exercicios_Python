produtos = ('Mouse', 30, 'Teclado', 30, 'Headset', 50, 'Fone Bluetooth', 30, 'Monitor', 100)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:.>7.2f}')

print('-' * 40)
