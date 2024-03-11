# RO_P071_creixement_poblacional
from math import *

k = (50 - (2*exp(0.1*10))) / 10
print(k)
t = float(input(" t = "))
f = k * t + 2*exp(0.1 * t)
print(" f = ",f )
