lista = [2,6,9,4,0,12,3,7]

for item in lista:
    print(item)

print('---------------------------')

palavra = 'Stefani'
for letra in palavra:
    print(letra)

print('---------------------------')

for numero in range(1,11):      # range(faixa) |faixa de valores, nesse caso imprimi do 1 ao 10
    print(numero)

print('---------------------------')

nome = input('Digite seu nome: ')
for x in range(10):
    print(f'{x+1} {nome}')

print('---------------------------')

# range(valor_inicial, valor_final, incremento) o ultimo numero nunca entra

for x in range (2,21,3):
    print(x)

print('---------------------------')

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina') #tuplas

for pedra in pedras:
    if pedra == 'Quartzo':
        continue                     #encerra a iteraçao atual do laço, vai mostrar tudo na lista menos o quartzo
    print(pedra)