# 16. Escreva um programa que resolva o seguinte problema: uma cópia “xerox” custa R$ 0,25 por folha, mas acima de 100 folhas esse valor cai para R$ 0,20 por unidade. Dado o total de cópias, informe o valor a ser pago.

# INPUT
copias = int(input("informe a quantidade de cópias: "))
total = 0

# CÁLCULO

# modo 1
#for i in range(copias):
#    if ( i < 100 ):
#        total += 0.25
#    else:
#        total += 0.20

# modo 2
if ( copias <= 100 ):
    total = copias * 0.25
else:
    total = (copias - 100) * 0.20 + 100 * 0.25

# OUTPUT
print("total: " + str(total))

