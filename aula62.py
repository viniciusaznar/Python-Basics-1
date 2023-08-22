''' EXERCÍCIO - VALIDANDO CPF.
    CALCULO DO PRIMEIRO DIGITO DO CPF:

    #   CPF: 746.824.890-70

    #   Colete a soma dos 9 primeiros digitos do CPF,
        MAIS O PRIMEIRO DIGITO,
        multiplicando cada um dos valores por uma
        contagem regressiva começando de 10.

    #   Ex.: 746.824.890-70 (7468248907)
        11  10  9   8   7   6   5   4   3   2 
    *   7   4   6   8   2   4   8   9   0   7   #   PRIMEIRO DIGITO
        77  40  54  64  14  24  40  36  0   14
        
    #   Somar todos os resultados:
        77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363

    #   Multiplicar o resultado anterior por 10:
        363 * 10 = 3630

    #   Obter o resto da divisão da conta anterior por 11:
        3630 % 11 = 0

    #   Se o resultado anterior for maior que 9:
            Resultado é 0
        else:
            resultado é o valor da conta

    #   O segundo digito do CPF é 0. '''



''' 1) Declarando a var 'cpf' ('SEM PONTOS OU TRAÇO),
    somente com digitos: '''

cpf ='74682489070'


''' 2) Fazendo o fatiamento dos digitos da var 'cpf': '''

nove_digitos = cpf[:9]


#   teste1:
# print(nove_digitos)
#   verificar o fatiamento atribuído à var 'nove_digitos'


''' 3) Declarando a var 'resultado' para armazenar
    as operações matemáticas necessárias com os números do CPF: '''

resultado_digito_1 = 0


''' 4) Declarando a var 'contador_regressivo' para armazenar
    o vaor atribuído que para o contador regressivo necessário
    para os calculos: '''

contador_regressivo_1 = 10


''' Laço 'for' para iterar a var 'nove_digitos' e aplicar automaticamente
    as operações matemáricas necessárias aos digitos atribuídos. '''

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 
    contador_regressivo_1 -= 1 
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


#   teste1:
print(digito_1)
#   verificar a lógica atribuída ao laço 'for':
#   -   Para cada 'digito', começando do 0, na var 'nove_digitos'.
#   -   Decremente o contador regressivo em -1.
#   -   A var 'digito' passa a receber o valor da var 'resultado',
#       multiplicado por 10, e o resto da divisão por 11
#       (digito = (resultado * 10) % 11)
#   -   Se a var 'digito' for maior que 9, o valor zero é atribupido a ela
#   -   Senão, a var 'digito' recebe o valor da conta da 'var' digito.