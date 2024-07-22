# Funções lambdas(anonimas) - são funçôes que nao tem nome e que podem ser criadas e usadas no mesmo momento
# Sintaxe: lambda argumentos: expressao

quadrado = lambda x: x**2

for i in range(1,11):
    print(quadrado(i))


print('---------------------------')

par = lambda x: x % 2 ==0
print(par(8))

print('---------------------------')

f_c = lambda f: (f - 32) * 5/9
print(f_c(32))

# FUNÇÃO MAP() - permite aplicar uma outra função a cada elemento de um objeto iteravel e retorna um objeto do tipo map contento o resulado              | UMA FUNÇÃO QUE APLICA FUNÇÕES | geralmente usada com lambda

# SINTAXE:   map(função, iteravel)

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x*2, num))
print(dobro)

print('---------------------------')

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiuscula = list(map(str.upper, palavras))
print(maiuscula)

print('---------------------------')

# FILTER    - filtra o elemento de uma sequencia

def numero_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,121,12,13]

num_par = list(filter(numero_pares, numeros))
print(num_par)


print('---------------------------')

# RECUDE  - realiza opção comulativas em uma sequencia de elemento e retorna um unico valor no final
# SINTAXE - função, sequencia, valor_inicial

from functools import reduce

def mult(x,y):
    return x * y

numeros = [1,2,3,4,5,6]

total = reduce(mult, numeros)
print(total)

# Soma acumulativa dos quadrados de valores, usando expressão lambda

numeross = [1,2,3,4]
total = reduce(lambda x,y: x **2 + y**2, numeross)
print(total)