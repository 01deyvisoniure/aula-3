Etanol=4.90
gasolina=5.80

litro=float(input("digite a quantidade de litros:"))
combustivel=input("E-etanol(R$4.90)\nG-gasolina(R$5.80)\ndigite qual o combustivel:")
if combustivel=="e" or combustivel=="E":
    valor_etanol = litro * Etanol
    print(f"R${valor_etanol}")
else:
    if combustivel=="g" or combustivel=="G":
        valor_gasolina = litro * gasolina
        print(F"R${valor_gasolina}")
    else:
        print("esse combustivel não existe")

