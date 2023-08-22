'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
Estourar / Levantar uma exceção -> Ver um erro na tela

Sempre que usuário mandar um 'input',
O valor dele deve ser sempre tratado
'''

numero_str = input(
    'Vou dobrar o número que você digitar: '
    )

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso náo é um número')