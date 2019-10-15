PREB=float(input("Ingrese el precio basico del producto basico:"))
if PREB>500:
    IMP=20*0.3+(PREB-40)*0.5
    PRETOT=PREB+IMP
    print(f"El precio del producto es {PREB} y con el impuesto es {PRETOT}")
elif PREB>40:
    IMP=20*0.3+(PREB-40)*0.40
    PRETOT=PREB+IMP
    print(f"El precio del producto es {PREB} y con el impuesto es {PRETOT}")
elif PREB>20:
    IMP=(PREB-20)*0.3
    PRETOT=PREB+IMP
    print(f"El precio del producto es {PREB} y con el impuesto es {PRETOT}")
else:
    print(f"El precio del producto es {PREB} y con el impuesto es {PREB}")
print("FIN")
