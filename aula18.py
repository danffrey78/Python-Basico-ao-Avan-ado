def nome_info(nome):
    print(f'{nome} ao contrario é: {nome[::-1]}')
nome = input('Digite seu nome: ')
nome_info(nome)

def checa_numero (numero):
    numero_int = int(numero)
    
    impar_par = numero_int % 2 == 0
    impar_par_txt = 'impar'

    if impar_par:
        impar_par_txt = 'par'
    
    print(f'{impar_par_txt}')

numero = input('Digite um numero: ')

checa_numero(numero)