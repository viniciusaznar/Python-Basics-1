'''Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

# SOLUÇÃO 1

# hora_entrada = input('Digite que horas são agora: ')

# int_hora_entrada = int(hora_entrada)

# entrada_bom_dia = int_hora_entrada >= 0 and int_hora_entrada <= 11
# entrada_boa_tarde = int_hora_entrada >= 12 and int_hora_entrada <= 17
# entrada_boa_noite = int_hora_entrada >= 18 and int_hora_entrada <= 23

# if entrada_bom_dia:
#     print('Bom dia')
# elif entrada_boa_tarde:
#     print('Boa tarde')
# else:
#     print('Boa noite')


# SOLUÇÃO 2

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora  >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora.')
except:
    print('Por favor, digite apenas números inteiros')
