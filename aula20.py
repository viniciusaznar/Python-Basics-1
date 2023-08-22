primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# int_primeiro_valor = int(primeiro_valor)
# int_segundo_valor = int(segundo_valor)

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual 2'
        f'ao {segundo_valor=}'
    )
else:
    print(
        f'O {segundo_valor=} é maior '
        f'ao {primeiro_valor=}'
    )

# if primeiro_valor > segundo_valor:
#     print(f'O {int_primeiro_valor=} é maior do que o {int_segundo_valor=}')
# else:
#     print(f'O {int_segundo_valor=} é maior do que o {int_primeiro_valor=}')