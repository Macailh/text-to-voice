import typer
from gtts import gTTS


app = typer.Typer()


def convert(txt_file: str, audio_name: str):
    try:
        archivo = open(txt_file + ".txt", "r", encoding="utf-8")
        texto = archivo.read()
        archivo.close()
    except FileNotFoundError as exc:
        typer.echo("ERROR: No se pudo abrir el archivo de texto")
        typer.echo(
            "Verifique que el archivo se encuentre en la misma carpeta que el programa")
        typer.echo("saliendo...")
        raise typer.Exit() from exc

    tts = gTTS(text=texto, lang="es")
    tts.save(audio_name + ".mp3")
    typer.echo("Audio generado correctamente")


@app.command()
def main(txt_file: str, audio_name: str):
    convert(txt_file, audio_name)


def run():
    app()


if __name__ == "__main__":
    run()
