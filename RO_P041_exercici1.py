# RO_P041_exercici1

n = int(input( "n = "))
pes_maxim = 0 

for i in range(n):
    pes = float(input(f"pes del paquet {i + 1 } en kg = "))
    if pes > pes_maxim :
        pes_maxim = pes 
    
print("pes_maxim =", pes_maxim , "kg")