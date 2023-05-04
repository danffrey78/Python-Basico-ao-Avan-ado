# Operadores logicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se quqlquer valor for considerado falso, a expressão
# inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0.0.0 ''false
# Também existe o tipo None que é
# usado para resprentar um não valor

entrada = input('[E]ntrar [S]air ')
senha = input('SENHA: ')
if (entrada == 'E' or 'e') and senha == '1234':
    print('Vc entrou!')

elif (entrada == 'S' or 's') and senha == '1234':
    print('Vc saiu!')
    
else:
    print('Algo inesperado aconteceu! X.X')