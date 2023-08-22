# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))

# Nas função dentro de funções,
# O Python resolve os 'parenteses' (Parâmetros),
# do mais interno possível até o mais externo possível
# Polimorfismo -> usar o mesmo operador pra fazer
# coisas diferentes
print(1 + 1) # fazer a adição de dois números int
print('a' + 'b') # concatenar duas strings
print(bool('')) # Na conversão para o tipo bool,
# string vazia -> False
print(bool(' ')) # Na conversão para o tipo bool,
# string com, pelo menos, um espaço -> True
print(str(11) + 'b')