import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))

#para importar uma biblioteca inteira se usa import biblioteca
#para importar alguma função especifica da biblioteca se usa from biblioteca import função

#a diferença é que quando vc for usar a função, se vc importou a biblioteca inteira vc vai ter
#que escrever biblioteca.função

#se vc importou só a função especifica vc pode soh escrever o nome dela e usar
#função(variavel q vc quer usar ela)
