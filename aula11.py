USUARIO_1 = 'danffreyvava'
USUARIO_2 = 'danffreytft'
SENHA = '12345'
IDADE = 18

def maior_de_idade(idade):
    if idade > IDADE:
        print('Vc é maior de idade')
    else:
        print('Vc é menor de idade')

usuario = input('Usuário: ')
senha = input('Senha: ')
if usuario == USUARIO_1 and senha == SENHA:
    print(f'Olá {usuario}!')
    if senha == SENHA:
        print(f'vc entrou! Seja bem vindo {usuario}')
        print(f'O seu nome ao contrário é: {usuario[::-1]}')
        print(f'{usuario} possui {len(usuario)} letras')
        print(f'A primeira letra é: {usuario[0]} ')
        print(f'A ultima letra é: {usuario[-1]} ') 
        if ' ' in usuario:
            print('Possui Espaço em seu nick')
        else:
            print('Nao possui espaço em seu nick')
        
        idade = input('Digite sua idade: ')
        idade_int = int(idade)
        maior_de_idade(idade_int)
    else:
        print('Senha incorreta')
else:
    print('Usuario invalido')