# 7. Escreva um programa que apresente um menu de opções para a escolha do time de futebol favorito de alguém.

op = -1

while ( op < 1 or op > 5 ):

    print("\n1 - corinthians")
    print("2 - palmeiras")
    print("3 - santos")
    print("4 - são paulo")
    print("5 - juventus")

    op = input("Informe uma opção: ")
    
    if not( op.isdigit() ):
        op = -1         # Casts variable to an integer type, so that it can be evaluated again
                        # by the '<' and '>' operators, in the while loop.
                        # Assigns -1, to force a new iteration.
    else:               
        op = int(op)   
    
    # Prepares for new evaluaton, in the while loop.
            
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
    
print("\nO time escolhido é: " + time)
