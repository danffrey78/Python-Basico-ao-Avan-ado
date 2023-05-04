'''
calculadora com while
'''

while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*):  ')
    
    numeros_validos = None
    float_numero1 = 0
    float_numero2 = 0
    try:
        float_numero1 = int(numero1)
        float_numero2 = int(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros não são válidos')
        continue ### nao vai executar a linha de baixo

    operador_permitido = '+/*-'

    if operador not in operador_permitido:
        print('Operador inválido! \n')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador! \n')
        continue

    if operador == '+':
        print(f'{float_numero1}+{float_numero2}=',float_numero1+float_numero2)
    elif operador == '-':
        print(f'{float_numero1}-{float_numero2}=',float_numero1-float_numero2)
    elif operador == '*':
        print(f'{float_numero1}*{float_numero2}=',float_numero1*float_numero2)
    elif operador == '/':
        print(f'{float_numero1}/{float_numero2}=',float_numero1/float_numero2)

    sair = input('Queira sair? [s]im [n]ão: ').lower().startswith('s')
    #####transforma letra em minuscula / se começar com a letra retorna True(bool)
    if sair is True:
        break