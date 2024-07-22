nome = None         #variavel vazia

while True:
    print('Digite seu nome, ou x para parar')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo(a), {nome}')
print('Até logo!')