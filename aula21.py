'''
Operadores lógicos
and (e) or (ou) not (não)

and -> todas as condicões precisam ser verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquela valor

São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tippo None que é
usado para representar um 'não-valor'
'''

'''
entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:
#   ...
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''


# Avaliação de curto circuito
print(True and True and True)
print(True and False and True)
print(bool(0))
print(bool(0.0))
print(bool(''))