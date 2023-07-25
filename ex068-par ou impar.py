import random
sorteio = random.randint(0, 11)
par = ''
impar = ''
res = 0
cont = 0
while True:
    print('Vamos jogar PAR ou IMPAR?')
    n = int(input('Diga um número: '))
    poui = input('Par ou Impar? [P/I]: ').upper().strip()[0]
    res = n + sorteio
    if res % 2 == 0 and poui in 'Pp':
        print(f'Você ganhou! Você jogou --> {n} e o computador -->{sorteio}, logo o resultado foi {res} que é PAR! ')
        cont += 1
        if cont > 1:
            print(f'Você está na sua {cont}° vitoria consecutiva')
        else:
            print('Você ganhou apenas 1 partida. Tente uma win streak!!!')
    if res % 2 == 0 and poui in 'Ii':
        print(f'Você perdeu! Você jogou --> {n} e o computador -->{sorteio}, logo o resultado foi {res} que é PAR! ')
        break
    if res % 2 == 1 and poui in 'Pp':
        print(f'Você perdeu! Você jogou {n} e o computador {sorteio}, logo o resultado foi {res} que é IMPAR! ')
        break
    if res % 2 == 1 and poui in 'Ii':
        print(f'Você ganhou! Você jogou {n} e o computador {sorteio}, logo o resultado foi {res} que é IMPAR! ')
        cont += 1
        if cont > 1:
            print(f'Você está na sua {cont}° vitoria consecutiva')
        else:
            print('Você ganhou apenas 1 partida. Tente uma win streak!!!')
print('Fim da sua sequência. Você perdeu.')
