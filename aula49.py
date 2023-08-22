''' DADOS MUTÁVEIS:

        #   Cuidado com dados mutáveis.

        #   =   ->  Copia o valor para uma variável (valor imutável).
        #   =   ->  Também aponta o mesmo valor na memória (mutável). '''



''' APENAS APONTANDO PARA UM VALOR NA MEMÓRIA. '''


lista_a = ['Liz', 'Marcos', 1, True, 2.0]


''' A lista_b apenas apontará o valor na memória da lista_a,
    SEM DUPLICAR o seu valor, ou criar uma nova lista. 
    
    #   Qualquer modificação nos itens da lista_a será
        acontecerá, também, na lista_b. 
    #   Pois, a lista_b apenas aponta o valor da lista_a. '''


lista_b_aponta_memoria = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b_aponta_memoria)


lista_1 = ['Azul', True, 1, 3.5]


''' COPIANDO OS VALORES DE UMA LISTA PARA OUTRA LISTA.  '''


lista_2_copia_lista_1 = lista_1.copy()


del lista_1[-3]
print(lista_1)
print(lista_2_copia_lista_1)