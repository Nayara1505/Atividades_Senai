#Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if len(self.bucho) == 0:
            print(f"{self.nome} está com o bucho vazio.")
        else:
            print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")

    def digerir(self):
        if len(self.bucho) == 0:
            print(f"{self.nome} não tem nada para digerir.")
        else:
            print(f"{self.nome} está digerindo {self.bucho.pop(0)}.")


macaco1 = Macaco("Chico")
macaco2 = Macaco("Jorge")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Pêssego")

macaco2.comer("Cenoura")
macaco2.comer("Abacaxi")
macaco2.comer("Melancia")

macaco1.ver_bucho()
macaco2.ver_bucho()

macaco1.digerir()
macaco2.digerir()

macaco1.ver_bucho()
macaco2.ver_bucho()

# Tentativa de fazer um macaco comer o outro
macaco1.comer(macaco2.nome)

macaco1.ver_bucho()
macaco2.ver_bucho()
