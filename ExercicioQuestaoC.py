"""
Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um
acréscimo de 8% de imposto.
"""
valorProduto = float(input("Digite o valor do produto: "))
valorAcrescimo = valorProduto * 0.08
precoFinal = valorProduto + valorAcrescimo

print("O preço final de um produto após o acréscimo de 8% de imposto é: ", precoFinal)