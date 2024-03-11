#RO_P096_numero3xifres.py

numero = int(input("ingresa un número de tres xifres:"))

[numero1,numero2] = divmod(numero, 100)
[numero2,numero3] = divmod(numero2, 10)
multiplicacio = numero1 * numero2
resultat = multiplicacio % 10

if resultat == numero3:
    print("codi vàlid")
else :
    print("Codi invàlid")


