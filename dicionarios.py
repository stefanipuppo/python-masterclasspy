# DICIONAIRIOS  - Permitem armazenar dados em pares, chaves e valor. São similares ao arrays assosiativos

elemento = {                                   # Não pode ter mais de um valor para a mesma chave e são imutaveis
    'Z' : 3,
    'nome' :  'Litio',
    'grupo' : 'Metais Alcalinos',
    'densidade' : '0.534'
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicinario possui {len(elemento)} elementos.')

print('---------------------------------------')

# ATUALIZAR UMA ENTRADA

elemento['grupo'] = 'Alcalinos'
print(elemento)

print('---------------------------------------')

# ADICIONAR UMA ENTRADA

elemento['periodo'] = 1
print(elemento)

print('---------------------------------------')

# RETORNA OS ITENS DENTRO DO DICIONARIO NA FORMA DE UMA LISTA DE ITENS - cada item esta dentro de uma tupla               

print(elemento.items())
for i in elemento.items():
    print(i)

print('---------------------------------------')

# MOSTRA AS CHAVES DO DICIONARIO

print(elemento.keys())
for i in elemento.keys():
    print(i)

print('---------------------------------------')

# MOSTRA OS VALORES DO DICIONARIO

print(elemento.values())
for i in elemento.values():
    print(i)

print('---------------------------------------')

# PARA DESEMPACODAR AS CHAVES E VALORE SIMULTANEAMENTES (forma de uma tabela/resumo)

for i, j in elemento.items():
    print(f'{i}: {j}')

print('---------------------------------------')


# EXCLUSÃO DE ITENS EM DICIONARIOS]

del elemento['periodo']
print(elemento)

elemento.clear()
print(elemento)                               # apaga tudo dentro do dicionario

del elemento                                  # apaga o dicionario