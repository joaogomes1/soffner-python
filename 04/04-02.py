# 4. Escreva um programa que indica o número de dias de um mês escolhido pelo usuário.

mes = int(input("Informe um mês (no formato de número): "))

if ( mes == 2 ):
    print("28 ou 29 dias")
else:
    if ( mes == 4 or mes == 5 or mes == 7 or mes == 11 ):
        print("30 dias")
    else:
        if ( mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ):
            print("31 dias")
        else:
            print("Não existe um mês correspondente ao número [" + str(mes) + "]")

print('\n' + "[fim do programa]")
