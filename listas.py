# Lista representa uma sequencia de valores | Sintaxe: nome_lista = [valores] | lembrando que o indice começa com 0

# Listas podem ser concatenadas

n1 = [9,8,7,6,4,3]
n2 = [22, 1, 5, 3, 87]

valores = n1 + n2
print(valores)

print('--------------------------------------------')

# acessando o indice do valor na lista

print(valores[3])

print('--------------------------------------------')

# acessando o ultimo valores da lista

print(valores[-1])

print('--------------------------------------------')

# alterando o valor da lista

num1 = [9,8,7,6,4,3]
num2 = [22, 1, 5, 3, 87]
valores_num = num1 + num2
valores_num[0] = 10
print(valores_num)

print('--------------------------------------------')

# imprimi valores sequencias, de um ponto ao outro

num1 = [9,8,7,6,4,3]
num2 = [22, 1, 5, 3, 87]
valores_num = num1 + num2
valores_num[0] = 10
print(valores_num[0:2])

print('--------------------------------------------')

# para saber quantos valores tem dentro da lista

num1 = [9,8,7,6,4,3]
num2 = [22, 1, 5, 3, 87]
valores_num = num1 + num2
valores_num[0] = 10
print(len(valores_num))

print('--------------------------------------------')

# para trazer a versao ordenada da lista sem modifica-la

num1 = [9,8,7,6,4,3]
num2 = [22, 1, 5, 3, 87]
valores_num = num1 + num2
valores_num[0] = 10
print(sorted(valores_num))              
print(sorted(valores_num, reverse=True))                 # para trazer a versao reversa o codigo
print(sum(valores_num))                                  # para somar os valores da lista
print(min(valores_num))                                  # para encontrar o valor minimo da lista
print(max(valores_num))                                  # para encontrar o valor maximo da lista

print('--------------------------------------------')

# iserindo um valor na lista, no final da lista

valores_num.append(55)                                           
print(valores_num)

print('--------------------------------------------')

# excluindo o valor da lista, ultimo valor da lista

valores_num.pop()
print(valores_num)

print('--------------------------------------------')

# excluindo o valor da lista pelo indice

valores_num.pop(2)
print(valores_num)

print('--------------------------------------------')

# inserindo o valor da lista pelo indice, esse metodo tem dois argumentos, o primeiro é o indice e o segundo o valor

valores_num.insert(3,44)
print(valores_num)

print('--------------------------------------------')

# para saber se um determinado valor esta na lista

print(7 in valores_num)

print('-------------------Lista de strings-------------------------')

planetas = ['Mercurio', 'Venus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:                              # aqui planeta é uma variaver de interaçao
    print(planeta)

print('------------------- Exericicio -------------------------')

# Crie um script que peça para o usuario digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista. Na sequencia, exiba na tela os elementos em ordem alfabetica, um por linha, usando laço de repetição

bebidas = []                        # voce pode criar uma lista vazia assim

for i in range(5):
    print(f'Digite sua bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde!')