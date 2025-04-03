Etanol=4.90
gasolina=5.80

litro=float(input("digite a quantidade de litros:"))
combustivel=float(input("1-etanol(R$4.90)\n2-gasolina(R$5.80)\ndigite qual o combustivel:"))
if combustivel==1:
    valor_etanol = litro * Etanol
    print(f"R${valor_etanol}")
else:
    if combustivel==2:
        valor_gasolina = litro * gasolina
        print(F"R${valor_gasolina}")
    else:
        print("esse combustivel não existe")

