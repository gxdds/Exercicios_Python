preço = float(input('Qual é o preço do produto? '))
desc = preço/100*5
preço = preço - desc
print('O produto com desconto ficou R$:{}'.format(preço))
### desconto 5%



salario = float(input('Qual o seu salário?'))
aumento = int(input('Quantos % de aumento você recebeu?'))
porcentagem = salario/100*aumento
salariofinal = salario + porcentagem
print('Já que você recebeu {}% de aumento, seu salário passou de R${} para R${}'.format(aumento,salario,salariofinal))