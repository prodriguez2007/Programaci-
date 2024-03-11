# RO_P032_blocrectangular.py
import math

altura = float(input("altura =")) #entrada dades reals
longitud = float(input("longitud ="))
amplada = float(input("amplada ="))

diagonal_1 = math.sqrt( (altura * altura) + (longitud * longitud))
diagonal_2 = math.sqrt( (amplada * amplada) + (longitud * longitud))
diagonal_3 = math.sqrt( (altura * altura) + (amplada * amplada))

if diagonal_1 > diagonal_2:
    if diagonal_1 > diagonal_3:
         diagonal_gran = diagonal_1
elif diagonal_2 > diagonal_1 :
    if diagonal_2 > diagonal_3:
        diagonal_gran = diagonal_2   
else :
    diagonal_gran = diagonal_3
    
print("diagonal_gran =", diagonal_gran)