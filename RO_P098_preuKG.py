#RO_P098_kilos.py

k = float(input("La quanitat de producte en kg ="))

if k  < 3:
    preu = k * 2.4
elif k >= 3 and k < 6:
    preu = k * 2.3
elif k >= 6 and k < 10 :
    preu = 2.1 * k
elif k >= 10 :
    preu = 1.85 * k

print(" EL preu total és",preu,"€")