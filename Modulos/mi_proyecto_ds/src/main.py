# Punto de entrada principal
from preprocesamiento import cargar_datos
from modelo import entrenar_modelo

if __name__ == "__main__":
    datos = cargar_datos("data/dataset.csv")
    modelo_entrenado = entrenar_modelo(datos)
    # Lógica adicional según tu proyecto
