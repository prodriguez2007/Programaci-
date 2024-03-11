# RO_FOrmes

def quadrat(a):
    area = a**2
    p = 4 * a
    print("Area =",area)
    print("Perímetre =",p)
def triangle(a, b , c, h):
    area = (b * h )/ 2
    p = a + b + c
    print(area)
    print(p)
def rectangle(a, b):
    area = a * b
    p = 2 *(b+a)
    print(area)
    print(p)
def paralelogram(a,b,h):
    area = b * h
    p = 2 * (a + b)
    print(area)
    print(p)
def rombo(D,d,a):
    area = (D * d) / 2
    p = 4 * a
    print(area)
    print(p)
def cometa(D, d ,a ,b):
    area = (D*d) / 2
    p = 2 * (a + b )
    print(area)
    print(p)
def trapezi(B, b, h, a, c):
    area = ((B*b)*h)/2
    p = B + b + a + c
    print(area)
    print(p)
def cercle(r):
    area = 3.1416 * (r**2)
    p = 2 * 3.1416 * r
    print(area)
    print(p)
def poligon_regular(P,a, n, b):
    area = (P*a)/2
    p = n * b
    print(area)
    print(p)
def corona_circular(R,r):
    area  = 3.1416 * (R**2 - r**2 )
    print(area)
def sector_circular(R,n):
    area = (3.1416 * R**2 * n) / 360
    print(area)
    
salida = False
while not salida :
    print("")
    print("1. rectangle")
    print("2. tirangle")
    print("3. rectangle")
    print("4. paralelogram")
    print("5. rombe")
    print("6 estel")
    print("7 trapezi")
    print("8. cercle")
    print("9. polígon regular")
    print("10. corona regular")
    print("11. sector regular")
    print("12. Sortida")
    x = int(input("Escull:"))
    if x == 1 :
        a = float(input("Costat a ="))
        quadrat(a)
    elif x == 2:
        a = float(input("Costat a ="))
        b = float(input("Costat b ="))
        c = float(input("Costat c = "))
        h = float(input("Altura ="))
        triangle(a,b,c,h)
    elif x == 12:
        salida = True
     
    
