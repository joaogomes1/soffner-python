# 22. Escreva um programa que calcule a área de um círculo de raio r, testando se o valor do raio é menor que zero.

# INPUT

raio = 0
while( raio <= 0 ):
    raio = int(input("Digite o raio: "))
# validar raio
    if ( raio <= 0 ):
        print("valor inválido")

# PROCESSING

# OUTPUT

print("área " + str(3.141592 * raio * raio))

