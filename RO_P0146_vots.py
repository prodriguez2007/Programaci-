# RO_P0146_vots

vots = int(input(" Vots = "))
candidat_1 = 0
candidat_2 = 0
candidat_3 = 0
vot_en_blanc = 0 
resultat = 0
i = 1
nul = 0 
while i >= 1 and i <= vots:
    resultat = int(input(f"Vot {i} ="))
    if resultat == 0 :
        vot_en_blanc = vot_en_blanc + 1
    elif resultat == 1 :
        candidat_1 = candidat_1 + 1
    elif resultat == 2 :
        candidat_2 = candidat_2 + 1
    elif resultat == 3 :
        candidat_3 = candidat_3 + 1
    else:
        nul = nul + 1
    i = i  + 1 
print(f"Hi han hagut {vot_en_blanc} vots en blanc")
print(f"Hi han hagut {nul} vots nuls")
print(f"El Candidat 1 ha rebut {candidat_1} vots")
print(f"El Candidat 2 ha rebut {candidat_2} vots")
print(f"El Candidat 3 ha rebut {candidat_3} vots")

        