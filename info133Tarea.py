from re import A
from Cython.Shadow import NULL
from pymongo import MongoClient
import os
import time
import folium
import webbrowser
import branca
from io import open 
import base64
from folium import plugins
from playsound import playsound



#--------------------#
client = MongoClient("localhost")
#--------------------#
db = client["proyecto_Fusa"]
#--------------------#


def agregar_Archivos(sonidoL,AcodigoB,archivos,fechaGrabacion, cuidad, duracion,formato, lista_ubicacion, rut,categoria):
    archivos.insert_one({
        "sonidoN" : sonidoL,
        "AcodigoB" : AcodigoB, 
        "fecha de grabacion" : fechaGrabacion,
        "cuidad" : cuidad,
        "duracion" : duracion,
        "formato" : formato,
        "ubicacion" : {

            "Latitud" : lista_ubicacion[0],
            "Longitud" :  lista_ubicacion[1],        
            "Exterior_Interior" : lista_ubicacion[2]
        },

        "rut_propietario" : rut,  
        "Categoria " : categoria           
    })

def agregar_Persona(personas,nombreP,apellidoP,rutP,):


    personas.insert_one({
        "Nombre" : nombreP,
        "Apellido" :apellidoP,
        "Rut" : rutP

    })

def Agregar_Segmento_audio(id_archivo_A,segmento,categoria ,listaSegmentos, nombre_fuentes,descripcion,ID_analizador ):

    segmento.insert_one({
        "ID_Archivos_A" : id_archivo_A,
        "ID" : listaSegmentos[0],
        "Categoria" : categoria,
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
    
def buscarPersona(data,rut,estado):


    doc = data.find_one({
        "Rut" : rut
    })
    print()
    if estado == 1:

        try:

            print("el Usuario Buscado es : ")
            print("Nombre : ",doc["Nombre"])
            print("Apellido : ", doc["Apellido"])
            time.sleep(2)
            informacion_archivo_audio(archivos, rut)
            

        except: 
            print("ocurrio un error....")
    
    if estado == 2:
        try:
            return doc["Nombre"]
        except:
            return "Error........"
        
    

def informacion_archivo_audio(data, rut):
    
    '''
    print("hola")
    doc = data.find_one({
        "sonido" : nombre
    })
    '''
    ### metodo solo para pruebas 
    ###data1 =data.find()
    
    num  = data.count({
        "rut_propietario" : rut
    })
    os.system("clear")
    
    
    if num >= 1:
        print("tu usuario cuenta con registro de audio ")
        print()

        H = data.find({

            "rut_propietario" : rut
        })
        for i in H:
            print("audio asociado : {}".format(i[ "sonidoN"]))

        print("---------------------------------------------------------")
        validador = input("quieres escuchar un audio ? (Y/N) : ")
        if validador.upper() == "Y":
            nombreA = input("Ingresa el nombre del audio : ")
            reproducir_sonido(data,nombreA)
        else: 
            pass 

    else: 
        print("usuario no cuenta con registros de audio :( ")
    


    '''
    H = data.find({
        "rut_propietario" : rut
    })
    for i in H:
        print("audio asociado : {}".format(i[ "sonido"]))
    '''  
def Crear_mapa(data,estado,categoria,fecha):

    
    ##marcador1 = folium.Marker(location= [-39.82857809929557, -73.23505522174938],popup=folium.Popup(iframe1, max_width=500),icon=folium.Icon(color="black"))
    if estado == 1:

        mapa = folium.Map(location=[-39.81730435463257, -73.24257650930436], zoom_start=10)
        for i in data.find():
            html = '''
                    <p> - Nombre de audio : {} </p>
                    <p>- Duracion : {}  </p>
                    <p> - fecha de grabacion : {}  </p>
                    <p> - rut del propietario : {}  </p>
                    '''.format(i["sonidoN"],i["duracion"],i["fecha de grabacion"],i["rut_propietario"])
                    
            iframe1 = branca.element.IFrame(html=html, width=500, height=300)
            marcador = folium.Marker(location= [i["ubicacion"]["Latitud"],i["ubicacion"]["Longitud"]],popup=folium.Popup(iframe1, max_width=500),icon=folium.Icon(color="black"))
            marcador.add_to(mapa)

        mapa.save("mapa_test.html")
        webbrowser.open("mapa_test.html")

    if estado== 2 : 

        mapa2 = folium.Map(location=[-39.81730435463257, -73.24257650930436], zoom_start=10)
        for i in data.find({
            "Categoria " : categoria
        }):
            html = '''
                    <p> - Nombre de audio : {} </p>
                    <p>- Duracion : {}  </p>
                    <p> - fecha de grabacion : {}  </p>
                    <p> - rut del propietario : {}  </p>
                    '''.format(i["sonidoN"],i["duracion"],i["fecha de grabacion"],i["rut_propietario"])
                    
            iframe1 = branca.element.IFrame(html=html, width=500, height=300)
            marcador = folium.Marker(location= [i["ubicacion"]["Latitud"],i["ubicacion"]["Longitud"]],popup=folium.Popup(iframe1, max_width=500),icon=folium.Icon(color="black"))
            marcador.add_to(mapa2)

        mapa2.save("mapa2_test.html")
        webbrowser.open("mapa2_test.html")

    if estado == 3: 
        mapa2 = folium.Map(location=[-39.81730435463257, -73.24257650930436], zoom_start=10)
        for i in data.find({
            "fecha de grabacion" : fecha
        }):
            html = '''
                    <p> - Nombre de audio : {} </p>
                    <p>- Duracion : {}  </p>
                    <p> - fecha de grabacion : {}  </p>
                    <p> - rut del propietario : {}  </p>
                    '''.format(i["sonidoN"],i["duracion"],i["fecha de grabacion"],i["rut_propietario"])
                    
            iframe1 = branca.element.IFrame(html=html, width=500, height=300)
            marcador = folium.Marker(location= [i["ubicacion"]["Latitud"],i["ubicacion"]["Longitud"]],popup=folium.Popup(iframe1, max_width=500),icon=folium.Icon(color="black"))
            marcador.add_to(mapa2)

        mapa2.save("mapa2_test.html")
        webbrowser.open("mapa2_test.html")

    if estado == 4: 
        mapa2 = folium.Map(location=[-39.81730435463257, -73.24257650930436], zoom_start=10)
        for i in data.find({
            "Categoria " : categoria,
            "fecha de grabacion" : fecha
        }):
            html = '''
                    <p> - Nombre de audio : {} </p>
                    <p>- Duracion : {}  </p>
                    <p> - fecha de grabacion : {}  </p>
                    <p> - rut del propietario : {}  </p>
                    '''.format(i["sonidoN"],i["duracion"],i["fecha de grabacion"],i["rut_propietario"])
                    
            iframe1 = branca.element.IFrame(html=html, width=500, height=300)
            marcador = folium.Marker(location= [i["ubicacion"]["Latitud"],i["ubicacion"]["Longitud"]],popup=folium.Popup(iframe1, max_width=500),icon=folium.Icon(color="black"))
            marcador.add_to(mapa2)

        mapa2.save("mapa2_test.html")
        webbrowser.open("mapa2_test.html")

def encode_audio(nombre):
    audio = open("audios/"+nombre+".wav","rb")
    audio_content = audio.read()
    return base64.b64encode(audio_content)

def reproducir_sonido(data,nombre):

    try:

        os.remove("audio.wav")
    except:
        print()
        pass
    H = data.find_one({

        "sonidoN" : nombre
    })
    codeB = H["AcodigoB"]
    info = base64.b64decode(codeB)
    with open("audio.wav", mode ="bx")  as f:
        f.write(info)

    
    playsound("audio.wav")
    os.remove("audio.wav")

def menu():
     while True: 
        print("1 - Ingresa un usuario ")
        print("2 - Buscar  un usuario ")
        print("3 - Agregar Archivo de audio  ")
        print("4 - Analizar Automaticamente ")
        print("5 - Analizar Manualmente    ")
        print("6 - eliminar la base de datos ")
        print("7 - mapa")
        print("8 - salir ")
        print()
        print("Escribe una opción del 1 al 8 ")
        ele_menu = int(input(" : "))

        if ele_menu == 1:
            nom  = input("Ingresa tu nombre : ")
            apell = input("Ingresa tu apellido :") 
            rut = input("Ingresa tu rut :  ") 
            agregar_Persona(personas,nom,apell,rut.upper())
            print("el Usuario ", nom.upper() , "fue agregado a la base de datos exitosamente ")
            time.sleep(2)
            os.system("clear")
        if ele_menu ==2:
            
            rut = input("Ingresa el rut de la persona que quieras buscar : ")
            buscarPersona(personas,rut.upper(),1)
            
            q = input("presione ENTER para volver al menu principal")
            os.system("clear")

        
        if ele_menu == 3: 
            rut= input("Ingrese el rut del usuario : ")
            os.system("clear")
            nombre = buscarPersona(personas,rut.upper(),2)
            print("Hola {} ".format(nombre))
            print("Ingresa el nombre de tu archivo de audio ")
            nom_archivo =input( ": " )

            agregar_Archivos(nom_archivo,
                            encode_audio(nom_archivo),
                            archivos,
                            input("ingresa la fecha de grabacion : "),
                            input("cuidad de la grabacion : "),
                            input("duracion : "),
                            "wav",
                            [float(input("Latitud : ")),float(input("Longitud : ")),"exterior"],
                            rut,
                            input("ingresa la categoria :"))
               
        
            


            os.system("clear")


            
        if ele_menu == 4:
            informacion_archivo_audio(archivos, input("ingresa tu rut : "))
            
                                            

            time.sleep(2)
            os.system("clear")###realizando prueebas
        if ele_menu == 5 :
            os.system("clear") 


        if ele_menu == 6 : 
            eliminarData()
            print("base de datos eliminada")
            time.sleep(2)
            os.system("clear")
           
        
        if ele_menu == 7 :
            os.system("clear")
            while True:
                print(" 1- ver mapa completo")
                print(" 2- filtrar por categoria ")
                print(" 3- filtrar por fecha "  )
                print(" 4 - filtrar por fecha y categoria")
                print(" 5 - Ir al menu principal")
                print("Escribe una opción del 1 al 5 ")
                ele_menu = int(input(" : " ))

                if ele_menu==1:
                    Crear_mapa(archivos,1,"animales",0)
                    time.sleep(1)
                    os.system("clear")
                if ele_menu==2:
                    os.system("clear")
                    print("tipos de filtro :") 
                    print("1- Humanos    4- Climatico y medio ambientales  7- Alertas")
                    print("2- Música     5- Mécanicos")
                    print("3- Animales   6- Vehiculos")

                    cate = input("Ingresa el nombre de la categoria : ")
                    Crear_mapa(archivos,2,cate,0)
                    time.sleep(1)
                    os.system("clear")
                if ele_menu==3:
                    fe = input("Ingrese la fecha : ")
                    Crear_mapa(archivos,3,"null",fe)
                    time.sleep(1)
                    os.system("clear")
                if ele_menu ==4 :
                    cate = input("Ingresa el nombre de la categoria : ")
                    fe = input("Ingrese la fecha : ")
                    Crear_mapa(archivos,4,cate,fe)
                    time.sleep(1)
                    os.system("clear")




                if ele_menu==5:
                    os.system("clear")
                    break


        if ele_menu == 8:

            os.system("clear")
            print("Adios.....  :)") 
            break

##------------------------------------------------------------------------------------------------------------------------------------------------------##

if __name__ == "__main__":

    archivos = db["Archivos_audios"]
    personas = db["Usarios"]
    segmentos = db["segmentos"]
    menu()

    

    

   

