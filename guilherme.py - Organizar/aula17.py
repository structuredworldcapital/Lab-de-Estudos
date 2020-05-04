#tuplas são imutaveis, listas não

num =[2,5,9,1]
num[2]= 3 #num[posição que vc quer trocar] = oq vc quer colocar no lugar
print(num)
num.append(7)#num.append(add oq vc quiser no final da lista)
num.sort() #num.sort poe em ordem
num.insert(2,0) #num.insert(posição ,valor a ser inserido)
num.pop()#num.pop(oq vc quer excluir da lista) se não colocar nada apaga o ultimo valor da lista

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)
print('Essa lista tem {} elementos'.format(len(num)))
print('-'*20)


valores = []

'''valores.append(5) #para vc add valores para lista vazia
valores.append(9)
valores.append(4)'''

for cont in range(0,5): #para contagem de 0 até 5
    valores.append(int(input('Digite um valor: '))) #o usuario faz a lista

print(valores)
for c,v in enumerate(valores):
    print('Na posição {} encontrei o valor {}'.format(c,v))

print('='*40)
a = [2, 3, 4, 7]
b = a[:] #ASSIM Q SE FAZ UMA CÓPIA DA LISTA
b[2] = 8
print('Lista A: {}'.format(a))
print('Lista B {}'.format(b))






