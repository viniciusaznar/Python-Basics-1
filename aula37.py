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

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o ', contador)
        continue

    print(contador)
          
    if contador == 40:
        break

print('Acabou')