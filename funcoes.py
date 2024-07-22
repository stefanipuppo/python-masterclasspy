# Funçoes - Modularização, Reuso de Código, Legibilidade

"""
def <nome_função> ([argumentos]):
    <intruções>
"""

# Função sem argumentos

def mensagem():
    print('Boston Treinamentos em Tecnologia')
    print('Curso completo de Python')

mensagem()

print('---------------------------------------')

# Função com argumentos

def soma(a,b):
    print(a+b)

soma(12, 7)

print('---------------------------------------')

# TRABALHANDO COM RETURN

def mult(x,y):
    return x + y

a = 5
b = 8
c = mult(a,b)
print(f'O produto de {a} e {b} é {c}')

print('---------------------------------------')

def div(k,j):
    if j != 0:
        return k / j
    else: 
        return'Impossivel dividir por zero'

if __name__ == '__main__':
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))

    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')

print('---------------------------------------')

# Parâmetros opcionais, obrigatorio e valor padrao

def contar(num=11, caractere='+'):
    for i in range (1,num):
        print(caractere)

if __name__ == '__main__':
    contar(caractere='&')

