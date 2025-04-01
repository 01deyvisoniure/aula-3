n1=float(input("digite a primeira nota: "))
n2=float(input("digite a segunda nota: "))
n3=float(input("digite a terceira nota: "))
media= (n1+n2+n3)/3
if media >=7:
    print(f"nota: {media:.1f}\n - aluno aprovado -")
else:
    print(f"nota: {media:.1f}\n - aluno reprovado -")
