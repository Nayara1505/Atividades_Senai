#Faça um programa, utilizando , que peça para o usuário  o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

produtos = {}

for i in range(3):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[produto] = preco

print("Produtos e seus preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")
