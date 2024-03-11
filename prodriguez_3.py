# Exercici 3examen.py
#apartat a)

pes =  0.75 * 1.25 # * h en metres cúbics
# el volum multiplicat per la densitat 1 kg/dm3 dona una massa de 937,5 kg * h
a = pes * 4.187 * 20  # el pes està en tones per a que el resultat sigui en MJ
print(a,"MJ * h")

# apartat b)
# totes les unitats de la taula estan en m
energia1 =  78.506 * 0.2 
energia2 = 78.506 * 0.25
energia3 = 78.506 * 0.3
energia4 = 78.506 * 0.35
energia5 = 78.506 * 0.4

print("Energia en MJ:")
print(energia1)
print(energia2)
print(energia3)
print(energia4)
print(energia5)

# apartat c
eu = 78.506 * 0.4 #energia útil donada l'alçada
eur = eu / 0.8 # energia d'entrada
kg = eur / 45.79 # quantitat de kg
# preu per kg
preu = 12.94 / 12.5
preu_total = preu * kg

print("El preu total és", preu_total,"€")


