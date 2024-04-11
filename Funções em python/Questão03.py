#Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.


def verifica_primo(numero):

    if numero <= 1:
        return False

    elif numero <= 3:
        return True

    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:

        i = 5

        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

numero = int(input("Digite um número para verificar se é primo: "))
print("O número", numero, "é primo?" , verifica_primo(numero))
