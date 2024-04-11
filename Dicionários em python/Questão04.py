#Faça um programa, utilizando , que:
1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
2° Passo: Peça para o usuário  um número.
3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa = []

for i in range(4):
    item = input(f"Insira o {i + 1}º item na Caixa Misteriosa: ")
    caixa_misteriosa.append(item)

numero = int(input("Digite um número de 1 a 4: "))
print("Item na posição selecionada:", caixa_misteriosa[numero - 1])
