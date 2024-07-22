import random                                      # random significa aleatiorio

# NUMEROS ALEATORIOS

valor = random.randint(1,20)                       # randint significa aleatorio inteiro
print(valor)

print('---------------------------------------------------------')

# ALEATORIOS INTEIROS

print('Gerar cinco numeros aleatorios entre 1 e 50: \n' )
for i in range(7):                                # geralmente usa a variavel i para contatores, range determina quantas vezes vai rodar
    n = random.randint(1,50)                      # recebe o retorno de random
    print(f'Numero gerado: {n}')

print('---------------------------------------------------------')

# ALEATORIOS FLUTUANTES - FLOAT - ele gera numeros de 0.0 a 1.0

valor_float = random.random()                           # esse metodos nao aceita argumetos
print(valor_float)

print('---------------------------------------------------------')

# PARA GERAR NUMEROS DE 1 A 10

valor_float = random.random()                           
print(F'valor_float: {valor_float * 10}')

print('---------------------------------------------------------')

# PARA ARREDONDAR O VALOR

valor_floats = random.random()                           
print(F'valor_floats: {round(valor_floats * 10, 2)}')

print('---------------------------------------------------------')

# PARA ESTABELECER O VALOR DE INICIO E DE FIM

valor_uni = random.uniform(1,100)
print(f'Numero: {round(valor_uni, 3)}')

print('---------------------------------------------------------')

# UMA LISTA DE VALORES CRIADA E PREVIAMENTE CRIAR ALEATORIOS A PARTIR DELA 

L = [9,8,7,6,54,32,1,65,32,87,65,43]

n = random.choice(L)                                    # choice significa escolha
print(f'Numero escolhido: {n}')

print('---------------------------------------------------------')

# PARA EXTRAIR VARIOS VALORES DE DENTRO DESSA LISTA

num = random.sample(L,3)                                # sample signifca amostragem
print(f'Numeros escolhidos: {num}')

print('---------------------------------------------------------')

# PARA EMBARALHAR OS VALORES DA LISTA

print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-la: ')
num_emb = random.shuffle(L)                               # shuffle significa embaralhar
print(L)