# 7. Escreva um programa que apresente um menu de opções para a escolha do time de futebol favorito de alguém.

# menu
while (True):
    print("\n1 - corinthians")
    print("2 - palmeiras")
    print("3 - santos")
    print("4 - são paulo")
    print("5 - juventus")

    op = int(input("\nInforme uma opção: "))

    if ( op < 1 or op > 5 ):
        print("Opção inválida")
        input("Pressione ENTER para continuar...")
        continue
    else:
        break

# switch
if op == 1:
    time = "corinthians"
elif op == 2:
    time = "palmeiras"
elif op == 3:
    time = "santos"
elif op == 4:
    time = "são paulo"
else:
    time = "juventus"

# output    
print("\nO time escolhido é: " + time)

print('\n' + "[fim do programa]")
