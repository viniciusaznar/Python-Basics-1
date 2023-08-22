''' ENUMERATE

    #   Enumera iteráveis (índices).    '''

lista = ['Marcos', 'Vinícius', 'Aznar']
lista.append('João')


lista_enumerada = enumerate(lista)
print(next(lista_enumerada))


''' MOSTRAR OS ÍNDICES DE UMA LISTA ENUMERADA.  '''


for item in lista_enumerada:
    print(item)


''' Após chamar os dados de uma lista, onde o foi utilizado
    o módulo enumerate(), os mesmo serão consumidos,
    deixando a variável apenas apontando o endereço de memória,
    mas sem qualquer dado.  '''


print('O que tem na lista enumerada: ')
for item in lista_enumerada:
    print(item)


''' CONTORNANDO O CONSUMO DOS DADOS DO INTERETOR.

        #   Para iterar por uma lista com o enumerate(),
            sem consumir os dados do iterador, faça:

        #   NÃO COLOCAR o valor do enumerate() em uma variável.

        #   Colocar a função enumerate() direto na estrutura 'for'. '''
    
for item in enumerate(lista):
    print(item)


''' SEPARANDO E NOMEANDO OS ELEMENTOS DE UMA LISTA. '''

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])