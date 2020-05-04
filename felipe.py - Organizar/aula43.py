peso = float(intput('Qual e o sue peso? (kg)'))
altura = float(input('Qual e sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {}'.format(imc))
if imc < 18.5:
  print('Voce esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
  print('PARABENS, voce esta na faixa do PESO NORMAL')
elif 25 <= imc < 30:
  print('Voce esta SOBREPESO')
elif 30 <= imc < 40:
  print('Voce esta em OBESIDADE, cuidade!')
elif imc >= 40
  print('Voce esta OBESIDADE MORBIDA, cuidado!')
