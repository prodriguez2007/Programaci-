# RO_P095_diagonals

from math import*

altura = float(input("altura =")) 
longitud = float(input("longitud ="))
amplada = float(input("amplada ="))

diagonal_1 = sqrt( (altura * altura) + (longitud * longitud))
diagonal_2 = sqrt( (amplada * amplada) + (longitud * longitud))
diagonal_3 = sqrt( (altura * altura) + (amplada * amplada))

if diagonal_1 > diagonal_2:
    if diagonal_1 > diagonal_3:
         diagonal_gran = diagonal_1
elif diagonal_2 > diagonal_1 :
    if diagonal_2 > diagonal_3:
        diagonal_gran = diagonal_2   
else :
    diagonal_gran = diagonal_3
    
print("diagonal_gran =", diagonal_gran)