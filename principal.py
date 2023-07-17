import core
import cita
import os

ismenu=True
while ismenu==True:
    if __name__ == '__main__':
        
        os.system("clear")
        print("Centro médico CampusMd")
        print("Menu:")
        print("1. Agregar cita") 
        print("2. Buscar cita")
        print("3. Modificar cita")
        print("4. Cancelar cita")
        print("5. Salir")

        
        opcion=input("Digite la opcion que desea seleccionar: ")
        os.system("clear")
        
        if opcion == "1":
            cita.LoadInfo()
            cita.AgregarCita()
        elif opcion == "2":
            cita.LoadInfo()
            cita.BuscarCita()
        elif opcion == "3":
            cita.LoadInfo()
            cita.ModificarCita()
        elif opcion == "4":
            cita.LoadInfo()
            cita.CancelarCita()
        elif opcion == "5":
            print("Fin del programa, esperamos que regrese pronto.")
            ismenu=False
