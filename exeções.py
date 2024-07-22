# Exeção é um objeto que representa um erro que ocorreu ao executar um programa
# Blocos try ... except

"""
Exception - Classe base para todas as exceções

ArithmeticError - Classe base para todos os erros que ocorrem em calculos numericos

OverflorError - Um calculo excedeu o limite maximo de um tipo numerico

ZeroDivisionError - Lançada quando uma divisao ou módulo por zero é executada em tipos numéricos

ImportError - Um identificador(nome) não foi encontrado no namespace local ou global 

IOError - Ocorre quando uma operação de E/S, como ler ou escrever em um arquivo, falha.

IndentationError - A identação  nao foi aplicada corretamente

RecursionError - O interpredator detectou que a profundidade maxima de recursao foi exibida

TypeError - Lançada quando uma funçao ou operador é invalido para tipo de dados especificos
"""

# Tratamento de divisão por zero

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

try:                                                    
    r = round(n1 / n2, 2)
except ZeroDivisionError:
    print(f'Não é possivel dividir por zero!')
else: 
    print(f'Resultado: {r}')


print('---------------------------')

def div(k,j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite outro numero: '))
            break
        except ValueError:
            print('Ocorreu um erro ao leo o valor, tente novamente')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
         print(f'Não é possivel dividir por zero!')
    except:
        print('Ocorreu um erro desconhecido..')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'fim do calculo')
        