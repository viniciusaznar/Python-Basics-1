# Operadores in e not in
# strings são iteráveis
# = pode-se navegar através delas

# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# in
# print('á' in nome)
# print('z' in nome)
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# # in not
# print('á' not in nome)
# print('z' not in nome)
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')