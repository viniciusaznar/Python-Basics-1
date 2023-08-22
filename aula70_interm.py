''' RETORNO DE VALORES DAS FUNÇÕES. '''

variavel = print('Marcos')
print(variavel)

def soma_a(x, y):
    ...

soma1 = soma_a(2, 2)
soma2 = soma_a(3, 3)

variavel_1 = soma_a(1, 2)
print(variavel_1)

def soma_b(x, y):
    if x > 10:
        return [10, 20]
    return x + y

soma1 = soma_b(2, 2)
soma2 = soma_b(3, 3)

print(soma1)
print(soma2)
print(soma_b(11, 55))