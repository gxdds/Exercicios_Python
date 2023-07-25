n = 0
tab = 1
while True:
    print('-=' * 9)
    n = int(input('Você quer saber a tabuada de qual número? Digite número negativo para desligar o programa. '))
    print('-=' * 9)
    if n < 0:
        break
        print('-='*9)
    for c in range (1,11):
        tab = n*c
        print(f'{n}x{c}={tab}')
print('Programa ENCERRADO.')