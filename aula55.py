# '''  IMPRECISÃO DE PONTO FLUTUANTE  

#         #   Double-precision floating-point format IEEE 754. '''

# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2
# print(numero_3)

# '''   NÚMERO FORMATADO   '''

# print(f'{numero_3:.2f}')
# print(type(f'{numero_3:.2f}'))

# '''   FUNÇÃO 'ROUND'   

#         #   round(variável float, quantidade de casas decimais)'''

# print(round(numero_3, 1))
# print(type(round(numero_3)))

'''    BIBLIOTECA DECIMAL   '''

# import decimal
# numero_decimal_1 = decimal.Decimal(0.1)
# numero_decimal_2 = decimal.Decimal(0.7)
# numero_decimal_3 = decimal.Decimal(numero_decimal_2) + decimal.Decimal(numero_decimal_1)
# print(numero_decimal_3)

import decimal
numero_decimal_1 = decimal.Decimal('0.1')
numero_decimal_2 = decimal.Decimal('0.7')
numero_decimal_3 = decimal.Decimal(numero_decimal_2) + decimal.Decimal(numero_decimal_1)
print(numero_decimal_3)