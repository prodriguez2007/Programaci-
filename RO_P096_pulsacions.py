# RO_P097_pulsacions

genere = int(input("Si és dona posa un 1 i si és home posa un 2:"))
edad = int(input("Edat:"))

if genere == 1:
    pulsacions = (220 - edad)/10
elif genere == 2 :
    pulsacions = (210 - edad)/10

print("Número de puslacions per cada 10 segons d'exercici", pulsacions)

    