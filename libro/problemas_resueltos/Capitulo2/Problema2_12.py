SUE=float(input("Ingrese sueldo del trabajador:"))
CAT=int(input("Ingrese categoria del trabajador:"))
HE=int(input("Ingrese las horas extas del trabajador:"))
if CAT ==1:
    PHE=30
elif CAT ==2:
    PHE=38
elif CAT ==3:
    PHE=50
elif CAT ==4:
    PHE=70
else:
    PHE=0
if HE>30:
    NSUE=SUE+30*PHE
else:
    NSUE=SUE+HE*PHE
print(f"El nuevo suelo del trabajador es {NSUE}")
print("FIN")
