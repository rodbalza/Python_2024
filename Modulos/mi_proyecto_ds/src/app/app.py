# app.py
import streamlit as st
from modelo import entrenar_modelo

def main():
    st.title("Predicción de Ingresos según Edad")
    datos = cargar_datos("data/dataset.csv")
    modelo_entrenado = entrenar_modelo(datos)

    edad_input = st.slider("Selecciona una edad:", 20, 60, 30)
    predicciones = modelo_entrenado.predict([[edad_input]])

    st.write(f"Ingresos estimados para una edad de {edad_input} años: ${predicciones[0]:,.2f}")

if __name__ == "__main__":
    main()
