#Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento.

def fatorial(numero):

    if numero < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo."

    elif numero == 0 or numero == 1:
        return 1

    else:
        fat = 1
        for i in range(2, numero + 1):
            fat *= i
        return fat

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print("O fatorial de", numero, "é:", fatorial(numero))
