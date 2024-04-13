class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo="0", limite="0"):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = float(saldo)
        self.limite = float(limite)
        self.conta_ativa = True  # Assuming the account is active by default

    def sacar(self, valor):
        if self.conta_ativa:
            if self.saldo + self.limite >= valor:
                self.saldo -= valor
                print("Saque de", valor, "realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta bloqueada. Não é possível realizar saques.")

    def depositar(self, valor):
        if self.conta_ativa:
            self.saldo += valor
            print("Depósito de", valor, "realizado com sucesso.")
        else:
            print("Conta bloqueada. Não é possível realizar depósitos.")

    def desbloquear(self):
        self.conta_ativa = True
        print("Conta desbloqueada.")

    def bloquear(self):
        self.conta_ativa = False
        print("Conta bloqueada.")

    def verificar_saldo(self):
        if self.conta_ativa:
            print("Saldo atual:", self.saldo)
        else:
            print("Conta bloqueada.")

    def mudar_limite(self, novo_limite):
        if self.conta_ativa:
            self.limite = float(novo_limite)
            print("Limite alterado para", novo_limite, "com sucesso.")
        else:
            print("Conta bloqueada. Não é possível alterar o limite.")

titular = input("Digite o nome do titular da conta: ")
numero_conta = input("Digite o número da conta: ")
saldo_inicial = input("Digite o saldo inicial da conta: ")
limite_inicial = input("Digite o limite inicial da conta: ")

conta = ContaBancaria(titular, numero_conta, saldo=saldo_inicial, limite=limite_inicial)

while True:
    print("\nEscolha uma opção:")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Bloquear")
    print("4. Desbloquear")
    print("5. Verificar Saldo")
    print("6. Mudar Limite")
    print("7. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        valor = float(input("Digite o valor que deseja sacar: "))
        conta.sacar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor que deseja depositar: "))
        conta.depositar(valor)
    elif opcao == '3':
        conta.bloquear()
    elif opcao == '4':
        conta.desbloquear()
    elif opcao == '5':
        conta.verificar_saldo()
    elif opcao == '6':
        novo_limite = input("Digite o novo limite da conta: ")
        conta.mudar_limite(novo_limite)
    elif opcao == '7':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


    #Digite o nome do titular da conta: lucas
    #Digite o número da conta: 123456
    #Digite o saldo inicial da conta: 1500
    #Digite o limite inicial da conta: 3000

    #Escolha uma opção:
    #1. Sacar
    #2. Depositar
    #3. Bloquear
    #4. Desbloquear
    #5. Verificar Saldo
    #6. Mudar Limite
    #7. Sair
    #Digite o número da opção desejada: 1
    #Digite o valor que deseja sacar: 700
    #Saque de 700.0 realizado com sucesso.

    #Escolha uma opção:
    #1. Sacar
    #2. Depositar
    #3. Bloquear
    #4. Desbloquear
    #5. Verificar Saldo
    #6. Mudar Limite
    #7. Sair
    #Digite o número da opção desejada: 
