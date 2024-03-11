#exercici 1 examen

personas = int(input("Personas = "))
n = 1

while n <= personas:
    n = n + 1
    renda = float(input(f"Renda actual de la persona {n-1}:"))
    if renda < 10000 :
        renda = renda * 0.95
        print(renda)
    elif renda >= 10000 and renda <= 20000:
        renda = renda * 0.85
        print(renda)
    elif renda > 20000 and renda <= 35000:
        renda = renda * 0.80
        print(renda)
    elif renda > 35000 and renda <= 60000:
        renda = renda * 0.70
        print(renda)
    else :
        renda = renda * 0.55
        print(renda)
    
