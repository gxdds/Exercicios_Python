lista1 = list()
listapar = list()
listaimpar = list()
while True:
    num = int(input('Digite o número que deseja adicionar na lista: '))
    lista1.append(num)
    ver = input('Caso deseja continuar, digite [S], caso deseja parar, digite qualquer outra coisa : ').upper().strip()[0]
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    if ver != 'S':
        break
print(f'A lista com todos os valores ficou: {lista1}')
print(f'A lista com os valores PARES ficou: {listapar}')
print(f'A lista com os valores IMPARES ficou: {listaimpar}')
