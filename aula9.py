'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero = input('Digite um numero: ')

try:

    if numero.isdigit:
        numero1 = int(numero)
        print(f'O dobro de {numero1} é: {numero1 *2}')

except:
    print('nao digitou um numero')