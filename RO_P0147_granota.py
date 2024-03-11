# RO_P0147_granotas
from random import*

llista = [-1,1]
meta1 = 20
meta2 = 0 
començament = meta1 / 2 
suma = començament
salts = 0

while suma != meta1 and suma != meta2:
    d = choice(llista)
    suma = d + suma
    salts = salts + 1
    
print(f"La granota haurà fet {salts} salts")

    
    

