from io import open 
import os
from playsound import playsound
import base64



def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content)




def decode_audio(codigo):
    info = base64.b64decode(codigo)
    with open("audio.wav", mode ="bx")  as f:
        f.write(info)

















audioo = open("audios/Ladrido_de_Perro.wav","rb")
codigo_B = encode_audio(audioo)
decode_audio(codigo_B)

print("reproduccion...........")
playsound("audio.wav")


