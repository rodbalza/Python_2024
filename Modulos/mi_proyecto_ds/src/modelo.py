# Funciones para entrenar y evaluar el modelo
from sklearn.linear_model import LinearRegression

def entrenar_modelo(datos):
    X = datos[["Edad"]]
    y = datos["Ingresos"]
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

# Otras funciones relacionadas con el modelo
