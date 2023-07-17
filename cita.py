import core
import verif
import os

diccCitas={"data":[]}


def LoadInfo():
    global diccCitas
    if (core.CheckFile("citas.json")):
        diccCitas = core.LoadInfo("citas.json")
    else:
        core.CrearInfo("citas.json",diccCitas)
def AgregarCita():
    
    verificfech=verif.VerificarFecha()
    if verificfech[1]==True:
        verifichora=verif.VerificarHora()
    
    if verificfech[1]==True and verifichora[1]==True:
        fechacita=verificfech[0]
        horacita=verifichora[0]
    
        nom=(input("Ingrese el nombre del paciente: ")).upper()
        motivo=input("Ingrese el motivo de la consulta: ").capitalize()

        paciente={
            "nombre":nom,
            "fecha":fechacita,
            "hora":horacita,
            "motivo":motivo,
        }
        
        diccCitas["data"].append(paciente)
        core.CrearInfo("citas.json",paciente)
def BuscarCita():
    Bander1=False
    os.system("clear")
    print("Criterios de busqueda:\n")
    print("1. Nombre del paciente")
    print("2. Fecha de la cita")
    criterio=input("\nSeleccione el criterio de busqueda que desea usar: ")
    os.system("clear")
    if (criterio=="1"):
        listcitaspacientes=[]
        print("Pacientes con citas agendadas:\n")
        for i in diccCitas["data"]:
            if (i["nombre"] in listcitaspacientes):
                pass
            else:
                listcitaspacientes.append(i["nombre"])
        for j in listcitaspacientes:
            print(j)
        selecpac=(input("\nIngrese el nombre del paciente que desea consultar: ")).upper()    
        
        print(str(selecpac))
        os.system("clear")
        print(f"Citas del paciente {selecpac.capitalize()}:\n")
        for i in diccCitas["data"]:
            if i["nombre"] == selecpac:
                print(f"Fecha: {i['fecha']}")
                print(f"Hora: {i['hora']}")
                print(f"Motivo: {i['motivo']}\n")
                Bander1=True
        if Bander1==False:
            print("No hay citas agendadas para este paciente\n")
        redirigir=input("Preione enter para continuar")   
        
    elif (criterio=="2"):
        
        verificfech=verif.VerificarFecha()
                
        if verificfech[1]==True:
            fechacita=verificfech[0]
            
            os.system("clear")
            print(f"Citas agendadas para el {fechacita}:\n")
            for i in diccCitas["data"]:
                if i["fecha"] == fechacita:
                    print(f"Paciente: {i['nombre']}")
                    print(f"Hora: {i['hora']}")
                    print(f"Motivo: {i['motivo']}\n")
                    Bander1 = True
            
            if Bander1==False:
                print("No hay citas agendadas para esta fecha\n")
            
            redirigir=input("Presione enter para continuar")
    
    else:
        print("Opción no valida")
        redirigir=input("Presione enter para continuar")
def ModificarCita():

    verificfech=verif.VerificarFecha()
    if verificfech[1]==True:
        verifichora=verif.VerificarHora()
    
    if verificfech[1]==True and verifichora[1]==True:
        fechacita=verificfech[0]
        horacita=verifichora[0]
        
        Bander1=False
        bandermod=True
        
        nom=(input("Ingrese el nombre del paciente: ")).upper()
        
        for i in diccCitas["data"]:
                if i["fecha"] == fechacita and i["hora"] == horacita and i["nombre"] == nom:
                    os.system("clear")
                    print("Cita actual:\n")
                    print(f"Paciente: {i['nombre']}")
                    print(f"Fecha: {i['fecha']}")
                    print(f"Hora: {i['hora']}")
                    print(f"Motivo: {i['motivo']}\n")
                    
                    print("Seleccione que desea modificar:"
                        "\n1. Nombre del paciente"
                        "\n2. Fecha de la cita"
                        "\n3. Hora de la cita"
                        "\n4. Motivo de la cita"
                        "\n5. Volver al menu"
                        "\n")
                        
                    seleccion=input("Seleccione la opcion que desea modificar:")
                    if seleccion != "5":     
                        print("\nModificaciones a la cita actual:\n")
                        newpaciente=i["nombre"]
                        newfechacita=i["fecha"]
                        newhoracita=i["hora"]
                        newmotivo=i["motivo"]
                    
                    if seleccion=="1":
                        newpaciente=input("Ingrese la correcion del nombre del paciente o presione enter para conservar el actual: ").upper() or i["nombre"]
                    elif seleccion=="2":
                        print("Ingrese la nueva fecha de la cita en formato (AAAA/MM/DD)")
                        año=input("Ingrese el año AAAA: ")
                        mes=input("Ingrese el mes MM: ")
                        dia=input("Ingrese el dia DD: ")
                        newfechacita=año+"/"+mes+"/"+dia
                    elif seleccion=="3":
                        print("Ingrese la hora de la cita en formato 24H (HH:MM)")
                        hora=input("Ingrese la hora HH: ")
                        minutos=input("Ingrese los minutos MM: ")
                        newhoracita=hora+":"+minutos
                    elif seleccion=="4":
                        newmotivo=input("Ingrese la correccion del motivo de la cita o presione enter para conservar el actual: ").capitalize() or i["motivo"]
                    elif seleccion=="5":
                        bandermod=False
                    
                    if bandermod==True:
                        i["nombre"]=newpaciente
                        i["fecha"]=newfechacita
                        i["hora"]=newhoracita
                        i["motivo"]=newmotivo
                        core.EditInfo("citas.json",diccCitas)   
                        
                    Bander1 = True
        
        if Bander1==False:
            print("\nNo hay citas agendadas para este paciente en esta fecha y hora\n")
        
        redirigir=input("Presione enter para continuar")
def CancelarCita():
    verificfech=verif.VerificarFecha()
    if verificfech[1]==True:
        verifichora=verif.VerificarHora()
    
    if verificfech[1]==True and verifichora[1]==True:
        fechacita=verificfech[0]
        horacita=verifichora[0]
        
        Bander1=False
        
        nom=(input("Ingrese el nombre del paciente: ")).upper()
        
        for pos,i in enumerate(diccCitas["data"]):
                if i["fecha"] == fechacita and i["hora"] == horacita and i["nombre"] == nom:
                    os.system("clear")
                    print("\nCita cancelada:\n")
                    print(f"Paciente: {i['nombre']}")
                    print(f"Fecha: {i['fecha']}")
                    print(f"Hora: {i['hora']}")
                    print(f"Motivo: {i['motivo']}\n")
                    
                    diccCitas["data"].pop(pos)
                    core.EditInfo("citas.json",diccCitas)   
                    redirigir=input("Presione enter para continuar")
                        
                    Bander1 = True
        if Bander1==False:
            print("\nNo hay citas agendadas para este paciente en esta fecha y hora\n")
            redirigir=input("Presione enter para continuar")
        
