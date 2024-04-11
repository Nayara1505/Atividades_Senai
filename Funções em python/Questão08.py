#Escreva uma função chamada imprime_tabuada que aceita um número inteiro como parâmetro e imprime a tabuada desse número de 1 a 10.

def imprime_tabuada(numero):

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero_input = int(input("Digite um número para imprimir sua tabuada: "))
imprime_tabuada(numero_input)
