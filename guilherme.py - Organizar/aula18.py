teste = list() #mesma coisa que teste = [] cria uma lista vazia
teste.append('Guilherme')
teste.append(40)

galera = list()
galera.append(teste[:]) #da pra add uma lista em outra lista, a lista teste ta dentro da lista galera

teste[0] = 'Maria' #mudei as informações de teste
teste[1] = 22
galera.append(teste[:]) #é preciso criar uma cópia com [:] senão as duas listas dentro de galera ficam iguais
print(galera)





galera = [['João',19], ['Ana',33],['Joaquim',13],['Maria',45]]
print(galera[0]) #printar o primeiro item da lista galera no caso João,19
print(galera[0][0])#printar o primeiro item do primeiro item da lista galera no caso só João
print(galera[2][1])
for pessoa in galera:
    print(pessoa)

for pessoa in galera:
    print(pessoa[0]) #só printa o primeiro item de cada pessoa no caso nome

for pessoa in galera:
    print(pessoa[1]) #printa só a idade

for pessoa in galera:
    print('{} tem {} anos de idade'.format(pessoa[0],pessoa[1]))








galera = list()
dado = list()
totmaior = totmenor = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #se não fizer uma cópia na hora q der clear dado a lista galera tbm é apagada
    dado.clear()


for pessoa in galera:
    if pessoa[1] >= 18:
        print('{} é maior de idade'.format(pessoa[0]))
        totmaior += 1
    else:
        print('{} é menor de idade'.format(pessoa[0]))
        totmenor += 1

print('Temos {} maiores e {} menores de idade'.format(totmaior, totmenor))
















