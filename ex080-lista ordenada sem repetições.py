lista = list()
while True:
    c = int(input('Digite o valor que deseja adicionar na lista: '))
    posicao = 0
    while posicao < len(lista) and c > lista[posicao]:
        posicao +=1

    lista.insert(posicao, c)

    if len(lista) == 5:
        break

print(f'A lista ordenada em ordem crescente é: {lista}')