pal = ('vasco','problema','militar','jogador','vela','distribuir')
vogal = ('a', 'e', 'i', 'o', 'u')
print(pal)

for p in pal:
    print(f'\nA palavra {p.upper()} possui como vogal: ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
