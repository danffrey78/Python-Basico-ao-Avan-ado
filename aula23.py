import os

palavra = 'danffrey'
letras_acertadas = ''
tentativas = 0



while True:
    os.system('clear')
    tentativas += 1
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    

    if letra in palavra:
        letras_acertadas += letra
    palavra_1 = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_1 += letra_secreta
        else:
            palavra_1 += '*'

    print(palavra_1)

    if palavra_1 == palavra:
        break
            
