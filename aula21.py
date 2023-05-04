frase = 'O python é uma linguagem de programação multiparadigma. Python'\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu = letra_atual
    i += 1

print('A letra que apareceu mais vezes foi '
    f'"{letra_apareceu}" que apareceu'
    f'{apareceu_mais_vezes}x')