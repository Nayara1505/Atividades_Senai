#Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_lado(self, novo_tamanho_lado):
        self.tamanho_lado = novo_tamanho_lado

    def retornar_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2
