#Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(10):
    idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
    altura = float(input("Digite a altura do aluno {}: ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
alunos_contador = 0
for i in range(10):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_contador += 1

print("Número de alunos com mais de 13 anos e altura inferior à média:", alunos_contador)
