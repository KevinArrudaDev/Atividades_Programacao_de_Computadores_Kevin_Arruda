"""
Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o
resultado final.
"""

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))
terceiroNumero = float(input("Digite o terceiro número: "))
quartoNumero = float(input("Digite o quarto número: "))
quintoNumero = float(input("Digite o quinto número: "))

mediaAritmetica = (primeiroNumero + segundoNumero + terceiroNumero + quartoNumero + quintoNumero) / 5

print("A média aritmética entre as notas é: ", mediaAritmetica)