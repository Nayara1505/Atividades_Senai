#A série de Fibonacci é formada pela seqüência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o valor de n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
