#RO_P031_notacióalgorítmica_2.py

c = float(input("c ="))
t = float(input("t ="))
d = float(input("d ="))
p = 0

if c <= 40 :
    p = c * t - d
else :
    p = 40 * t + (1.5 * t * (c - 40)) -d
    
print("p =", p)
    
