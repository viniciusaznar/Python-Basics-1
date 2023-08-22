nome = 'Marcos Vinícius'
altura = 1.90
peso = 92
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Marcos tem 1.90 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987
# IMC = peso / (altura x altura)

# (...) -> Ellipsis,
# Usado como placeholder, por exemplo,
# em uma variável onde ainda não se pensou
# sobre o seu algorítmo