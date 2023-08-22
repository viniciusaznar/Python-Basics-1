a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
string1 = 'a={0} a={0} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)
formato = string1.format(a, b, c)

print(formato)

# IndexError:
# out of range -> você está buscando algo que já acabou

'''
OBJETO

Tudo em Python é um objeto.

    Objetos podem fazer ações.

        Essas ações são chamadas de métodos.

o sinal de '.' depois do nome de um objeto dá acesso
a todos os métodos que existem dentro dele.
'''

'''
PARÂMETRO NOMEADO

É quando é dado nome aos parâmetros dentro
da chamada da função

A partir do momento em que um parâmetro é nomeado
dentro da chamada da função,
TODOS os outros, se houver, deverão ser nomeados também

parâmetro -> quando se refere ao nome da variável
argumento -> quando se refere ao valor da variável

ex.
parâmetro = argumento
'''