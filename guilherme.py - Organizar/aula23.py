try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print(f'Tivemos um problema com os dados que vc digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, Muito obrigado')

'''except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')'''

