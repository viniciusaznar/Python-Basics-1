'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''

'''
# LOOP INFINITO:
    Quando um código não tem fim.
    Quando não há uma mudança de condição para
    que ele possa parar de executar

# EXEMPLO DE LOOP INFINITO:
        
    # condicao = True

    # while condicao:
    #     print(1)
    #     print(2)
    #     print(3)
'''
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break

# print('acabou')

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print(f'Acabou a  repetição da contagem, o {contador=} não é menor que 10')
print('Sair do bloco while atual')