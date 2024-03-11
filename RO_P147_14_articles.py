#RO_P147_14_articlespy

diners = float(input("Diners ="))
articles = [454, 785, 1000, 2347]
a = 0 
for n in articles:
    if n < diners:
        a += 1
        d = diners + 1  /n // 1
        print(f"Podem comprar {d} unitats de l'article {a}")

print(f"En total pot comprar {a} articles")
    
    
