''' Fatiamento de strings
 Obs: a função len retorna a qtd de caraceteres da str
 fatiamento [i:f:p] [::]
'''

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[::-1]) # inversão da string
'''        começo : fim   '''

print(len(variavel))

if len(variavel) > 8:
    print('Tudo certo')