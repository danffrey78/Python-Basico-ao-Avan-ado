'''
letras maiusculas serve como constantes
'''
velocidade = 120
local_carro = 100

VELOCIDADE = 80
LOCAL = 100
RADAR_RANGE = 1

velocidade_carro_passou_velocidade_1 = velocidade > VELOCIDADE 

carro_multado = local_carro >= (LOCAL - RADAR_RANGE) and \
     local_carro <= (LOCAL + RADAR_RANGE)

carro_foi_multado = carro_multado and velocidade_carro_passou_velocidade_1

if carro_foi_multado:
    print('Foi mutado')