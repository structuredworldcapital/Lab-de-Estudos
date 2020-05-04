n = int(input('Digite um numero?'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.A raiz quadrada de {} e igual a {}.'.format(n, t, n, r))
#ou pode ser dito da seguinte forma print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.A raiz quadrada de {} e igual a {}.'.format(n, (n*3), n, pow(n, (1/2))))
