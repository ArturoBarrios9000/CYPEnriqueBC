NUM=float(input("Ingrese el monto de la compra:"))
if NUM<500:
    print(f"El precio a pagar es {NUM}")
elif NUM<=1000:
    PA=NUM-(NUM*0.05)
    print(f"El precio a pagar es {PA}")
elif NUM<=7000:
    PA=NUM-(NUM*0.11)
    print(f"El precio a pagar es {PA}")
elif NUM<=15000:
    PA=NUM-(NUM*0.18)
    print(f"El precio a pagar es {PA}")
else:
    PA=NUM-(NUM*0.25)
    print(f"El precio a pagar es {PA}")
print("FIN")
