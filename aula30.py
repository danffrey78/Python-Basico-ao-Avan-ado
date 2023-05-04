def soma(*args):
    total = 0
    for numero in args:
        total += numero

    return total
soma1 = soma(2,3,4,5,6)

print(soma1)
nomes = ['dan','joao','felipe']

print(*nomes)