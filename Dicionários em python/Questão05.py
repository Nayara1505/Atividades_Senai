#Faça um programa, utilizando , que:
1° Passo: Peça para o usuário  o nome de três funcionários e os mostre na tela.
2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.

funcionarios = []

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º funcionário: ")
    funcionarios.append(nome)

print("Funcionários:", funcionarios)

demitido = input("Digite o nome do funcionário a ser demitido: ")
if demitido in funcionarios:
    funcionarios.remove(demitido)

print("Funcionários restantes:", funcionarios)
