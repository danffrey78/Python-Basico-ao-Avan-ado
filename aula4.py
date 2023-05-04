nome = input('Digite seu nome: ')
encontrar = input('Digite o que queira encontar: ')

if encontrar in nome:
    print(f"Possui {encontrar} em {nome}")
else:
    print(f'Nao possui {encontrar} em {nome}')