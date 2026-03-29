"""
Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor
da hora trabalhada, calculando o salário total.
"""

horasTrabalhadas = float(input("Quantas horas vocÊ trabalha por dia?"))
valorHoras = float(input("Qual o valor de sua hora trabalhada?"))

salarioTotal = ((horasTrabalhadas * valorHoras) * 5) * 4

print("Seu salário baseando-se em cinco dias de trabalho em quatro semanas é: ", salarioTotal)