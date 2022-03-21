userInput = input("Informe um número: ")

if int(userInput) > 0:
    print("O número informado é maior que zero.")
elif int(userInput) < 0:
    print("O número informado é menor que zero.")
else:
    print("O número informado é zero.")