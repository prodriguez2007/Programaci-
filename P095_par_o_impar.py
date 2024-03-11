# R0_P095_paroimpar
from math import*

nombre = int(input("Ingresa número de 2 xifres:"))

[unitat, desena] = divmod(nombre,10)
suma = unitat + desena

if suma % 2 == 1:
    print(f"El nombre {suma} és imparell")
else:
    print(f"El nombre {suma} és parell")
    