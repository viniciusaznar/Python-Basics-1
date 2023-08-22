''' ESCOPO DE FUNÇÕES EM PYTHON. 

    #   Escopo significa o local onde aquele código pode atingir. 
    
    #   Existe ESCOPO GLOBAL e ESCOPO LOCAL. 
    
        -   GLOBAL: Escopo onde todo o código é alcançavel.
        -   LOCAL:  Escopo onde apenas nomes do mesmo local
            podem ser alcançados. '''


''' DEFININDO O ESCOPO DE UMA FUNÇÃO:   '''


''' Variáveis definidas DENTRO DO ESCOPO DA FUNÇÃO só funcionam,
    ou são acessadas dentro da própria função. '''

x = 1

def escopo1():
    global x             
    x = 10

    def escopo2 ():
        global x
        x = 11
        y = 2
        print(x, y)

    escopo2()
    print(x)

escopo1()
print(x)


''' Variáveis definidas DENTRO DO ESCOPO DO MÓDULO funcionam,
    TANTO DENTRO, QUANTO FORA do escopo da função. '''


# x = 1
# def escopo3():
#     print(x)

# escopo3()
# print(x)