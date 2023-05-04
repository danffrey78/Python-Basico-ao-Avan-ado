BOM_DIA = 00.00
BOA_TARDE = 12.00
BOA_NOITE = 18.00

hora = input('Qual o seu hoario?: ')

try:
    hora_float = int(hora)
    if hora_float >= BOM_DIA and hora_float < BOA_TARDE:
        print('Bom dia!')
    elif hora_float >= BOA_TARDE and hora_float < BOA_NOITE:
        print('Boa tarde!')

    elif hora_float >= BOA_NOITE and hora_float < 24:
        print('Boa noite')
except:
    print('Hora incorreta')


