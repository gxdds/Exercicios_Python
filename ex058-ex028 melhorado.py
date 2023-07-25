import random
sorteio = random.randint(0, 10)
guess = 0
c = 0
while guess != sorteio:
    guess = int(input('Digite o valor que você acha que foi sorteado: '))
    if guess == sorteio:
        print('Você acertou, o número sorteado era mesmo o {}'.format(guess))
    else:
        c += 1
        print('Tente novamente')
print('Você precisou de {} tentativas'.format(c))
