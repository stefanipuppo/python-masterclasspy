# Escopo indica a visibilidadecde uma variavel dentro do codigo, onde essa variavel é visivel e acessivel

# Escopo Global é criada fora das funções e pode ser acessada em toda parte do codigo

# Escopo Local é criada dentro de uma função e existe somente dentro dessa função onde foi declarada sendo inicializada toda vez que a função for chamada
# ou seja, uma variavel que funciona localmente somente dentro da função

var_global = 'Curso completo de python'

def escreve_texto():
    var_local = 'Fabio dos reis'
    var_global = 'Banco de dados SQL'
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessae as variaveis diretamente')
    print(f'Variavel Global: {var_global}')
