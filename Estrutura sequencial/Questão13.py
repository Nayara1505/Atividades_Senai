#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a fórmula abaixo:
Salário Bruto : R −IR(11  - INSS (8%) : R −Sindicato(5  = Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = ganho_por_hora * horas_trabalhadas
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"Salário Bruto: R$ {salario_bruto}, IR: R$ {ir}, INSS: R$ {inss}, Sindicato: R$ {sindicato}, Salário Líquido: R$ {salario_liquido}")
