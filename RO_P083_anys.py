#RO_P083_dies_anys.py
from math import *

dies = int(input("dies = "))
anys = [x,y]=divmod(dies,365)
messos = [y,z] = divmod(y , 30)
dies_3 = z
print(f"{dies} dies equivalen a {x} anys, {y} messos i {dies_3} dies" )
