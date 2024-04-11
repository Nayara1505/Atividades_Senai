#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. Altere o programa anterior para mostrar no final a soma dos números.

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))
soma = 0

for num in range(inicio, fim + 1):
    print(num)
    soma += num

print(f"Soma dos números: {soma}")
