from random import randint
from time impor sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5.Tente advinhar...')
print('-=-' * 20)
jogador = itn(input('Em que numero eu pensei?')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
  print('PARABENS! Voce conseguiu me vencer!')
else:
  print('GANHEI!Eu pensei no numero {} e nao no {}!'.fomrat(computador, jogador))