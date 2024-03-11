# RO_P096_roba.py

articles = int(input("articles ="))
preu_unitari = float(input("preu ="))
preu = articles * preu_unitari
if articles >= 5 :
    if articles < 10:
        preu = preu * 0.95
if articles >= 10:
    preu = preu * 0.92

print("El preu final és",preu, "€")
    

    
    