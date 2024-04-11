#Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os metodos para fazer as operacoes de incremento (de segundos) no horario e diferença ´entre dois horarios.
5. Crie uma classe que modele um carro 
(a) Atributos: marca, ano e preco 
(b) Metodos: mostrar preco e de exibicao dos dados

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1
                if self.hora == 24:
                    self.hora = 0

    def diferenca_horarios(self, outro_horario):
        segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca = abs(segundos_atual - segundos_outro)
        return f"A diferença entre os horários é de {diferenca // 3600} horas, {(diferenca % 3600) // 60} minutos e {diferenca % 60} segundos."

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return self.preco

    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: R${self.preco:.2f}"
