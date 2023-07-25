n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
t = (n1, n2, n3, n4)
par = 0
print(t)
print(f'O número 9 aparece {(t.count(9))} vez(es)')
if 3 in t:
    print(f'O 3 aparece na posição {t.index(3)+1}')
else:
    print('O número 3 não foi digitado.')
print('Os valores pares digitados são: ', end = ' ')
for n in t:
    if n % 2 == 0:
        print(n, end = ' ')



