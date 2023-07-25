stop = 'S'
c = 1
cidd = 0
chome = 0
ccuie = 0
while True:
    idd = int(input(f'Digite a idade da {c}° pessoa: '))
    sex = input(f'Digite o sexo da {c}° pessoa [F/M]: ').upper().strip()[0]
    stop = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if idd > 18:
        cidd +=1
    if sex in 'Mm':
        chome +=1
    if sex in 'Ff' and idd < 20:
        ccuie +=1
    if stop != 'S':
        break
    c += 1
print(f'{cidd} é a quantidade de pessoas maiores de 18 anos cadastradas.')
print(f'{chome} é a quantidade de homens cadastrados.')
print(f'{ccuie} é a quantidade de mulheres que possuem menos de 20 anos.')
print('Você digitou "N" ou uma tecla diferente, o programa foi finalizado.')
