# OPERADORES
# == | igual a
# != | diferente de
#  > | maior que
#  < | menor que
# >= | maior ou igual a
# <= | menor ou igual a

x = y = z = False

n1 = n2 = 0

print('Digite um numero: ')                       # voce pode fazer separado
n1 = int(input())

n2 = int(input('Digite outro numero: '))          # e tambem pode fazer junto, os dois jeito sao validos

x = n1 == n2
print('São iguais?', x, '\n')                     # '\n' é uma quebra de linha 



z = n1 > n2                                       # Verifica se n1 é maior que n2 e armazena o resultado em z
print(n1, 'é maior que', n2, '?', z, '\n')        # Imprime a comparação e o resultado

y = n1 != n2                                      # Verifica se n1 é diferente de n2 e armazena o resultado em y
print('São diferentes? ' + str(y))                # Imprime se n1 e n2 são diferentes, convertendo o booleano para string
 