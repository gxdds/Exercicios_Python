c = 0
lista = list()
while True:
    num = int(input('Digite o número que deseja adicionar na lista: '))
    lista.append(num)
    ver = input('Caso deseja continuar, digite [S], caso deseja parar, digite qualquer outra coisa : ').upper().strip()[0]
    c += 1
    if ver != 'S':
        break
if 5 in lista:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado.')

lista.sort(reverse=True)
print('A lista em ordem decrescente é: ', end='')
print(lista)
print(f'A lista tem {len(lista)} números.')
