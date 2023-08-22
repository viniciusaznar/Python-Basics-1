''' DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES. '''

string = 'ABCD'
lista = ['Marcos', 'Vinícius', 1, 6.7, 'Aznar']
tupla = 'Python', 'é', 'legal.'

''' PEGANDO O ÚLTIMO ITEM DE UMA LISTA. '''

p, b, *_, u = lista
print(p, u)

''' PEGANDO O PENÚLTIMO ITEM DE UMA LISTA. '''

p, b, *_, p,     u = lista
print(p, u)

''' DESEMPACOTAMENTO EM CHAMADA DE FUNÇÕES. '''

for nome in lista:
    print(nome, end=' ')

    ''' DESEMPACOTAMENTO DIRETO NO PRINT. '''

print(*lista)
print(*string)
print(*tupla)

''' Ver cada lista-filho em linhas separadas. '''

salas = [
    # 0         1
    ['Marcos', 'Vinícius', ],  #   0
    # 0
    ['Aznar', ],                 #   1
    # 0     1
    ['da', 'Silva', (0, 1, 2, 3, 4)],           #   2
]

print(*salas, sep='\n')