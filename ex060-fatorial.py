num = int(input('Digite o número que deseja saber o fatorial: '))
c = num
f = 1
while c > 0:
     print('{}'.format(c), end='')
     print('x' if c > 1 else '=', end = '')
     f *= c
     c -= 1
print('{}'.format(f))
