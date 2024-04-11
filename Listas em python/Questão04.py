#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    num1 = int(input("Digite um número para o vetor 1 na posição {}: ".format(i)))
    num2 = int(input("Digite um número para o vetor 2 na posição {}: ".format(i)))
    num3 = int(input("Digite um número para o vetor 3 na posição {}: ".format(i)))
    vetor1.append(num1)
    vetor2.append(num2)
    vetor3.append(num3)

vetor_final = []
for i in range(10):
    vetor_final.append(vetor1[i])
    vetor_final.append(vetor2[i])
    vetor_final.append(vetor3[i])

print("Vetor final intercalado:", vetor_final)
