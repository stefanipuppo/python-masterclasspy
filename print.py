# Sintaxe significa qual é a forma correta de escrever algo
# Print(objeto, argumentos)

mensagem = 'função print()'
print(mensagem)
print('aula de python')

print('-------------------------------------------------')

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha.', end='')
print(' Continuo na mesma linha!')

print('-------------------------------------------------')

nome = 'Stef'
peso = 53
msg = f'Ola, meu nome é {nome} e eu peso {peso} quilos'
print(msg)

print('-------------------------------------------------')

a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)

print('-------------------------------------------------')

valor = 125.6789
print(f'O valor é {valor:.2f}')                        # :.2 | Para mostrar casas decimais que voce quer, arredonda o valor
print(f'O valor é \'{valor:.2f}\'')                    # Para adicionar caracteris de escape tipo '' quando for necessario

print('-------------------------------------------------')

seu_nome = 'Stefani'
sua_idade = 25
print(f'Nome:\t{seu_nome}\tIdade:\t{sua_idade}')                # Para colocar espaço maior
print(f'Nome:{seu_nome}\tIdade:{sua_idade}')  