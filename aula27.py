#enumerate ele enumera cada item da lista

lista = 'Ola', 'mundo'

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    indice, nome = item
    print(f'\t \n',indice,nome)