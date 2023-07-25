lista = list()
while True:
    c = int(input('Digite o valor que deseja adicionar na lista: '))
    if c in lista:
        print('Este número já está na lista, insira outro.')
    else:
        lista.append(c)
        lista.sort()
    a = input('Deseja continuar? [S/N]: ').upper().strip()
    if a in 'N':
        break
    if a != 'S':
        break

print(f'A lista ordenada, sem repetir valores é: {lista}')
