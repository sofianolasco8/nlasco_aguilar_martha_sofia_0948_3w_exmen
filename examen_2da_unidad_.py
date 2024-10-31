print(" ")
print("nolasco_aguilar_martha_sofia_0948_3W")
print(" ")
asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]#se abre la lista 
asignaturas[0] = int(input("ingresa tu calificacion:")) #indica al usuario ingresar su calificacion
asignaturas[1] = int(input("ingresa tu calificacion:"))#indica al usuario ingresar su calificacion
asignaturas[2] = int(input("ingresa tu calificacion:"))#indica al usuario ingresar su calificacion
asignaturas[3] = int(input("ingresa tu calificacion:"))#indica al usuario ingresar su calificacion
asignaturas[4] = int(input("ingresa tu calificacion:"))#indica al usuario ingresar su calificacion
if asignaturas[0] < 6:#indica que si la materia fue reprobada debe mostrar un mensaje 
    print("matematicas fue la materia que debe repetir")
else:
    asignaturas.remove(asignaturas[0])#indica que si la materia fue aprobada debe eliminarse de la lista 

if asignaturas[1] < 6:#indica que si la materia fue reprobada debe mostrar un mensaje 
    print("fisica fue la materia que debe repetir ")
else:
    asignaturas.remove(asignaturas[1])#indica que si la materia fue aprobada debe eliminarse de la lista 
if asignaturas[2] < 6:#indica que si la materia fue reprobada debe mostrar un mensaje 
    print("Química fue la materia que debe repetir")
else:
    asignaturas.remove(asignaturas[2])#indica que si la materia fue aprobada debe eliminarse de la lista 
if asignaturas[3] < 6 : #indica que si la materia fue aprobada debe eliminarse de la lista
    print("historia fue la materia que debe de repetir")
else:
    asignaturas.remove(asignaturas[3]) #indica que si la materia fue aprobada debe eliminarse de la lista 

if asignaturas[4] < 6:#indica que si la materia fue reprobada debe mostrar un mensaje 
    print("lengua fue la materia que debe repetir ")
else:
    asignaturas.remove(asignaturas[4])#indica que si la materia fue aprobada debe eliminarse de la lista 



