#tuplas = () imutavéis
#listas = [] mutavéis e da pra botar uma dentro da outra
#dicionários = {} tipo uma lista só que da pra nomear o indice não ficar usando 01234

pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': '19'}
print(pessoas['nome']) #printa Guilherme
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #primeira vez que to usando o novo modo de
                                                          #formatação kkk, não esquecer de colocar "indice"
                                                          #não funciona 'indice'
pessoas['nome'] = 'Leandro' #assim que se modifica
pessoas['peso'] = 72.4 #da pra add um novo indice com valor tbm


print(pessoas.keys()) #printa os indices
print(pessoas.values()) #printa os valores dos indices que nesse caso é Guilherme M 19
print(pessoas.items()) #printa os indices com os valores, nome: Guilherme etc

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)




estado = dict() #mesma coisa que estado = {}
brasil = list() #mesma coisa que brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #nao da pra fazer copia de um dicionário fznd [:]

print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()















