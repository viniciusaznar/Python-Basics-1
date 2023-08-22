'''LISTAS EM PYTHON

    #   Tipo list -> mutável.
    #   Suporta vários valores de qualquer tipo.
    #   Conhecimentos reutilizáveis -> índices e fatiamento.
    #   Métodos úteis: append, insert, pop,
    #   del, clear, extend, +. '''


# Índice:
#        0  1  2  3
lista = [1, 2, 3, 4]
#       -4 -3 -2 -1


print(lista)


'''
Declarar uma variável e atribuí-la
com o valor, o elemento que está no
índice de uma lista: '''


numero = lista[2]
print(numero)


'''
Atribuindo novos valores a uma lista,
pelo índice desejado: '''

lista[-3] = 'Vinícius'
print(lista)


'''
Apagando um elemento da lista
através do seu índice com o
comando 'del': '''


del lista[3]


'''
Adicionando novos item na lista. '''


lista.append(50)
lista.append(600)
lista.append(7000)
print(lista)


'''
Removendo o último item da lista.
    #   Colocar um valor inteiro no parâmetro
        do método '.pop()', excluirá o o conteúdo
        do índice do mesmo valor. '''


lista.pop()
#   lista.pop(3)


'''
Colocando o último valor retirado de uma lista
em uma variável. 

    #   O método '.pop()' retorna o valor do tipo
        do último item removido da lista. '''


ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)