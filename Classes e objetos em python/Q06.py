#1. Crie uma classe que modele uma pessoa 
(a) Atributos: nome, idade e endereço 
(b) Metodos: mostrar endereço e alterar endereço

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        return self.endereco

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
