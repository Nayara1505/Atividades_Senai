#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
for i in range(10):
    num = int(input("Digite um número inteiro para a posição {}: ".format(i)))
    vetor.append(num)

soma_quadrados = sum(x ** 2 for x in vetor)
print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
