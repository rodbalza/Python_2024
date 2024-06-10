from io import open

fichero = open("Personas", "r",  encoding='utf-8') 
lineas = fichero.readlines()
fichero.close()


personas = []

for linea in lineas:
    linea.replace("\n", "")
    campos = linea.split(";")
    persona = {'id': campos[0], 'nombre': campos[1], 'apellido': campos[2], 'nacimiento': campos[3]}
    personas.append(persona)

print(personas)