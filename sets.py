# SET são conjuntos, coleção não ordenadas de valores unicos que usamos para armazenar multiplos itens dentro de um objeto

planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)

print('---------------------------------------')

# Nos conjuntos não tera valor duplicado.  ex:

astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print(astros, end= '')
astros_set = set(astros)
print(astros_set)

print('---------------------------------------')

# Comparações entre conjuntos

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua', 'Cometa de Halley'}
print(astros1 == astros2)

print('---------------------------------------')

# União de Conjuntos
print(astros1 | astros2)
print(astros1.union(astros2))

print('---------------------------------------')

# Intersecção de conjuntos, conjuntos que tem apenas os elementos em comum

print(astros1 & astros2)
print(astros1.intersection(astros2))

print('---------------------------------------')

# Direfença simetrica de conjuntos, a diferença de conjuntos

print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

print('---------------------------------------')

# Como acrescentar mais elemento

astros1.add('Urano')
print(astros1)

print('---------------------------------------')

# Para remover algum elemento

astros1.remove('Urano')
astros1.discard('Urano')
astros1.pop('Urano')                                      # remove de forma aleatoria
astros1.clear('Urano')                                    # limpa todo o conjunto