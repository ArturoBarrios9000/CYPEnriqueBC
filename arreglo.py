# arreglos
# lectura
# escritura / Asignacion
# Acutalizacion: insercion, eliminacion , modificacion
# ordenamiento
# busqueda

# Escitura
frutas = ["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]

# Lectura, el selector [indice]
print(frutas[2])
# Lectura con for
#for opcion 1
for indice in range (0,7,1):
    print(frutas[indice])
print("---------------------------------------------------------")

# for opcion 2 -- por un iterador for each
for fr in frutas:
    print(fr)
print("---------------------------------------------------------")
# asignacion
frutas [2]="Melon"
print(frutas)
print("---------------------------------------------------------")
# insercion al final
frutas.append ("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)
print(len(frutas))
# eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda
print(f"La manzana esta en la posicion {frutas.index('Manzana')}")
print(f"El limon esta {frutas.count('Limon')}veces en la lista")

#concatenar
print(frutas)
otras_frutas=["Rambutan","Nispero","Liche","Pitaya"]
frutas.extend(otras_frutas)
print(frutas)

# copiar
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia=frutas.copy()
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
