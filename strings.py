# String são imutaveis

frase = 'Vamos aprender Python hoje'
palavras = frase.split()                    # Split divide as string em partes, separa por espaços criando assim uma lista de strings
print(palavras)

print('---------------------------------------')

print(palavras[1])                          # Consegue acessar palvras individuas acessando por indice

print('---------------------------------------')


for palavra in palavras:                    # Pode fazer uma iteração usando for, extrai informaçao de dentro de uma frase separando assim suas palavras constituintes
    print(palavra)

print('---------------------------------------')


for letra in frase:                         # separa por letras
        print(letra)

print('---------------------------------------')

print(frase[6:15])                          # faz o fatiamento de uma frase

print('---------------------------------------')

email = input('Digite seu endereço de email: ')
arroba = email.find('@')                    # para encontrar o caratcer desejado
print(arroba)
usuario = email[0:arroba]                   # retorna o primeiro caracter ate chegar na posição desejada
dominio = email[arroba+1:]                  # retorna o valor da posiçaõ desejada até o ultimo valor
print(usuario)
print(dominio) 

print('---------------------------------------')

# OPERADORES DE ASSOCIAÇÃO                 # verifica se um caracter ou uma sequencia de caracteres estão dentro da string

produtos = 'Carbonado de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' in produtos)
print('magnésio' not in produtos)

print('---------------------------------------')

# ENCONTRANDO A POSIÇÃO DE UMA SUBSTRING

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

# TRABALHANDO COM MAIUSCULOS E MINUSCULOS

print('---------------------------------------')

objeto_celeste = 'galaxia esPiral M31'
print(objeto_celeste.upper())                                 # Tudo maiusculo
print(objeto_celeste.lower())                                 # Tudo minusculo
print(objeto_celeste.capitalize())                            # Somente a primeira letra em maiusculo
print(objeto_celeste.title())                                 # Cada letra de cada palavraem maiusculo

print('---------------------------------------')

suplemento = 'cloreto de magnesio'
n_suplemento = suplemento.replace('magnesio', 'zinco')        # Replace significa substituir
print(suplemento)
print(n_suplemento)

print('---------------------------------------')

# TRABALHANDO COM ESPAÇOS EM BRANCO

frase = '     Ômega 3 é bom para a saúde!'
print(frase.lstrip())                                         # l de left, esquerda
print(frase.rstrip())                                         # r de rigth, direita
print(frase.strip())                                          # tanto esquerda quanto direita

print('---------------------------------------')

# ALINHAMENTO DE TEXTO PARA EXIBIÇÃO

fruta = 'Abatece'
print(fruta)
print(fruta.rjust(20))                                        # justifica a variavel para direita argumentando a quantidade de espaço desejado
print(fruta.center(20))                                       # centraliza a variavel
print(fruta.ljust(20))                                        # justifica a variavel para esquerda (padrão)
print(fruta.center(20, '-'))                                  # duas argumentações, para prencher o espaço

print('---------------------------------------')

# PREFIXOS E SUFIXOS

p = 'Bóson Treinamentos'            # verificar se a string inicia ou termina com uma sequencia de caracter qualquer
print(p.startswith('B'))            # startwith significa "começa com"
print(p.endswith('s'))              # endswith significa "finaliza com"

# DOCSTRINGS                        DOCUMENTA TRECHOS ESPECIFICOS DO CODIGO COMO MODULO, CLASSE, FUNÇÃO

"""
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classe no python, entre outros locais.
    Respeita deslocamento do texto e é    multilinhas
"""