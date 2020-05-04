'''cont = 1
while cont <= 10:
    print(cont)
    cont = cont + 1
print('Acabou')'''

# while True: realiza o comando infinitamente, só para com break

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print('A soma vale {}'.format(s))