A=int(input("Ingrese valor entero positivo para A:"))
B=int(input("Ingrese valor entero positivo para B:"))
C=int(input("Ingrese valor entero positivo para C:"))
if A>B:
    if A>C:
        print(f"El valor de A {A} es el mayor")
    elif A==C:
        print(f"A y C son mayores y tienen un valor de {A}")
    else:
        print(f"El valor de C {C} es el mayor")
elif A==B:
    if A>C:
        print(f"A y B son mayores y tienen un valor de {B}")
    elif A==C:
        print(f"A, B y C son iguales y tienen un valor de {A}")
    else:
        print(f"El valor de C {C} es el mayor")
elif B>C:
    print(f"El valor de B {B} es el mayor")
elif B==C:
    print(f"B y C son mayores y tienen un valor de {B}")
else:
    print(f"El valor de C {C} es el mayor")
print("Fin")
