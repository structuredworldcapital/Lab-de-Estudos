
def soma(a, b):    #def nomedafunção(variaveis):              #da pra fzr sem variaveis defnomedafunçao():
    print(f'A = {a} e B = {b}')
    s = a + b      #define oq vai acontecer com as variaveis  #ai sempre acontece a msm coisa qnd se usa a função
    print(f'A soma de A + B = {s}')       # a, b são chamados de parametros


#Programa Principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)



def contador(* num): #o * flexibiliza a quantidade de parametros basicamente pode colocar qnts quiser
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)



def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1


valores = [1,2,4,5,6,7]
dobra(valores)
print(valores)



def soma(* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)





























