# 25. Escreva um programa que calcule as raízes da equação do 2o grau (ax² + bx + c); os valores de a, b e c são fornecidos pelo usuário (veja a proposta de resolução mais adiante).

import math

# INPUT

a = float(input("informe a: "))
b = float(input("informe b: "))
c = float(input("informe c: "))

# PROCESSING

discriminante = ( (b ** 2) - (4 * a * c) )
raiz_1 = ( (-b + math.sqrt(discriminante)) / (2 * a) )
raiz_2 = ( (-b - math.sqrt(discriminante)) / (2 * a) )

# OUTPUT
print("r_1 " + str(raiz_1) + '\n' + "r_2 " + str(raiz_2))

