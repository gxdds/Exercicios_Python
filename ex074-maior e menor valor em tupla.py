import random
random1 = random.randint(0,10)
random2 = random.randint(0,10)
random3 = random.randint(0,10)
random4 = random.randint(0,10)
random5 = random.randint(0,10)
t = (random1, random2, random3, random4, random5)
maior = menor = t[0]

for numero in t:
    if numero > maior:
        maior = numero
for numero in t:
    if numero < menor:
        menor = numero
print(f'Os números criados criados foram: {t}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

## modo mais rápido print(f'O maior número sorteado é {max(t)}')
## modo mais rápido print(f'O menor número sorteado é {min(t)}')