"""ESCENARIO/PLANTEAMIENTO DEL PROBLEMA

El centro médico CampusMd desea crear un programa que permita gestionar citas médicas para
un consultorio. El programa deberá permitir agregar, buscar, modificar y cancelar citas médicas,
y guardar la información en archivos JSON.

TIPS DE SOLUCION

1. El programa debe tener un menú que permita al usuario seleccionar diferentes opciones:
agregar cita, buscar cita, modificar cita, cancelar cita y salir del programa.
2. Cada cita médica debe tener los siguientes datos: nombre del paciente, fecha de la cita,
hora de la cita y motivo de la consulta.
3. Al agregar una cita, el programa debe solicitar al usuario que ingrese los datos
correspondientes y luego guardar la cita en un archivo JSON.
4. Al buscar una cita, el programa debe solicitar al usuario un criterio de búsqueda (por
ejemplo, nombre del paciente o fecha de la cita) y mostrar todas las citas que coincidan
con ese criterio.
5. Al modificar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y solicitar los nuevos datos para actualizarla en el archivo JSON.
6. Al cancelar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y eliminarla del archivo JSON.
7. Al salir del programa, se deben guardar todos los cambios realizados en el archivo JSON
y mostrar un mensaje de despedida."""

print("Ingrese la fecha de la cita en formato (AAAA/MM/DD)")
año=input("Ingrese el año AAAA: ")
mes=input("Ingrese el mes MM: ")
dia=input("Ingrese el dia DD: ")
fechacita=año+"/"+mes+"/"+dia
print("Ingrese la hora de la cita en formato 24H (HH:MM)")
hora=input("Ingrese la hora HH: ")
minutos=input("Ingrese los minutos MM: ")
horacita=hora+":"+minutos
nom=(input("Ingrese el nombre del paciente: ")).capitalize()
motivo=input("Ingrese el motivo de la consulta: ").capitalize()

paciente={
    "nombre":nom,
    "fecha":fechacita,
    "hora":horacita,
    "motivo":motivo,
}
nombre del paciente, fecha de la cita,
hora de la cita y motivo de la consulta.