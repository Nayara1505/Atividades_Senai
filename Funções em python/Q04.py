#Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.

def inverte_string(string):

    return string[::-1]

string_original = input("Digite uma string para inverter: ")
string_invertida = inverte_string(string_original)
print("A string invertida é:", string_invertida)
