#Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.

def maior_valor(lista):

    return max(lista)

lista_numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
print("O maior valor na lista é:", maior_valor(lista_numeros))
