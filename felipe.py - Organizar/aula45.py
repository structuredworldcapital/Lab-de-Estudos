from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opcaoes:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual � a sua jogada?'))
print('-=' * 11)
print('Computador jogou {}'.format(itens[jogador]))
print('Jogador jogou {}'.fomrat(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
  if jogador == 0
    print('EMPATE')
  elif jogador == 1:
    print('JOGADOR VENCE')
  elif jogador == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVALIDA!')
elif computador == 1: # computador jogou  PAPEL
if jogador == 0
    print('COMPUTADOR VENCE')
  elif jogador == 1:
    print('EMPATE')
  elif jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVALIDA!')
elif computador == 2: # computador jogou TESOURA
if jogador == 0
    print('JOGADOR VENCE')
  elif jogador == 1:
    print('COMPUTADOR VENCE')
  elif jogador == 2:
    print('EMPATE')
  else:
    print('JOGADA INVALIDA!')