from gtts import gTTS


txt_file = input("Ingrese el nombre del archivo de texto: ")
audio_name = input("Ingrese el nombre que tendra el archivo de audio final: ")

archivo = open(txt_file + ".txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

tts = gTTS(text=texto, lang="es")
tts.save(audio_name + ".mp3")
