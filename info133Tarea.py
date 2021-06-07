from pymongo import MongoClient
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


def Arregar_Segmento_audio(segmento, listaSegmentos, nombre_fuentes,descripcion,ID_analizador ):

    segmento.inset_one({
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










if __name__ == "__main__":

    archivos = db["Archivos_audios"]
    personas = db["Usarios"]
    segmentos = db["segmentos"]

    agregar_Persona(personas,"bastian","villanueva","20135031k")
    client.drop_database("proyecto_Fusa")
   



   

