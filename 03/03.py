# 3. Escreva um programa que recebe o ano de nascimento de uma pessoa, calcula sua idade e diz se é maior de idade.

# input
nasc = int(input("Informe um ano de nascimento: "))
ano_atual = 2022 # current year

if ( ano_atual - nasc ) >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")

print('\n' + "[fim do programa]")
# input("Aperte [ENTER] para sair...")
