#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

produto_mais_barato = min(preco_produto1, preco_produto2, preco_produto3)
print(f"Você deve comprar o produto mais barato, que custa: {produto_mais_barato}")
