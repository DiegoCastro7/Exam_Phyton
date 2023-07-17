import json
import os

def CrearInfo(*args):
    if (CheckFile(args[0])==False):
        with open ('data/'+args[0], 'w') as write_file:
            json.dump(args[1],write_file,indent=4)
            write_file.close()
    
    else:
        with open ('data/'+args[0], 'r+') as file:
            file_data = json.load(file)
            file_data['data'].append(args[1])
            file.seek(0)
            json.dump(file_data,file,indent=4)
            file.close()

def EditInfo(*args):
    with open ('data/'+args[0], 'w') as write_file:
        json.dump(args[1],write_file,indent=4)
        write_file.close()

def LoadInfo(fileName):
    if CheckFile(fileName)==True:
        #revisar
        with open ('data/'+fileName, 'r') as read_file:
            dicc=json.load(read_file)
            return dicc
        
def CheckFile(fileName):
    try:
        with open ('data/'+fileName,'r') as f:
            return True
    except FileNotFoundError as e:
        print("Error revise el codigo")
        print("x_x")
        os.system("clear")
        return False
    except IOError as e:
        return False