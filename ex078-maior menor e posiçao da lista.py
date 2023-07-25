lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
print(lista)
for p, n in enumerate(lista):
    if max(lista) == n:
        print(f'O maior valor digitado na lista é {max(lista)} e sua posição é {p+1}')
    if min(lista) == n:
        print(f'O menor valor digitado na lista é {min(lista)} e sua posição é {p+1}')
