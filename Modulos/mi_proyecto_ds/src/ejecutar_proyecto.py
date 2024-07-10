# Ejecución Automatizada del Proyecto

import os
import subprocess

def ejecutar_proyecto():
    # Ruta al archivo principal (main.py o el nombre que le hayas dado)
    ruta_archivo_principal = "src/main.py"

    # Comando para ejecutar el archivo principal
    comando = f"python {ruta_archivo_principal}"

    try:
        # Ejecuta el comando en la terminal
        subprocess.run(comando, shell=True, check=True)
        print("Proyecto ejecutado con éxito.")
    except subprocess.CalledProcessError:
        print("Error al ejecutar el proyecto.")

if __name__ == "__main__":
    ejecutar_proyecto()
