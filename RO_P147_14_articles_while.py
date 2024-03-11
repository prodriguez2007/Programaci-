#RO_P147_14_articlespy

diners = float(input("Diners ="))
articles = [454, 785, 1000, 2347]
n = len(articles)
a = 0
c = 0  
while n != c :
    c += 1 
    if n < diners:
        a += 1
        d = diners / articles[a - 1 ] // 1
        print(f"Podem comprar {d} unitats de l'article {a}")
        
print(f"En total pot comprar {a} articles")
    
    