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

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1  



print('Acabou')