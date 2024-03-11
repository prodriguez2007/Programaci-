# R0_P096_kw

kw = float(input("Quantitat de Kw consumida:"))
preu_kwh = float(input("Preu del Kw/h:"))

total = kw * preu_kwh

if total >= 700 :
    total = total * 1.05
    
print(f"El total a pagar són {total}€")