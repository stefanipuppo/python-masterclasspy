# Inicializa a variável  com o valor 0 (int)
media = 0  

# voce pode criar varias variaveis com o mesmo valor 0.0 (float)
n1 = n2 = n3 = n4 = 0.0  
 
# voce pode criar varias variaveis de uma vez só e colocar seu valores em ordem
nome, idade = 'Stef', 25 

# Tipo boleano
estado = True

# Função type() é uma função que retorna o tipo de um objeto em tempo de execução.
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j))                          # é numero complexo, geralmente usado em calculos 

# Função isinstance() é uma ocorrencia de uma determinada classe/tipo, ela retorna um valor verdadeiro se a variavel/dado for de uma determinado tipo que voce vao especificar e retornar falso se nao for 
a = 10
b = 'sol'
print(isinstance(a, int))
print(isinstance(a, (int, float)))  # tabem verefica se a variavel/valor e do tipo dentro de um conjunto de tipos