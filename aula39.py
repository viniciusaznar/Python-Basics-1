'''
# ITERANDO (NAVEGANDO) STRINGS COM O 'WHILE'
'''

#       012345
nome = 'Marcos'     #Iteráveis
#      -654321

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome = '*'
print(novo_nome)