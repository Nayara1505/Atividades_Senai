#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

print ("Conversão de temperatura")
fahrenheit = float (input ("Valor em fahrenheit: "))
celsius = 5 * ((fahrenheit - 32)/9)
print (f"Valor em celsius {celsius}")
