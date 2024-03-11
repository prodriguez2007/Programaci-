# RO_P097_IMC
from math import*

p = float(input("Pes en kg ="))
a = float(input("Altura en m ="))

imc = p / pow(a,2)
print("L'IMC és :",imc)

if imc < 20 :
    print("Desnutrit")
elif imc >= 20 and imc < 25 :
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepes")
elif imc >= 30 and imc < 35:
    print("Obesitat grau 1")
elif imc >= 35 and imc <= 40 :
    print("Obesitat grau 2")
elif imc > 40 :
    print("Obesitat grau 3")
