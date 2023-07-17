import os
def VerificarFecha(*args):
    Banderfech=True
    print("Ingrese la fecha de la cita en formato (AAAA/MM/DD)")
    año=input("Ingrese el año AAAA: ")
    mes=input("Ingrese el mes MM: ")
    dia=input("Ingrese el dia DD: ")
    if len(año)!=4 or int(año)<2023:
        print("Fecha no valida, ingrese un año valido")
        Banderfech=False
    if len(mes)!=2 or int(mes)<1 or int(mes)>12:
        print("Fecha no valida, ingrese un mes valido")
        Banderfech=False
    if len(dia)!=2 or int(dia)<1 or int(dia)>31:
        print("Fecha no valida, ingrese un dia valido")
        Banderfech=False
    redirigir=input("Presione enter para continuar")
    fechacita=año+"/"+mes+"/"+dia
    return fechacita,Banderfech
def VerificarHora(*args):
    Banderhora=True
    print("Ingrese la hora de la cita en formato 24H (HH:MM)")
    hora=input("Ingrese la hora HH: ")
    minutos=input("Ingrese los minutos MM: ")
    if len(hora)!=2 or int(hora)<0 or int(hora)>23:
        print("Hora no valida, ingrese una hora valida")
        Banderhora=False
    if len(minutos)!=2 or int(minutos)<0 or int(minutos)>59:
        print("Hora no valida, ingrese minuto validos")
        Banderhora=False
    redirigir=input("Presione enter para continuar")
    horacita=hora+":"+minutos
    return horacita,Banderhora