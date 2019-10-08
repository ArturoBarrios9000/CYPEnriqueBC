CAT=int(input("Introdusca la categoria del trabajador (1-4):"))
SUE=float(input("Introdusca el sueldo del trabajador:"))
NSUE=0
if CAT ==1:
    NSUE=SUE*1.15
elif CAT==2:
    NSUE=SUE*1.10
elif CAT==3:
    NSUE=SUE*1.08
elif CAT==4:
    NSUE=SUE*1.07
print(f"El sueldo con categoria {CAT} con el aumento es: {NSUE}")
