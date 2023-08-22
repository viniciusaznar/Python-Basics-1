'''LISTAS EM PYTHON

    #   Tipo list -> mutável.
    #   Suporta vários valores de qualquer tipo.
    #   Conhecimentos reutilizáveis -> índices e fatiamento. '''


lista = []


''' MÉTODOS ÚTEIS: '''


''' append  -> Adiciona um item ao final da lista. '''


lista.append('Marcos')


''' insert  ->  Adiciona um item no índice escolhido da lista.
            #   lista.insert(número do índice, valor a ser inserido). '''


lista.insert(0, 100)


''' pop     ->  Remove o item final da lista, ou do índice escolhido. 
            #   lista.pop(número do índice). '''


lista.pop()


''' del     -> Apaga um índice. '''


del lista[-1]



''' clear   -> Limpa a lista. '''



lista.clear()



''' extend  -> Extende a lista. '''
''' + -     -> Concatena listas. '''
''' (CRUD): 
        #   [C]reate
        #   [R]ead
        #   [U]pdate
        #   [D]elete

        #   Criar, ler, alterar, apagar = lista[i]. '''


#        0   1   2   3
lista = [10, 20, 30, 40]
#       -4  -3  -2  -1


'''O índice [-1] sempre será o último item de uma lista'''