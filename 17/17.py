# 17. Escreva um programa que informe a categoria de um jogador de futebol, considerando sua idade: infantil (até 13 anos), juvenil (até 17 anos) ou sênior (acima de 17 anos).

categoria = ""

# INPUT
idade = int(input("informe a idade: "))

# PROCESSING
if ( idade <= 13 ):
    categoria = "infantil"
elif ( idade <= 17 ):
    categoria = "juvenil"
else:
    categoria = "sênior"

# OUTPUT
print("categoria: " + categoria)

