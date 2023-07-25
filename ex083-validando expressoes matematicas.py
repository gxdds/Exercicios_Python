lista = list(input('Informe sua expressão: '))
if lista.count('(') != lista.count(')'):
    print('Está faltando fechar um parêntesis não acha?')
else:
    print('Sua expressão está correta')