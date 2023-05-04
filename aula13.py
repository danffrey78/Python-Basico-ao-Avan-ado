usuario = input('Novo usuario: ')
int_usuario = len(usuario)

if len(usuario) < 5 and len(usuario) > 0:
    print('Usuario muito curto')
elif len(usuario) >= 5 and len(usuario) < 7:
    print('Usuario normal')
elif int_usuario > 6:
    print('Usuario é muito grande')

else:
    print('Algo inesperado aconteceu!')