# exemple5_P046

a = int(input(" a = "))
b = int(input(" b = " ))
c = int(input(" c = "))

if a > b :
    while c <= a :
        c = c+ 3
else :
    while a < b + c:
        a = a + 5
    print(" a = ", a )

print( "c = ", c )