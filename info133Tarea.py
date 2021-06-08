from pymongo import MongoClient
import os
import time
#--------------------#
client = MongoClient("localhost")
#--------------------#
db = client["proyecto_Fusa"]
#--------------------#


def agregar_Archivos(archivos,fechaGrabacion, cuidad, duracion,formato, lista_ubicacion, lista_segmentos, rut):
    archivos.insert_one({
        "fecha de grabacion" : fechaGrabacion,
        "cuidad" : cuidad,
        "duracion" : duracion,
        "formato" : formato,
        "ubicacion" : {

            "Latitud" : lista_ubicacion[0],
            "Longitud" :  lista_ubicacion[1],        ### crea una lista con latitud[0] logitud[1] exterior[2]
            "Exterior_Interior" : lista_ubicacion[2]
        },
        "segmentos" : [
            {
                "ID" : lista_segmentos[0],
                "formato" : lista_segmentos[1],
                "duracion " : lista_segmentos[2],
                "inicio" : lista_segmentos[3],
                "fin" : lista_segmentos[4]
                


            }
        ],
        "rut_propietario" : rut             
    })

def agregar_Persona(personas,nombreP,apellidoP,rutP):
    personas.insert_one({
        "Nombre" : nombreP,
        "Apellido" :apellidoP,
        "Rut" : rutP

    })


def Agregar_Segmento_audio(segmento, listaSegmentos, nombre_fuentes,descripcion,ID_analizador ):

    segmento.insert_one({
        "ID" : listaSegmentos[0],
        "formato" : listaSegmentos[1], 
        "duracion" : listaSegmentos[2],
        "inicio " : listaSegmentos[3],
        "fin"  : listaSegmentos[4], 
        "tipo_De_Fuente" :[
            {
               "nombre" : nombre_fuentes,
               "descripcion" : descripcion,
               "id_analizador" :ID_analizador
            }
        ]
    })

def analizar_automaticamente(seg, ID_seg, nombre_fuente, porcentaje):
    seg.inset_one({
        "ID segmento" : ID_seg,
        "Nombre fuente " : nombre_fuente, 
        "porcentaje " : porcentaje

    })

def analizar_automaticamente(seg, ID_seg, nombre_fuente):
    seg.inset_one({
        "ID segmento" : ID_seg,
        "Nombre fuente " : nombre_fuente, 
    })


def eliminarData():
    client.drop_database("proyecto_Fusa")
    





if __name__ == "__main__":

    archivos = db["Archivos_audios"]
    personas = db["Usarios"]
    segmentos = db["segmentos"]
    listaNull = ["null","null","null","null","null" ,"null"]
    bole = True

    while True: 
        print("1 - Ingresa un usuario ")
        print("2 - Agregar Archivo de audio  ")
        print("3 - Analizar Automaticamente ")
        print("4 - Analizar Manualmente    ")
        print("5 - eliminar la base de datos ")
        print("6 - salir ")
        ele_menu = int(input(" : "))

        if ele_menu == 1:
            nom  = input("Ingresa tu nombre : ")
            apell = input("Ingresa tu apellido :") 
            rut = input("Ingresa tu rut :  ") 
            agregar_Persona(personas,nom,apell,rut)
            print("el usuario ", nom.upper() , "fue agregado a la base de datos exitosamente ")
            time.sleep(2)
            os.system("clear")
        if ele_menu == 2: 
            os.system("clear")
        if ele_menu == 3:
            os.system("clear")
        if ele_menu == 4 :
            os.system("clear") 


        if ele_menu == 5 : 
            eliminarData()
            print("base de datos eliminada")
            time.sleep(2)
            os.system("clear")
           
        
        if ele_menu == 6 :
            
            os.system("clear")
            print("Adios.....  :)") 
            break
        
        os.system("clear")

        

        



   

