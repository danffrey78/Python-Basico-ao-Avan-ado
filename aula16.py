condicao = True
count = 0

while condicao:
    condicao = input('Digite "sair" para sair do programa: ')

    if condicao == 'sair':
        break

while count  < 10:
    print(f'{count=}')

    count = count +1

    if count == 8:
        count = count +1
        continue
