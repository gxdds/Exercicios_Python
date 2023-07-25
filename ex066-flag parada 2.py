n = contador = soma = 0
while True:
    n = int(input('Digite um número (para parar digite 999): '))
    contador += 1
    if n == 999:
        break
    soma = (soma + n)
print(f'Você digitou {contador-1} números e a soma entre eles é {soma}')