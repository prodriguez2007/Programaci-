# R0_P096_determinartriangle

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == b and b == c:
    print("El triangle és equilàter")
elif a == b and b != c :
    print(" El triangle és iscoscels")
elif a == c and b != c :
    print(" El triangle és iscoscels")
elif b == c and b != a :
    print(" El triangle és iscoscels")
else:
    print("El triangles és escalè")
    
