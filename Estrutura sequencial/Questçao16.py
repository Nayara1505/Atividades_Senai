
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00ouemgalõesde3,6litros,quecustamR  25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metros_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_tinta = metros_quadrados / 6
latas = litros_tinta / 18
galoes = litros_tinta / 3.6
latas_cheias = int(latas)
galoes_cheios = int(galoes)
preco_latas = latas_cheias * 80
preco_galoes = galoes_cheios * 25
preco_misto = (latas_cheias * 80) + (galoes_cheios * 25)
print(f"Latas de 18 litros: {latas_cheias}, Preço: R$ {preco_latas}")
print(f"Galões de 3,6 litros: {galoes_cheios}, Preço: R$ {preco_galoes}")
print(f"Misto (latas e galões): {latas_cheias} latas, {galoes_cheios} galões, Preço: R$ {preco_misto}")
