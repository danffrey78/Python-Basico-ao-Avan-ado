palavra = 'danffrey'

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    palavra1 = ''
    for i in palavra:
        if letra in palavra:
            palavra1 += letra
        else:
            palavra1 += '*'
    print(palavra1)