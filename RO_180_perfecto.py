#RO_P180_perfecto

def perfecto(n):
    d = 0
    divisors = 0
    suma = 0 
    while n != d:
        d += 1
        if n == d:
            break
        elif n % d == 0:
            divisors = divisors + 1
            suma = d + suma 
    if suma == n :
        return "És un número perfecte"
    else:
        return"No és un número perfecte"
    