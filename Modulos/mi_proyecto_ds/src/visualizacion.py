# Funciones para visualizar resultados
import matplotlib.pyplot as plt

def graficar_resultados(modelo, datos):
    plt.scatter(datos["Edad"], datos["Ingresos"], label="Datos reales")
    plt.plot(datos["Edad"], modelo.predict(datos[["Edad"]]), color="red", label="Modelo")
    plt.xlabel("Edad")
    plt.ylabel("Ingresos")
    plt.legend()
    plt.show()

# Otras funciones de visualización
