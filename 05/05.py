# 5. Escreva um programa que recebe a distância em KM percorrida por um carro e o consumo em litros, calculando depois o consumo médio.

dist = int(input("Informe a distância percorrida (Km): "))
lit = int(input("Informe o consumo (litros): "))
media = dist/lit

print("O consumo médio é: " + str(media) + " Km/litro")

print('\n' + "[fim do programa]")
