'''
For & Range

Range -> range(start, stop, step)
'''

# UM ÚNICO PARÂMETRO DEFINE O 'STOP':
    #        ('STOP'): ATÉ ONDE VAI

# numeros_range_stop = range(10)
# print(numeros_range_stop)

# # DOIS PARÂMETROS DEFINEM O 'START' E O 'STOP':
#     #        ('START, STOP'): DA ONDE COMEÇA ATÉ ONDE VAI

# numeros_range_start_stop = range(5, 10)
# print(numeros_range_start_stop)


# # TRÊS PARÃMETROS DEFINEM O 'START', 'O STOP' E O 'STEP'
#     #        ('START, STOP, STEP'): DA ONDE COMEÇA ATÉ ONDE VAI,
#     #        E DE QUANTO EM QUANTO SERÁ O INCRMENTO

# numeros_range_start_stop_step = range(5, 10, 2)
# print(numeros_range_start_stop_step)

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)