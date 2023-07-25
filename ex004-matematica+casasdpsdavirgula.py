n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo valor '))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div1 = n1 // n2
pot = n1 ** n2
print('A soma dos números é: {};\n subtração: {};\n multiplicação: {};\n divisão: {:.3f};\n divisao inteira: {};\n potência: {}'
      .format(s, sub, mult, div, div1, pot))

#### na divisao o :.3f ta colocando quantas casas decimais vao ter dps da ,
#### \n pula linha
#### pra nao quebrar, no final do print bota , end =''