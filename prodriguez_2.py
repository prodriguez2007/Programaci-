# exercici 2 examen.py


x = int(input("Any qualsevol = "))

a = x % 19
b = a % 14
c = b % 7
d = (19 * a + 24) % 30
e = (( 2* b) + (4 * c) + (6 * d) + 5) % 7
f = 22 + d + e


if f > 31 :
    f = f % 30
    print(f"El diumenge de pascua és el dia {f } d'abril")
else:
    print(f"El diumenge de pascua és el dia {f} de març")
    
    

