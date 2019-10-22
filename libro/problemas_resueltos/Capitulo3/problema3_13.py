ARSU=0
ARNO=0
MERSU=50000
MES=0
ARCE=0
for i in range (1,13,1):
    print(f"Mes {i}:")
    RNO=int(input("Ingrese el promedio de lluvia en el mes Zona norte:"))
    RCE=int(input("Ingrese el promedio de lluvia en el mes Zona centro:"))
    RSU=int(input("Ingrese el promedio de lluvia en el mes Zona sur:"))

    ARNO=ARNO + RNO
    ARCE=ARCE+RCE
    ARSU=ARSU+RSU

    if RSU < MERSU:
        MERSU=RSU
        MES=i
PRORCE=ARCE/12
print(f"Promedio region centro: {PRORCE}")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MERSU}")
if ARNO>ARCE:
    if ARNO>ARSU:
        print("La region con mayor lluvia es la region Norte")
    else:
        print("La region con mayor lluvia es la region Sur")
elif ARCE>ARSU:
    print("La region con mayor lluvia es la region Centro")
else:
    print("La region con mayor lluvia es la region Sur")
print("FIN")
