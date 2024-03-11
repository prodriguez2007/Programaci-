# RO_P041_exercici2

n = int(input( "n ="))
vots_a_favor = 0
vots_en_contra = 0
vots_nuls = 0 

for i in range(1, n + 1 ):
    vots = int(input(f"vot {i} ="))
    if vots == 1 :
        vots_a_favor = vots + vots_a_favor
    elif vots == 0 :
        vots = 1 
        vots_en_contra = vots + vots_en_contra
    else :
       vots  = 1
       vots_nuls = vots + vots_nuls
         
        
print("vots a favor = ",vots_a_favor)
print("vots en contra = ", vots_en_contra)
print("vots nuls =", vots_nuls)
        