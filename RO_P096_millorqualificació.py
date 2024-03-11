# RO_P095_calificacions dos estudiants

q1 = float(input(" La primera qualificació de l'estudiant 1 és:"))
q2= float(input(" La segona qualificació de l'estudiant 1 és:"))
q3 = float(input(" La tercera qualificació de l'estudiant 1 és:"))

q4 = float(input(" La primera qualificació de l'estudiant 2 és:"))
q5 = float(input(" La segona qualificació de l'estudiant 2 és:"))
q6 = float(input(" La tercera qualificació de l'estudiant 2 és:"))

#estudiant 1
if q1 == q2 and q2 == q3:
    suma1 = q1 + q2
    
elif q1 == q2 and q1 > q3:
    suma1 = q1 + q2
    
elif q1 == q2 and q1 <q3:
    suma1 = q1 + q3
    
elif q2 == q3 and q2 > q1:
    suma1 = q2 + q3
elif q2 == q3 and q2 < q1:
    suma1 = q2 + q1
elif q1 == q3 and q3 > q2:
    suma1 = q1 + q3
elif q1 == q3 and q3 < q2:
    suma1 = q2 + q3
elif q1 > q2 and q2 > q3:
    suma1 = q1 + q2
elif q1 > q2 and q3 > q2:
    suma1 = q1 + q3
elif q2 > q1 and q3 > q1:
    suma1 = q2 + q3
elif q2 > q1 and q1 > q3:
    suma1 = q2 + q1
print(suma1)
#estudiant 2
if q4== q5 and q5 == q6:
    suma2 = q1 + q2
elif q4 == q5 and q4 > q6:
    suma2 = q4 + q5
elif q4 == q5 and q4 < q6:
    suma2= q4 + q6
elif q5 == q6 and q5 > q4:
    suma2 = q5 + q6
elif q5 == q6 and q5 < q4:
    suma2 = q5 + q4
elif q4 == q6 and q4 > q5:
    suma2 = q4 + q6
elif q4 == q6 and q4 < q5:
    suma2 = q5 + q4
elif q4 > q5 and q5 > q6:
    suma2 = q4 + q5
elif q4 > q5 and q6 > q5:
    suma2 = q4 + q6
elif q5 > q4 and q6 > q4:
    suma2 = q5 + q6
elif q5 > q4 and q4 > q6:
    suma2 = q5 + q4
print(suma2)
#comparacio 
if suma2 > suma1:
    print("L'estudiant 2 ha tingut una millor qualificació final")
elif suma2 == suma1:
    print("Els dos estudiants han tret la mateixa qualificació final")
else:
    print("L'estudiant 1 ha tingut una millor qualificació final")
