'''
NUNCA faça um type casting
do input que o usuário digitar

ex.
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: ))
'''
'''
SEMPRE jogue a coerção de tipo para uma nova variável,
quando o usuário digitar o input

ex.
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: ))

int_num_1 = int(numero_1)
int_num_2 = int(numero_2)
'''

# sem coerção, o input sempre gerará um valor do
# tipo str


'''
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}')
Ao invés de escrever o nome da variável para que ela sejá
printada, dentro da referência de chaves, depois
do nome da variável, pode-se colocar o sinal de '='
e no print() aparecerá o nome da variável
e  sinal de igual
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}')
'''

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_num_1 = int(numero_1)
int_num_2 = int(numero_2)

print(f'A soma dos números é: {int_num_1 + int_num_2}')