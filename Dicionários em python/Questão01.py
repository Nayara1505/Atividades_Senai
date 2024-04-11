#Faça um programa que possua um, adicione elementos ao dicionário e os mostre na tela.

dicionario = {}

def adicionar_elemento(chave, valor):
    dicionario[chave] = valor

def mostrar_dicionario():
    print("Elementos do dicionário:")
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

adicionar_elemento("chave1", "valor1")
adicionar_elemento("chave2", "valor2")
mostrar_dicionario()
