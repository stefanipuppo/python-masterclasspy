# FUNÇÕES BUILTIN - funções internas


# valores = [2,-3,4,5,6,9,-8,7,6,7]
# print(max(valores))
# print(min(valores))
# a = -5
# b = 4
# print(abs(a))                               # para saber o valor absoluto
# print(pow(a, b))                            # para saber o valor expoente
# c = 2.789011
# print(round(c,2))                           # para arredondar o valor com a quantidade de casa decimal desejada

import math

# Para saber o valor da raiz quadrada

x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(raiz_quadrada)
print(math.ceil(raiz_quadrada))                        # para arredondar o valor int pra cima
print(math.floor(raiz_quadrada))                       # para arredondar o valor int pra baixo
print(round(raiz_quadrada, 2))                         # para arredondar o valor float em quantos decimais desejado

logaritmo = math.log10(y)                               # expressa a potência à qual 10 deve ser elevado para obter um determinado número.
print(logaritmo)

print(math.pi)
print(math.factorial(x))
print(x / math.inf)