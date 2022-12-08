# 23. Escreva um programa que receba um número inteiro do teclado e diga se ele é par. Dica: Um número é par se o resto da divisão dele por 2 for zero - usar o operador % de resto da divisão.

# INPUT

n1 = int(input("Digite um número inteiro: "))

# PROCESSING

# OUTPUT
if ( not(n1%2) ):
    print("par")
else:
    print("ímpar")

