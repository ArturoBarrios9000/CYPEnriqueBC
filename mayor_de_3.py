A=int(input("Ingrese el primer numero:"))
B=int(input("Ingrese el segundo numero:"))
C=int(input("Ingrese el tercer numero:"))

if A != B and A != C and B != C:
if A>B and A>C:
    print(f"{A} Es mayor")
else:
    if B>A and B>C:
        print(f"{B} Es mayor")
    else:
        print(f"{C} Es mayor")
