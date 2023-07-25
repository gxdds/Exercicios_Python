sexo = ''
masc = 'M'
fem = 'F'
while sexo != masc and sexo != fem:
    sexo = input('Digite se seu sexo é Feminino [F] ou Masculino [M]: ').upper()
    if sexo == masc:
        print('Seu sexo é Masculino')
    elif sexo == fem:
        print('Seu sexo é Feminino')
    else:
        print('Digite um sexo valido')
print('fim')



