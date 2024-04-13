#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

print ("Digite 2 números inteiros e 1 número real")
num1 = int (input ("primeiro valor: "))
num2 = int (input ("Segundo valor: "))
num3 = float (input ("terceiro valor: "))

produto = (num1 * 2) + (num2 / 2)
soma = (num1 * 3) + (num3 * 3)
cubo = num3 ** 3

print (f"produto: {produto}")
print (f"soma: {soma}")
print (f"cubo: {cubo}")
