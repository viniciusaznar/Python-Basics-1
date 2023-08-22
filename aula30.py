'''
CONTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

# Para constantes, seu nomes devem ser escritos
# com letras maíusculas
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega


# CÓDIGO INICIAL
# if velocidade > RADAR_1:
#     print('Velocidade carro passou do radar 1')

#     if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#         local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#             velocidade > RADAR_1:
#         print('Carro multado em radar 1')

# CÓDIGO LIMPO

vel_carro_pass_radar = velocidade > RADAR_1

radar_range_1 = LOCAL_1 - RADAR_RANGE
radar_range_2 = LOCAL_1 + RADAR_RANGE

local_carro_radar_1 = local_carro >= radar_range_1
local_carro_radar_2 = local_carro <= radar_range_2

carro_passou_radar_1 = local_carro_radar_1 or local_carro_radar_2
    
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar

if vel_carro_pass_radar:
    print('Velocidade carro passou radar 1')

if carro_passou_radar_1:
    print('Carro passou do radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')