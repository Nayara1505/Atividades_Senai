#Crie uma classe que modele uma aluno 
(a) Atributos: nome, numero de matrıcula e curso 
(b) Metodos: mostrar curso e alterar curso ´ 

class Aluno:
    def __init__(self, nome, numero_matricula, curso):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.curso = curso

    def mostrar_curso(self):
        return self.curso

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
