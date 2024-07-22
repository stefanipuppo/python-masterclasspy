# SINTAXE: expressão for item in lista
''' Onde a expressao é a expressao que será avaliada para cada elemento em 'lista', 
e 'item' é a variavel que representa cada elemento na lista '''

numeros = [1,3,7,9,10,12,21]

quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)

print('---------------------------')

numeros = [1,3,7,9,10,12,21]

quadrados = [num**2 for num in numeros]
print(quadrados)

print('---------------------------')

# Criar uma lista de numeros pares de 0 a 10

pares = [num for num in range(11) if num % 2 == 0]
print(pares)

print('---------------------------')

frase = 'A Lófigca é apenas o principio da sabedoria, e não o seu fim'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais')
print(lista_vogais)

print('---------------------------')

# Operação distributiva entre valores de duas listas

distributiva = [k * m for k in [2,3,5] for m in [10, 20, 30]]
print(distributiva)