nome = 'Daniel Sa'
count = 0
novo_nome = ''

while count < len(nome):
    letra = nome[count]
    novo_nome += f'*{letra}*'
    count += 1

print(novo_nome)