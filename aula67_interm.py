''' VALORES PADRÃO PARA PARÂMETROS.
    #   Ao definir uma função, os parâmetros podem ter
        valores padrão.
    
    #   Caso o valor não seja enviado para o parâmetro,
        o valor padrão será usado.
         
    #   REFATORAR: editar o seu código. '''

# def soma (x, y, z = None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)


''' Todo parâmetro que segue um parâmetro nomeado deve ser,
    também, nomeado. '''


def soma (x, y = None,  z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(1 ,2 ,3)