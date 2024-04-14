class Animal:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Som aleatório.")

    def mover(self):
        print("O animal está andando")

    def dormir(self):
        print("O animal está dormindo")


class Dog(Animal):
    def _init_(self, nome, idade, raca):
        super()._init_(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print("Au au!")

    def abanar_rabo(self):
        print("O cachorro está abanando o rabo")

    def farejar(self):
        print("O cachorro está farejando")

dog1 = Dog("Rex", 3, "Labrador")

print(f"Nome: {dog1.nome}")
print(f"Idade: {dog1.idade}")
print(f"Raça: {dog1.raca}")

dog1.emitir_som()
dog1.abanar_rabo()
dog1.farejar()
dog1.mover()
dog1.dormir()
