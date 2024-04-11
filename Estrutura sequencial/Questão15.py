15. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

cobertura_por_litro = 3  # metros quadrados
capacidade_lata = 18  # litros
preco_lata = 80.00  # em reais

area_a_ser_pintada = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area_a_ser_pintada / cobertura_por_litro

latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)

preco_total = latas_necessarias * preco_lata

print("Quantidade de latas de tinta necessárias:", latas_necessarias)
print("Preço total: R$", preco_total)
