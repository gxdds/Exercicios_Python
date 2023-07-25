import random
sorteio = random.randint(0, 5)
guess = int(input('Digite o valor que você acha que foi sorteado: '))
if guess == sorteio:
    print('Você acertou')
else:
    print('Você errou, o número sorteado era {}'.format(sorteio))