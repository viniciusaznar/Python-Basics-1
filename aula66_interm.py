''' ARGUMENTOS:

    #   ARGUMENTOS NOMEADOS:    
        - Tem nome com sinal de '='. '''

''' Definição:
    -   Os argumentos nomeados não precisam respeitar a ordem
        dos parâmetros estabelecidos na função. '''

def soma(x, y):
    print(f'{x=}, y={y}', '|', 'x + y= ', x + y)

soma(y=1, x=2)




def soma_z(x, y, z):
    print(f'{x=}, y={y}, {z=}', '|', 'x + y= ', x + y + z)

''' Caso um parâmetro tenha sido nomeado e existirem outros parâmetros
    subsequentes, eles deverão também ser nomeados. '''

soma(1, z=3, y=2)

''' Parametros nomeados não precisam respeitar a ordem da função. '''

soma(y=1, z=3, x=2)


'''    #   ARGUMENTOS NÃO NOMEADO:
        - Recebe apenas o argumento (valor). 
        - Chamado tambémd de argumento posicional. '''


''' Definição:
    -   Os argumentos não nomeados (Posicionais) devem respeitar a ordem
        dos parâmetros estabelecidos na função. '''

def soma(x, y):
    print(f'{x=}, y={y}', '|', 'x + y= ', x + y)

soma(1, 2)