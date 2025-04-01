time1=input("digite o nome do time1: ")
time2=input("digite o nome do time2: ")
gol_time1= int(input("qauntidade gols, time1: "))
gol_time2= int(input("qauntidade gols, time2: "))
if gol_time1 > gol_time2:
    print(f"{time1} ganhou de {gol_time1} a {gol_time2}")
else:
    if gol_time2 > gol_time1:
        print(f"{time2} ganhou de {gol_time2} a {gol_time1}")
    else:
        print(f"empate {gol_time2}x{gol_time1}")
