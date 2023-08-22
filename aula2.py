'''
corpo da função:
    função(argumento(s))
        print();
'''
print(12, 34)
print(56, 78)
'''
os argumentos inseridos, no exemplo acima, são chamados de:
    'argumentos não-nomeados'
        - são argumentos que não possui
        o trecho antecessor 'nome do argumento
'''
print(12, 34, sep='-')
print(56, 78, sep="-")
'''
O trecho sep='' é chamado de 'nome do argumento', logo ele nomeia o argumento
sucessor;
NOVO ARGUMENTO = sep=''
    - modifica o separador dos argumentos não-nomeados
'''
# \r\n -> CRLF (Windows)
# \n -> LF (Linux)
print(12, 34, sep='-', end='\n##')
print(12, 34, sep='-', end='\r\n')
print(56, 78, sep="-", end='\n')