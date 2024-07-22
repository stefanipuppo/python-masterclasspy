# CONDICIONAIS SIMPLES, COMPOSTO, ENCADEADO

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))


# Calcular a media aritmetica das notas
media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!')
    print('Parabéns!')
elif (media >= 5):
    print('Você está de recuperação')
else:
    print('Aluno reprovado')

#Esta é uma string formatada que utiliza o método format() para inserir o valor da variável media em um espaço reservado ({}) dentro da string.
print('Sua média é {}'.format(media))  # print(f'Sua média é {media}')    | pode ser usar assim tambem
