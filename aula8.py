#Exercicio:

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
espaço = ' '

if nome and idade:
    print(f'O seu nome é: {nome}')
    print(f'O seu nome invertido é: {nome[::-1]}')
    
    if espaço in nome:
        print('Seu nome tem espaço')
    
    else:
        print('Seu nome nao tem espaço')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe vc deixo os campos vazios')