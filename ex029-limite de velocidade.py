vel = int(input('Digite a sua velocidade'))
valor = (vel - 80)*7
if vel > 80:
    print('Você foi multado')
    print('Sua multa foi de R${}'.format(valor))
else:
    print('Ta dirigindo bem. Respeite os limites de velocidade.')