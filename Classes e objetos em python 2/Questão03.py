#Crie uma classe representando os alunos de um determinado curso. A classe deve conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova. Crie metodos para acessar o nome e a media do aluno. ´ 
(a) Permita ao usuario entrar com os dados de 5 alunos. ´ 
(b) Encontre o aluno com maior media geral. ´ 
(c) Encontre o aluno com menor media geral ´ 
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
#aprovação. 

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

alunos = []
for i in range(5):
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    nota3 = float(input("Digite a nota da terceira prova: "))
    aluno = Aluno(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

maior_media = alunos[0]
menor_media = alunos[0]

for aluno in alunos:
    if aluno.calcular_media() > maior_media.calcular_media():
        maior_media = aluno
    if aluno.calcular_media() < menor_media.calcular_media():
        menor_media = aluno

print(f"O aluno com maior média é: {maior_media.nome}, com média: {maior_media.calcular_media()}")
print(f"O aluno com menor média é: {menor_media.nome}, com média: {menor_media.calcular_media()}")

for aluno in alunos:
    print(f"O aluno {aluno.nome} está {aluno.verificar_aprovacao()}.")
