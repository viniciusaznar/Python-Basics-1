'''LISTAS EM PYTHON

    #   Tipo list -> mutável.
    #   Suporta vários valores de qualquer tipo.
    #   Conhecimentos reutilizáveis -> índices e fatiamento.
    #   Métodos úteis: append, insert, pop,
    #   del, clear, extend, +. '''

#       01234
#      -54321

string = 'ABCDE'        #   5 caracteres


''' 
Criando uma lista: 

    # utiliza-se os colchetes '[]'.
    # uma lista vazia é considerada falsy
'''


lista = []


'''
Conferindo o tipo da lista:
'''

print(lista, type(lista))


'''
Uma lista pode comportar 
varios tipos de valores:
'''


#    Índice: da lista:
#         0    1     2         3   4
#        -5   -4    -3        -2  -1
lista1 = [123, True, 'Marcos', 1.2,[...]]


'''
Acessando os itens de uma lista e checando seu type:
'''

print(lista1[2].upper(), type(lista1[2]))


'''
Atribuindo novos valores a uma lista,
pelo índice desejado:
'''

lista1[-3] = 'Vinícius'
print(lista1)