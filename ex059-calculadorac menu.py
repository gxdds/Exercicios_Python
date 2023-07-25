num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
c = 0
res = 0
while c != 5:
    print('=-'*10)
    c = int(input('MENU:\n [1] SOMAR: \n [2] MULTIPLICAR: \n [3] MAIOR: \n [4] NOVOS NUMEROS: \n [5] SAIR DO PROGRAMA. \n'))
    if c == 1:
        res = num1+num2
        print('Você escolheu {}. A soma dos números é: {}.'.format(c,res))
    elif c == 2:
        res = num1*num2
        print('Você escolheu {}. A multiplicação dos números é: {}.'.format(c,res))
    elif c == 3 and num1 > num2:
        print('O maior número é o primeiro número escolhido: {}'.format(num1))
    elif c == 3 and num1 < num2:
        print('O maior número é o segundo número escolhido: {}'.format(num2))
    elif c == 3 and num1 == num2:
        print('Os números são iguais')
    elif c == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
    else:
        print('Digite um valor válido.')

print('Programa finalizado.')


