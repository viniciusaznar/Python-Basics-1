'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6
letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é
é muito grande".
'''


# SOLUÇÃO 1
# primeiro_nome = input('Digite seu primeiro nome: ')

# primeiro_nome_curto = len(primeiro_nome) <= 4
# primeiro_nome_normal = len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6

# if primeiro_nome_curto:
#     print('Seu nome é curto')
# elif primeiro_nome_normal:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é longo')


# SOLUÇÃO 2

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito longo')
else:
    print('Digite mais de uma letra.')