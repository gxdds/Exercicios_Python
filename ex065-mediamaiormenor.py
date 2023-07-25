resp = 'S'
maior = menor = soma = c = media = 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    c = c + 1
    soma = soma + n
    media = soma/c
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Deseja continuar? [S/N]: ').upper().strip()[0]
print(f'O maior valor digitado é: {maior} e o menor {menor}')
print('A soma dos valores digitados é: {}'.format(soma))
print('A média dos valores digitados é: {}'.format(media))
print('Fim.')
