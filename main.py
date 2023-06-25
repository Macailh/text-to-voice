from gtts import gTTS


txt_file = input("Ingrese el nombre del archivo de texto: ")

try:
    archivo = open(txt_file + ".txt", "r", encoding="utf-8")
    texto = archivo.read()
    archivo.close()
except FileNotFoundError:
    print("ERROR: No se pudo abrir el archivo de texto")
    print("Verifique que el archivo se encuentre en la misma carpeta que el programa")
    print("saliendo...")
    exit()

audio_name = input("Ingrese el nombre que tendra el archivo de audio final: ")

tts = gTTS(text=texto, lang="es")
tts.save(audio_name + ".mp3")
