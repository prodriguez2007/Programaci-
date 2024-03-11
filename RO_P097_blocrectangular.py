# RO_P097_area bloque cares.py

altura = float(input("altura ="))
longitud = float(input("longitud ="))
amplada = float(input("amplada ="))

cara1 = altura * longitud
cara2 = altura * amplada
cara3 = amplada * longitud
print(cara1, cara2, cara3)

if cara1 > cara2 and cara1 > cara3:
    print(cara1)
elif cara1 > cara2 and cara1 < cara3:
    print(cara3)
elif cara1 == cara2 and cara1 == cara3:
    print(cara1)
elif cara1 == cara2 and cara2 < cara3:
    print(cara3)
elif cara1 == cara2 and cara1 > cara3:
    print(cara1)
elif cara1 == cara3 and cara1 < cara2:
    print(cara2)
elif cara1 == cara3 and cara1 > cara2:
    print(cara1)
elif cara2 == cara3 and cara2 < cara1:
    print(cara1)
elif cara2 == cara3 and cara2 > cara1:
    print(cara3)
elif cara1 < cara2 and cara2 < cara3:
    print(cara3)
elif cara1 < cara2 and cara2 > cara3:
    print(cara2)
elif cara3 > cara2 and cara1 > cara3:
    print(cara1)