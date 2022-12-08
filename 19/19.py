# 19. Escreva um programa que teste uma dada senha.

senha = 2002

# INPUT
# mode 1
while (1):
    s = int(input("digite a senha: "))
    if ( s == senha ):
        print("access granted")
        break
    else:
        print("access denied")

