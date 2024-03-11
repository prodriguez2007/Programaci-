# RO_P0147_granotas2.py
from random import*
granota1 = 0
granota2 = 0
granota3 = 0
opcions = [0, 0.5, 1, -0.5]
meta = 19.5

while granota1 <= meta and granota2 <= meta and granota3 <= meta:
    granota1 = choice(opcions) + granota1
    granota2 = choice(opcions) + granota2
    granota3 = choice(opcions) + granota3

print("Granota 1 =",granota1)
print("Granota 2 =",granota2)
print("Granota 3 =",granota3)

if granota1 >= 20:
    print("La granota 1 a guanyat la cursa")
elif granota2 >= 20:
    print("La granota 2 a guanyat la cursa")
elif granota3 >= 20:
    print("La granota 3 a guanyat la cursa")