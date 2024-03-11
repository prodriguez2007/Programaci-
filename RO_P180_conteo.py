#RO_P180_exercici1

def conteo(n):
    d = 0
    divisors = 0
    while n != d:
        d += 1
        if n % d == 0:
            divisors = divisors + 1
    return divisors 
d = 0 
for i in range(1,101):
    if conteo(i) > d :
        d = conteo(i)
        c = i
print(" El número que té més divisors entre 1 i 100 és el", c)
        
            