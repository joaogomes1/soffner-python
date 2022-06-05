# 3. Escreva um programa que recebe o ano de nascimento de uma pessoa, calcula sua idade e diz se é maior de idade.

# input
nasc = int( input("Informe seu ano de nascimento: ") ) # year of birth
ano_atual = int(2022) # current year

if ( ano_atual - nasc ) >= 18:
    print("Você é maior de idade")

print("\nFim do programa")
input("Aperte [ENTER] para sair...")
