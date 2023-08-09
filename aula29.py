"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

local_carro_cima = local_carro >= (LOCAL_1 - RADAR_RANGE)
local_carro_baixo = local_carro <= (LOCAL_1 + RADAR_RANGE)

local_carro_cima_e_baixo = local_carro_cima and local_carro_baixo
vel_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar1 = local_carro_cima_e_baixo
carro_multado_radar1 = (carro_passou_radar1 and vel_carro_passou_radar_1)

if vel_carro_passou_radar_1:
    print('Velocidade carro passou radar 1')
if carro_multado_radar1:
    print('Carro multado em radar 1')
