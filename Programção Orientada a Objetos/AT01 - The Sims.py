import time
import sys

class Pessoa:
    def _init_(self, nome, idade, altura, peso, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.falando = False
        self.dormindo = False
        self.comendo = False
        self.andando = False

    def falar(self, fala):
        self.dormindo = False
        self.comendo = False
        self.falando = True
        print(f"{self.nome} está falando: {fala}.\n")

    def andar(self, destino):
        self.dormindo = False
        self.andando = True
        print(f"{self.nome} está indo para: {destino}.\n")

    def dormir(self, onde):
        self.falando = False
        self.andando = False
        self.comendo = False
        self.dormindo = True
        print(f"{self.nome} está dormindo em: {onde}.\n")

    def comer(self, alimento):
        self.dormindo = False
        self.falando = False
        self.comendo = True
        print(f"{self.nome} está comendo: {alimento}.\n")


def Tela_Inicial():
    parar = False
    while not parar:
        escolha = int(input("""
                  ____
                 | The Sims |
                  ----------
             1 - Criar Personagem.
             2 - Sair do Jogo.

              >> """))
        if escolha == 1:
            Criar_person()
        elif escolha == 2:
            print("Encerrando o Jogo...")
            time.sleep(3)
            sys.exit()
        else:
            print(f"A opção {escolha} não existe. Selecione uma opção correta.")
            time.sleep(3)

def Rotina(pessoa):
    rotina = False
    while not rotina:
        print(f"{pessoa.nome} {'está' if pessoa.andando else 'não está'} andando")
        print(f"{pessoa.nome} {'está' if pessoa.dormindo else 'não está'} dormindo")
        print(f"{pessoa.nome} {'está' if pessoa.falando else 'não está'} falando")
        print(f"{pessoa.nome} {'está' if pessoa.comendo else 'não está'} comendo")
        acao = int(input("""
         O que a pessoa vai fazer?

          1 - Andar.
          2 - Dormir.
          3 - Comer.
          4 - Falar.

          >> """))
        print("")
        if acao == 1:
            destino = input("Andar para onde? \n >> ")
            pessoa.andar(destino)
        elif acao == 2:
            local = input("Dormir aonde?\n >> ")
            pessoa.dormir(local)
        elif acao == 3:
            alimento = input("Comer o que?\n >> ")
            pessoa.comer(alimento)
        elif acao == 4:
            fala = input("Falar o que?\n >> ")
            pessoa.falar(fala)
        else:
            print(f"A opção {acao} não existe. Selecione uma opção válida.")
            time.sleep(3)
            rotina = True

def Criar_person():
    print(" --- Criando Personagem --- ")
    nome = input(" Nome: ")
    idade = int(input(" Idade: "))
    altura = float(input(" Altura: "))
    peso = float(input(" Peso: "))
    genero = input(" Gênero: ")

    novo_pessoa = Pessoa(nome, idade, altura, peso, genero)
    print(" Personagem Criado com Sucesso.\n")
    print(f" Nome: {nome}.")
    print(f" idade: {idade}.")
    print(f" Altura: {altura}.")
    print(f" Peso: {peso}.")
    print(f" Gênero: {genero}.\n\n")
    Rotina(novo_pessoa)

Tela_Inicial()
