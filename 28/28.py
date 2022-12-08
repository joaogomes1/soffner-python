# 28. Escreva um programa que conceda um aumento de 10% ao salário dos funcionários de uma empresa, os quais recebem até R$ 1.000,00.

# INPUT

sal = float(input("informe o salário: $"))

# PROCESSING

# OUTPUT
if ( sal <= 1000 ):
    print("novo sal: $" + str(sal * 1.1))

