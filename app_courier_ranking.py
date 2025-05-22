
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ranking Couriers", layout="centered")

st.image("https://i.imgur.com/dnQak6S.png", width=120)
st.title("Consulta tu Ranking - Solucioning Delivery")
st.write("Introduce tu ID de Courier para ver tus resultados semanales:")

courier_id = st.text_input("Introduce tu ID de Courier:")

try:
    df = pd.read_excel("Ranking_Couriers_Semanal.xlsx")

    # Normalizar columnas para evitar errores por mayúsculas/minúsculas
    df.columns = df.columns.str.upper()

    if courier_id:
        resultados = df[df['IDCOURIER'].astype(str) == courier_id]

        if resultados.empty:
            st.warning("No se han encontrado datos para este ID.")
        else:
            columnas_mostrar = [
                "SEMANA","VEHICULO", "ORDENES", "EFICIENCIA", "CDT", "VELOCIDAD",
                "CAPU", "NO PRESENTADO", "REASIGNACIONES",
                "HORAS TRABAJADAS", "RANKING", "TOTAL INCENTIVOS"
            ]
            columnas_presentes = [col for col in columnas_mostrar if col in resultados.columns]
            st.success("Resultados encontrados:")
            st.dataframe(resultados[columnas_presentes].reset_index(drop=True))
except Exception as e:
    st.error(f"Ocurrió un error al procesar los datos: {e}")
