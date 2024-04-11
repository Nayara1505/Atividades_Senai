#Faça um programa que leia 5 números e informe o maior número.

numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(5)]
maior_numero = max(numeros)
print(f"O maior número é: {maior_numero}")
