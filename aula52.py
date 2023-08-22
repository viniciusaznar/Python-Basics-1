''' TIPO TUPLA

    #   Lista imutável: 
        Nenhum valor dentrod a tupla pode ser alterado. '''


''' Para criar uma tupla, basta adicionar mais de um valor
    literal a uma variável, separado por vírgurla,
    sem , OU COM parenteses, SEM chaves e SEM colchetes. '''


nomes = 'Marcos', 'Vinícius', 'Aznar'
print(type(nomes))


''' Transformando um 'tipo list' para um 'tipo tuple'. '''

nomes = tuple(nomes)