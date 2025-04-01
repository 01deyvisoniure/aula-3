time1=input("digite o nome do time1: ")
gol_time1= int(input("quantidade gols, time1: "))
time2=input("digite o nome do time2: ")
gol_time2= int(input("quantidade gols, time2: "))
if gol_time1 == gol_time2:
    print("empate")
else:
    if gol_time1 > gol_time2:
        print(f"{time1} ganhou de {gol_time1} a {gol_time2} do {time2}")
    else:
        print(f"{time2} ganhou de {gol_time2} a {gol_time1} do {time1}")
