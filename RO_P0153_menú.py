# Menús
salida = False
s = 0
n = 0
a = 0
u = 0 
while not salida:
    print("1 Per obtenir la suma de termes")
    print("2 Per obtenir la quantitat de termes")
    print("3 Per obtenir el primer terme")
    print("4 per obtenir l'últim terme")
    print("5 per sortir")
    a = int(input("Escull:"))
    if a == 1 :
        n = int(input("Quantitat de termes ="))
        a = int(input("Primer terme ="))
        u = int(input("Últim terme ="))
        s = (n / 2) * ( a + u)
        print("Suma =", s)
    elif a == 2 :
        s = int(input("Suma ="))
        a = int(input("Primer terme ="))
        u = int(input("Últim terme ="))
        n = 2 * s / (a + u)
        print("Quantitat de termes =",n)
    elif a == 3:
        s = int(input("Suma ="))
        n = int(input("Quantitat de termes ="))
        u = int(input("Últim terme ="))
        a = (s - (n / 2) * u) /( n /2) 
        print("Primer terme =",a)
    elif a == 4 :
        s = int(input("Suma ="))
        n = int(input("Quantitat de termes ="))
        a = int(input("Primer terme ="))
        u = (s - (n /2) * a) / (n / 2)
        print("Últim terme =",u)
    elif a == 5:
        print("Adiós muy buenas")
        salida = True
        
        
        