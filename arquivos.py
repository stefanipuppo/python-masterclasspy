# Manipulação de arquivo de texto

'''
Modos de acesso a arquivos com open()

MODO              -        SIGNIFICADO

r                 -        Somente leiturua
r+                -        Leitura e escrita. O texto é inserido no inicio do arquivo
w                 -        Escrita, apagando(truncando) o conteudo existente no arquivo
w+                -        Leitura e escrita. O arquivo é criado, se não exister; se existir, é truncado. O texto é inseiro no inicio do arquivo
a                 -        Escrita, preservando o conteudo existente(append). O arquivo é criado, se nao existir. O texto é inserido no final do arquivo.
b                 -        Modo binario
+                 -        Atualização - leitura e escrita
x                 -        Abre o arquivo para a criação excluisiva, falhando se o arquivo ja existir
'''

manipulador = open('arquivo.txt', 'r', encoding='utf-8')
print(f'\Método readline(): \n')
print(manipulador.readline())



try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        print(linha)
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()
