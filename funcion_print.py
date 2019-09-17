# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format()
4.- es con una variante de format()
"""
# Con comas, concatenar agregando
# un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad, estatura, nombre)
# con '+' hace lo mismo pero no
# realiza el casting automatico
# no agrega espacio
print(str(edad) + str(estatura) + nombre)
# Con la funcion format()
print("Nombre: {} Edad: {} ".format(nombre, edad, estatura))
# Con una variante de format() simplificada
print(f"Nombre: \"{nombre}\" \nEdad: {edad}")
# print y el argumento end
print("Solo hay 10 tipos de personas las que saben binario y las que no",end=" ")
print("Otra linea")
