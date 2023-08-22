'''
# MÉTODO:
    Uma ação que pode ser chamada dentro do objeto.
        Ex.

        texto = 'Luiz'      ->      objeto = 'do tipo str'

        texto.lower()       ->      objeto.metodo()
        
        objeto.metodo()     ->      texto.upper()
'''

'''
# ITERÁVEL:
    -> str, range, etc:
        Um elemento que pode ser navegável através de seus índices.
        Um elemento que pode te entregar um resultado por vez.
        Um elemento que possuí um método chamado (__iter__).
'''

'''
# COMO O 'FOR' FUNCIONA:
'''

texto = 'Texto aqui'
for letra in texto:
    print(letra)

''' 
    1)  O 'for' solicita,
        Dentro do objeto iterável 'string',
        o método '(__iter__)'
        [todo método é uma ação]
                

        2)  A ação do método
            '(__iter__)' é retornar
            a ativação de outro objeto
            chamado 'iterador'
            [o iterador é quem navega pelo objeto iterável]

                A função 'texto = iter('Luiz')

                ->  representa
                o mesmo que acionar/chamar
                o método '(__iter__)'
                do objeto 'texto'
                [que é do tipo 'str]
                [que é iterável]

                        
                3)  A função '.__next__()' é
                    acionada pelo iterador e a
                    sua função é retornar
                    cada índice dentro objeto
                    'str'para que foi apontada.
                    Chama o próximo valor
                    disponível no objeto
                    iterador.
'''

# Função para chamar 
# o iterador do objeto '.__iter__()'

texto = 'Luiz'              # iterável
iterador = iter(texto)      # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# Função para chamar 
# o próximo valor disponível
# objeto iterador '.__next__()'
        # Quando se esgotam os valores
        # para o next retornar,
        # ele levantará um erro.

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


'''
# ITERADOR
    -> quem saber entregar um valor por vez
'''

'''
# ITER
    -> me entregue seu iterador
'''

    # numeros = range(0, 100, 8)

    # for numero in numeros:
    #     print(numero)