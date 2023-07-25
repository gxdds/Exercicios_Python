ext = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite o número entre 0 e 20 que deseja saber por extenso: '))
while True:
    if n >= 0 and n <= 20:
        print(ext[n])
        break
    else:
        n = int(input('Digite o número VÁLIDO entre 0 e 20 que deseja saber por extenso: '))
