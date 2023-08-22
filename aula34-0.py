'''
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
'''

'''
(POO), 
um objeto é 
um modelo 
de um elemento 
do mundo real 
que possui 
estado e comportamento. 
'''

'''
O estado de um objeto é 
representado 
por suas propriedades, 
Propriedades são 
os dados 
que um objeto armazena.
'''

'''
O comportamento é 
representado por seus métodos.
Métodos são 
as operações
que um objeto pode realizar.
'''

'''
As propriedades 
e os métodos de um objeto são 
definidos 
por sua classe.
'''

'''
Classe é 
um modelo para 
um tipo de objeto. 
A classe define
as propriedades
e os métodos
que todos os objetos 
do mesmo tipo 
compartilham.
'''

'''
Os objetos são criados
a partir de classes. 
Quando um objeto é criado, 
ele é inicializado 
com os valores padrão 
de suas propriedades.
'''

'''
Os objetos podem 
interagir uns 
com os outros 
enviando mensagens. 
Uma mensagem é 
uma solicitação
para que um objeto execute 
um método.
'''

'''
Os objetos podem 
ser agrupados em coleções. 
Uma coleção é 
um grupo de objetos 
do mesmo tipo.
'''

'''
Os objetos são 
uma forma poderosa 
de representar o mundo real
 em programas de computador. 
Eles permitem 
que os programadores criem 
programas que são mais fáceis 
de entender e de manter.
'''

'''
EXEMPLOS DE OBJETOS:

Um carro é 
um objeto que tem propriedades 
como marca, modelo, cor e ano. 
Ele também tem 
métodos como dirigir, 
acelerar e frear.
'''

'''
Uma pessoa é 
um objeto que tem 
propriedades como 
nome, idade, sexo e endereço. 
Ele também tem 
métodos como falar, andar 
e comer.
'''

'''
Um banco de dados é 
um objeto que tem 
propriedades como 
nome, tipo e tamanho. 
Ele também tem 
métodos como inserir, 
atualizar e excluir dados.
'''

'''
Os objetos são 
usados em muitos 
diferentes tipos 
de programas de computador. 
Eles são 
usados em 
programas de desktop, 
programas de web, 
programas de jogos e 
programas de negócios.
'''

string = 'marcos'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# # string[3] = 'ABC'
# print(string)
# print(outra_variavel)

# ex. ...f'{string[:3]}'...
    # SIGNIFICA:

    # '[ : n ]' -> ir do índice inicial (0) até
    #   até índice enumerado;
    # '[ n : ]' -> ir do índice enumerado (0) até
    #   até índice final;

print(string.zfill(50))
print(string.capitalize())
