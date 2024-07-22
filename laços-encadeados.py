import random

# UM LAÇO ENCADEADO É UM LACO QUE ESTA DENTRO DE OUTRO LAÇO

for cont_ex in range(1, 6):                         # Loop externo para criar 5 rodadas (1 a 5)
    print(f'\nRodada: {cont_ex}')                   # Imprime o número da rodada
    for cont_in in range(5, 0, -1):                 # Loop interno para imprimir valores de 5 a 1
        print(f'Valor: {cont_in}')                  # Imprime o valor atual do loop interno

print('Fim dos laços')                              # Imprime mensagem indicando o fim dos loops



print('-------------------------------------')

import random

for A in range(1, 6):                       # Loop para criar 5 conjuntos (1 a 5)
    print(f'\nConjunto {A}')                # Imprime o número do conjunto
    for B in range(5):                      # Loop para gerar 5 números aleatórios por conjunto
        num = random.randint(1, 199)        # Gera um número aleatório entre 1 e 199
        print(f'Valor: {num}')              # Imprime o número aleatório


