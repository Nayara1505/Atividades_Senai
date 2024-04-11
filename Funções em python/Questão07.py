#Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números.

def soma_quadrados(lista):

    return sum(x**2 for x in lista)

lista_numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
soma_quadrados_resultado = soma_quadrados(lista_numeros)
print("A soma dos quadrados dos números na lista é:", soma_quadrados_resultado)
