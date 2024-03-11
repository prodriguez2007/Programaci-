#  RO_P083_nombrealreves.py

a = int(input("Ingresa nombre de tres xifres ="))

b = a // 10
b = b % 10
c = a // 100
d = a % 10
total = d * 100 + b * 10 + c
print("El nombre", a , "al revés es", total)