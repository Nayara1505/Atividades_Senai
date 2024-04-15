#Faça um Programa que leia três números e mostre-os em ordem decrescente

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros_ordem_decrescente = sorted([num1, num2, num3], reverse=True)
print(f"Números em ordem decrescente: {numeros_ordem_decrescente}")
