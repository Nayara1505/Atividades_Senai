while True:
    comando = input("Digite 'start' para exibir a sequência de números ou 'stop' para sair: ")
    
    if comando.lower() == 'start':
        numero = input("Digite um número ou deixe em branco para exibir de 1 até 10: ")
        try:
            if numero == '':
                for i in range(1, 11):
                    print(i)
            else:
                limite = int(numero)
                for i in range(1, limite + 1):
                    print(i)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    elif comando.lower() == 'stop':
        print("Programa encerrado.")
        break
    else:
        print("Comando inválido. Por favor, digite 'start' ou 'stop'.")
