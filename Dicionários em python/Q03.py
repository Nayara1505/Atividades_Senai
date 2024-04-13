#Faça um programa, utilizando  que peça para o usuário  quatro notas e mostre na tela as notas e a média entre elas.
Exemplo 3

notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média das notas:", media)
