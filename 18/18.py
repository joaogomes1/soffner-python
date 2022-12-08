# 18. Escreva um programa que diga qual é o maior de dois números distintos recebidos do usuário.

maior = 0.0

# INPUT
n1 = float(input("informe um número: "))
n2 = float(input("informe outro número (diferente do primeiro): "))

# PROCESSING
if ( n1 > n2 ):
    maior = n1
else:
    maior = n2

# OUTPUT
print("maior: " + str(maior))

