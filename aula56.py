''' SLIPT E JOIN (Com list ou str)  

        #   split   ->  divide uma string
        #   join    ->  une strings.    '''

frase = 'Olha só, que coisa interessante'

''' Método de String .split sem parâmetro:  

    #   Separa as palavras de uma string pelos espaços
        e cria uma nova lista com elas.  '''

lista_de_palavras = frase.split()
print(lista_de_palavras)

''' .slipt(',') 

    #   Quebra a string nas vírgulas e cria uma nova lista
        com as partes. '''

lista_de_palavras = frase.split(', ')

lista_frases = frase.split(',')

''' MÉTODO .strip() 

    #   Sem parâmetros, remove os espaços do começo e final de uma string. '''

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

print(lista_frases)

''' MÉTODO .rstrip() 

    #   Remove os espaços da direita de uma string. '''

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].rstrip())

print(lista_frases)

''' MÉTODO .lstrip() 

    #   Remove os espaços da direita de uma string. '''

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].lstrip())

print(lista_frases)

''' CORRIGINDO PROBLEMAS DE ESPAÇOS EM UMA STRING.

    #   Mantenha sempre o valor original de um mutável em uma variável,
        para consultas desejadas posteriores. '''

lista_frases_cruas = frase.split(',')

lista_frases_fixed = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases_fixed.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases_fixed)

''' MÉTODO  .join()

    #   'variável list' = 'separador'.join('Conteúdo a ser inserido
        na variável list'). '''

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)