#RO_PO32_kw.py

kw = float(input("kw ="))
preu_kwh = float(input("preu_kw ="))

if kw > 700 :
    total = kw * preu_kwh * 1.05
else :
    total = kw * preu_kwh
    
print("total =", total)

