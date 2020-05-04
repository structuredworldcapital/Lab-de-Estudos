salario = float(input('Qual e p salario do funcionario? r$'))
if salario <= 1250:
  novo = salario + (salario * 15 / 100)
else:
  novo = salario + (salario * 10/100)
print('Quem ganhava r${} passa a ganhar r${} agora.'.format(salario, novo))