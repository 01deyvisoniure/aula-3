nome=input("digite o seu  nome: ")
idade= int(input("digite a sua idade: "))
salario=float(input("digite seu salario: "))

print(f"nome: {nome}\nidade: {idade}\nsalario: R$ {salario}")
if salario <= 1200:
    print("----- tu é pobre -----")
else:
    print("----- da pra viver -----")

