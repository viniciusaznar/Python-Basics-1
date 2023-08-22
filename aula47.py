'''
# EXERCÍCIO

    #   Faça um  jogo para o usuário adivinhar
        qual a palavra secreta.

        -   Proponha uma palavra secreta qualquer e
            vai dar a possibilidade para o usuário
            digitar apenas uma letra.
        
        -   Quando o usuário digitar uma letra,
            confira se a letra digitada está na
            palavra secreta.

        -   Se a letra digitada estiver na palavra
            secreta; exiba a letra.

        -   Se a letra digitada não estiver na
            palavra secreta; exiba '*'.

        -   Faça a contagem de tentativas do seu
            usuário.'''



''' 1)  Importe a biblioteca 'os' para
        utilizar a ferramente 'cls',
        para criar uma lógica que limpa o terminal'''



import os



''' 2)  Defina e declare a variável da 
        palavra secreta antes do bloco do 'while.

    #   Se a variável da palavra secreta for 
        criada dentro do bloco do 'while',
        ela será apagada quando o laço
        voltar no seu começo, para reexecutar.'''



palavra_secreta = 'perfume'



''' 3)  Declare uma variável do tipo 'str'
        vazia para salvar as letras corretas
        que o usuário digitar.'''



letras_corretas = ''



''' 4)  Declare uma variável vazia (= 0) do tipo 'int',
        para salvar as letras corretas que o usuário digitar.'''



numeros_tentativa = 0



''' 5)  Inicie o bloco do 'while' com a lógica
        para solicitar que o usuário insira os
        dados desejados.'''



while True:



    ''' 6)  Peça ao usuário que digite uma única letra:'''



    letra_digitada = input('Digite uma letra: ')



    ''' 7)  Assim que o usuário inserir umam letra,
            declare uma variável para contabilizar a quantidade
            de tentativas'''

    

    numeros_tentativa += 1



    ''' 8)  É importante verificar se a condição
        do input foi satisfeita:

        #   Caso o usuário digite mais do que uma letra,
            alerte que ele entrou com a quantidade errada
            solicitada no 'input.
            E reinicie o laço com o comando 'continue ' '''



    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    


    ''' 9)  Crie um bloco 'if' para verificar se a letra
            digitada pelo usuário está dentro da variável
            'palavra_secreta'.'''
    


    if letra_digitada in palavra_secreta:


        ''' 10)  Caso a letra digitada pelo usuário esteja dentro
                da variável 'palavra_secreta',
                A mesma letra digitada será inclusa na variável
                'letras_corretas'.'''


        letras_corretas += letra_digitada


        ''' 11) Declare uma outra variável do tipo 'str' vazia
                para armazenar as letras corretas que forem
                digitadas pelo usuario.'''



    palavra_formada = ''


    ''' 12) Crie um bloco 'for' 
            com a nova variável 'letra_secreta',
            para percorrer a string que armazena a palavra secreta.'''


    for letra_secreta in palavra_secreta:


        ''' 13) Enquanto o bloco 'for' percorre
                a string que armazena a palavra secreta,
                com a variável 'letra_secreta',
                
                #   Crie uma condição onde é declarada a nova variável
                    letra_secreta para iterar a variável que guarda as
                    letras corretas inseridas pelo usuário ('letras_corretas').'''


        if letra_secreta in letras_corretas:



            ''' 14) Caso a condição seja verdadeira (True),

                    # Armazene a letra correta inserida pelo usuário
                    na variável declarada anteriormente: 'palavra_formada'.'''
            


            palavra_formada += letra_secreta



            ''' 15) Caso a condição seja falsa (False),

                    # Armazene um asterísco '*' na variável 
                    declarada anteriormente: 'palavra_formada'.'''
            


        else:
            palavra_formada += '*'



    ''' 16) Finalize o bloco do 'for', que está inserido
            no bloco do 'while', ainda em execução.'''



    ''' 17) Mostre na tela, a variável 'palavra_formada'.'''



    print(f'Palavra formada: {palavra_formada}')



    ''' 18) Crie uma condição para checar se a palavra formada
            é igual a palavra secreta.'''


    if palavra_formada == palavra_secreta:



        ''' 19) Caso a condição seja verdadeira (True),
                
                #   Limpe o terminal.
                #   Mostre na tela uma mensagem de congratulações.
                #   Mostre na tela a palavra secreta.
                #   Mostre o número de tentativas do usuário'''



        os.system('cls')
        print(
            'VOCÊ GANHOU! PARABÉNS!'
            f'A PALAVRA SECRETA É {palavra_secreta}'
            f'O NÚMERO DE TENTATIVAS FOI {numeros_tentativa}'
            )
        


        ''' 20) Reinicie as variáveis que armazenaram:
                
                # As letras corretas inseridas pelo usário
                # A palavra formada com as letras corretas inseridas pelo usuário
                # O número de tentativas.'''



        letras_corretas = ''
        palavra_formada = ''
        numeros_tentativa = 0        