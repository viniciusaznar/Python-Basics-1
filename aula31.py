'''
Flag (Bandeira) - Marca um local
None = Não valor
'is' e 'is not' = é ou não é (tipo, valor, identidade)
id = Identidade
'''


v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))

# condição = False

# if condição:
#   print('Faça algo')
# else:
#   print('Não faça algo')

condição = False
passou_no_if = None

if condição:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')
# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
  print('Não passou no If')

if passou_no_if is not None:
   print('Não passou no If') 