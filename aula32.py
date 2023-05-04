import copy

pessoa = {
    'nome': 'Dan',
    'Sobrenome' : 'sakay',
}

#print(pessoa.keys()) # mostra a chave
#print(pessoa.values()) # mostra o valor

print(list(pessoa.items())) # mostra a chave e o valor

#for chave, valor in pessoa.items():
 #   print(chave, valor)

pessoa.setdefault('idade',None)
print(pessoa['idade'])

# pessoa1 = pessoa.copy # copia raza, não copia lista dentro de listas

pessoa1 = copy.deepcopy(pessoa) # copia tudo

print(pessoa1)