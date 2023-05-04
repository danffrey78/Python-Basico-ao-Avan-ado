numero = input('Digite um inteiro: ')

if numero.isdigit:
    int_numero = int(numero)
    impar_par = int_numero % 2 == 0
    impar_par_text = 'Par'
    if impar_par == False:
        impar_par_text = 'impar'
    
    print(f'{int_numero} é {impar_par_text}')

    ...
else:
    print('Não é um inteiro')