# RO_P0146_mcd.py

a = int(input("a = "))
b = int(input("b = "))
mcd = 0
n =  1
d = 0
c = 0
while n != b:
    n = n + 1
    d = a / n
    c = b / n
    if d %1 == 0 and c % 1 == 0:
        mcd = n
    
if mcd == 0 :
    print("No tenen divisors comuns")

print(mcd)
    
    
    
    
  