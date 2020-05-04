def somar(a=0,b=0,c=0):       #parametros opcionais
    s = a + b + c
    return s


r1 = somar(3,2,1)
r2 = somar(3,2)
r3 = somar(3)
r4 = somar()

print(f'Os resultados foram {r1}, {r2}, {r3} e {r4}')
