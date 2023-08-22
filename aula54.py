''' EXERCÍCIO

    # Faça uma lista de compras com um elemento 'list':
    
        -   O usuário deve ter a possibilidade de inserir, apagar
            e listar valores da sua lista.
        -   Não permita que o programa quebre com erros
            de índices inexistentes na lista. '''


import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[I]nserir [A]pagar [L]istar')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        pritn('Por favor, escolha i, a ou l.')