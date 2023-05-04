'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ('Dan','Joao','Juh'):
    print(falar_bom_dia(nome))
    print(f'{falar_boa_noite(nome)}')

x = f'Ola mundo'

print(x)