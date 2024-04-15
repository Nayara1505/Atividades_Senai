#Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


def calcular_pisos_e_rodapes(retangulo, tamanho_piso, altura_rodape):
    area_pisos = retangulo.calcular_area()
    perimetro_retangulo = retangulo.calcular_perimetro()

    area_rodapes = perimetro_retangulo * altura_rodape

    quantidade_pisos = area_pisos / tamanho_piso
    quantidade_rodapes = area_rodapes / tamanho_piso

    return quantidade_pisos, quantidade_rodapes

if __name__ == "__main__":
    lado_a = float(input("Informe o comprimento do local: "))
    lado_b = float(input("Informe a largura do local: "))
    tamanho_piso = float(input("Informe o tamanho do piso: "))
    altura_rodape = float(input("Informe a altura do rodapé: "))

    local = Retangulo(lado_a, lado_b)

    quantidade_pisos, quantidade_rodapes = calcular_pisos_e_rodapes(local, tamanho_piso, altura_rodape)

    print(f"Quantidade de pisos necessários: {quantidade_pisos}")
    print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")
