#Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisor:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 10  # Definindo o volume inicial como 10

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print(f"Canal alterado para {novo_canal}.")
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print("Volume máximo alcançado.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print("Volume mínimo alcançado.")


# Função principal
def main():
    tv = Televisor()

    while True:
        print("\nControle Remoto:")
        print("1 - Mudar canal")
        print("2 - Aumentar volume")
        print("3 - Diminuir volume")
        print("0 - Desligar TV")

        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            novo_canal = int(input("Informe o número do canal: "))
            tv.mudar_canal(novo_canal)
        elif opcao == "2":
            tv.aumentar_volume()
        elif opcao == "3":
            tv.diminuir_volume()
        elif opcao == "0":
            print("Desligando a TV...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
