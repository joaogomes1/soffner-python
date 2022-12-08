# 4. Escreva um programa que indica o número de dias de um mês escolhido pelo usuário.

mes = input("Informe um mês: ")

if ( mes == "fevereiro" ):
    print("28 ou 29 dias")
else:
    if ( mes == "abril" or mes == "junho" or mes == "setembro" or mes == "novembro" ):
        print("30 dias")
    else:
        if ( mes == "janeiro" or mes == "março" or mes == "maio" or mes == "julho" or mes == "agosto" or mes == "outubro" or mes == "dezembro" ):
            print("31 dias")
        else:
            print("Não existe um mês chamado [" + mes + "]")

print('\n' + "[fim do programa]")
