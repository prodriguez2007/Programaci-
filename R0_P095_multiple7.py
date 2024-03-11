# R0_P095_multiple7

nombre = float(input("nombre ="))

if nombre % 1 == 0 :
    print("Aquest nombre és sencer")
    if nombre % 7 == 0:
        print(" Aquest nombre és múltiple de 7")
    else :
        print("Aquest nombre no és múltiple de 7")
else :
    print("No és sencer")
    