# RO_P083_suma_nombres

a = int(input("Primer nombre de tres xifres  = "))
b = int(input("Segon nombre de tres xifres = "))

a_2 = a // 10
nombre_mig_a = a_2 % 10
b_2 = b // 10
nombre_mig_b = b_2 % 10
suma = nombre_mig_b + nombre_mig_a

print("La suma dels dos nombres es =", suma)