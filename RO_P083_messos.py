#RO_P083_dies_messos
from math import*

dies = int(input("dies = "))

mesos = [x,y] = divmod(dies, 30)
setmanes = [y,z] = divmod(y, 7)

print(f"{dies} equivalen a { x} messos, {y} setmanes i {z} dies ")