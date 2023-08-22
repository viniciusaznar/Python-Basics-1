''' LISTA DE LISTAS E SEUS ÍNDICES.  '''

salas = [
    # 0         1
    ['Marcos', 'Vinícius', ],  #   0
    # 0
    ['Aznar', ],                 #   1
    # 0     1
    ['da', 'Silva', (0, 1, 2, 3, 4)],           #   2
]

# ''' Acessando os índices da 'lista-pai' e 'listas-filho'. 

#     #   list['índice da lista-pai']['índice da lista-filho'. '''

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][1])
# print(salas[2][2][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)