print("*******************************************************************************************")
# crea un nuevo archivo llamado my_notes.txt
my_notes=open("notes.txt","w")
# Escritura de Archivo de Texto con el metodo write()
 # Escribir notas personales en el archivo
my_notes.write("esta es mi agenda de la semana:\n")
my_notes.write("1. Lunes debo viajar a Cuenca.\n")
my_notes.write("2. Martes tengo una cita medica a las 8 a.m.\n")
my_notes.write("2. Miercoles tengo que entregar dederes de la universidad\n")
my_notes.write("2. Jueves debo enviar un paquete al Puyo\n")
my_notes.write("3. Viernes debo ir al gymnacio .\n")
#Metodo writeline(): escribe una lista de lineas
lineas =["Agrega una lista de notas personales adicionales-\n","4. preparar un informe","5. presenta tareas"]
my_notes.writelines(lineas)

#Abre el archivo my_notes.tx
print("Blog 1")
print("**********************************")
my_notes=open("notes.txt","r")
# Lectura de Archivo de Texto linea por linea por el metodo read()
print(my_notes.read())
my_notes.close()
# Metodo 2
my_notes=open("notes.txt","r")
print("Metodo 2")
print("**********************************")
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()
