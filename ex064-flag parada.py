c = 1
contador = 0
somac = 0
while c != 999:
    c = int(input('Digite um numero inteiro: (digite 999 para parar)'))
    if c != 999:
        contador += 1
        somac = somac + c
print('Você inseriu {} números'.format(contador))
print('A soma dos numeros digitados é: {}'.format(somac))