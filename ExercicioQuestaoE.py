"""
Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
Corporal (IMC).
"""

alturaUsuario = float(input("Digite sua altura: "))
pesoUsuario = float(input("Digite o seu peso: "))

formulaIMC = pesoUsuario / alturaUsuario ** 2

print("O resultado do cálculo de seu IMC é igual a: ", formulaIMC)
