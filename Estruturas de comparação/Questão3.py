#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").lower()
if letra in 'aeiou':
    print("É uma vogal.")
else:
    print("É uma consoante.")
