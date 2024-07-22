# Tuplas são imutaveis, não podem ser modificadas depois de criadas

# Operações nao disponiveis: .sort(), .append(), .reverse(), .pop()

# para saber quantos valores tem repetidos dentro da tupla

tupla = (1,2,3,4,5,6,7,2,9,8,2,7,6,5,4,3,2)
print(tupla.count(3))

print('--------------------------------------------')

# criando uma lista a partir de uma tupla

grupo17 = list(tupla)
grupo17[0] = '87654'
print(grupo17)

print('--------------------------------------------')

# criando uma tupla a partir de uma lista

grupo1 = ['Li', 'Na', 'K', 'RB', 'Cs', 'Fr']
alcalinos = tuple(grupo1) 
print(alcalinos)

# como nao pode modificar a tupla, voce pode criar uma nova caso queira por exemplo ordena-la

print(sorted(alcalinos))