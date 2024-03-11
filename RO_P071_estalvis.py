#RO_P071_estalvis
from math import*
p = float(input("p = "))
x = float(input("x= "))
n = int(input("n = "))

a = p *((pow((1 + x),n)-1)/ x) 
print("a = ",a)

#apartat b
k = ((pow((1 + x),n)-1)/ x)
x = float(input("x = "))
n = int(input("n= "))
a = float(input("a = "))
p = a / k
print("p = ")
