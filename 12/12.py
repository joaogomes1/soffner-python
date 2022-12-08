# 12. Dado um valor em reais e a cotação do dólar, converta esse valor para dólares.

dolar = 5.224

reais = float(input("informe o valor em reais: BRL "))
print("valor convertido: USD " + str(round(reais / dolar, 3)))

