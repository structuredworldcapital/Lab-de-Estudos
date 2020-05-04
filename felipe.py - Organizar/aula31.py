distancia = float(input('Qual e a distancia de sua viagem?'))
print('Voce esta prestes a comecar uma viaagem de {}km.'.format(distancia))
if distancia <= 200:
  preco = distancia * 0.50
else:
  preco = distancia * 0.45
print('E o preco de sua passagem sera de R${}'.format(preco))
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45