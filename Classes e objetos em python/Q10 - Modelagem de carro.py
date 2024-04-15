#Crie uma classe que modele um carro 
(a) Atributos: marca, ano e preco 
(b) Metodos: mostrar preco e de exibicao dos dados  

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco
    
    def mostrar_preco(self):
        print("Preço do carro:", self.preco)
    
    def exibir_dados(self):
        print("Marca:", self.marca)
        print("Ano:", self.ano)
        print("Preço:", self.preco)

carro1 = Carro("Toyota", 2020, 35000)
carro1.exibir_dados()
carro1.mostrar_preco()
