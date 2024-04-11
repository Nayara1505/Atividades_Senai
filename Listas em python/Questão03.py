#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []

for i in range(10):
    num1 = int(input("Digite um número para o vetor 1 na posição {}: ".format(i)))
    num2 = int(input("Digite um número para o vetor 2 na posição {}: ".format(i)))
    vetor1.append(num1)
    vetor2.append(num2)

vetor3 = [None] * 20
for i in range(10):
    vetor3[2*i] = vetor1[i]
    vetor3[2*i + 1] = vetor2[i]

print("Terceiro vetor intercalado:", vetor3)
