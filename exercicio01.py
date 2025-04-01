nome=input("digite o seu  nome: ")
idade= int(input("digite a sua idade: "))
salario=float(input("digite seu salario: "))
percentual= int(input("digite o aumento percentual do seu salario: "))
aumento= (salario*percentual)/100
salario_final= salario+aumento
print(f"olá {nome}, você tem {idade} anos, seu salario antigo é {salario}, com um acrescimo de {percentual}%\n seu novo salario é {salario_final}")
print(f"----------------------------------------")
print(f"> nome: {nome}")
print(f"> idade: {idade}")
print(f"> salario: R${salario:.2f}")
print(f"> percentual de aumento: {percentual}%")
print(f"> novo salario: R${salario_final:.2f}")
print(f"----------------------------------------")

