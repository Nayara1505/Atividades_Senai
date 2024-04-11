#Faça um programa para imprimir:
1
 2 2
 3 3 3
.....
 n n n n n n ... n


def imprimir_padrao(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)

n = int(input("Digite um número inteiro para imprimir o padrão: "))

imprimir_padrao(n)
