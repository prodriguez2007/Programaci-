# número primer 

enter = int(input("enter = "))
numero = 2

if enter == 1:
    print("El número és primer")

while ((enter / numero) % 1) != 0 :
    numero = 1 + numero

if numero == enter:
    print("El número és primer")
else :
    print("El número no és primer")

    
    

