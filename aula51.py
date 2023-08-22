''' INTRODUÇÃO AO DESEMPACOTAMENTO

    +

    TUPLES (TUPLAS) '''


nomes = ['Marcos', 'Vinícius', 'Aznar']


''' CRIANDO VARIÁVEIS COM CADA ITEM DE UMA LISTA  '''


nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)


''' EMPACOTAMENTO.

    #   variável,           ->      Que irá receber o valor do primeiro
                                    índice da lista.

    #   *_         ->      Onde será feito o empacotamento do restante
                                    dos dados da lista.

    #   Para declarar uma variável que não terá uso futuro,
        utiliza-se ' *_ '. '''


''' PEGANDO O PRIMEIRO ITEM DA LISTA.   '''


nome4, *_ = ['Marcos', 'Vinícius', 'Aznar']
print(nome4, _)


''' PEGANDO O SEGUNDO ITEM DA LISTA.   '''


_, nome, *_ = ['Marcos', 'Vinícius', 'Aznar']
print(nome)