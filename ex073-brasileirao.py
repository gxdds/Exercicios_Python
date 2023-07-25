times = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino',
'Athletico-PR', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians',
'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print(f'Os 5 primeiros colocados do Brasileirão são: {(times[0:5])}')
print(f'Os 4 últimos colocados do Brasileirão são: {(times[-4:])}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('O gigante está na posição: {}'.format(times.index('Vasco da Gama')+1))
