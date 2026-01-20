import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Registro Académico", layout="wide")

st.title("Registro de Asignaturas Matriculadas")

if "asignaturas" not in st.session_state:
    st.session_state.asignaturas = pd.DataFrame(columns=[
        "Estudiante", "Asignatura", "Código", "Fecha de Registro", 
        "Hora Inicio", "Hora Final", "Aula", 
        "Maestro", "Campus"
    ])

with st.container():
    st.subheader("Ingresar Matrícula de Estudiante")
    with st.form("registro_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            nombre_estudiante = st.text_input("Nombre del Estudiante")
            asignatura = st.selectbox("Asignatura", [
                "Matemáticas Discretas",
                "Programación Orientada a Objetos",
                "Base de Datos I",
                "Ingeniería de Software",
                "Redes de Computadoras"
            ])
            codigo = st.text_input("Código de Asignatura")

        with col2:
            campus = st.selectbox("Campus", [
                "San Pedro Sula", "Tegucigalpa", 
                "La Ceiba", "El Progreso", "Virtual"
            ])
            fecha_registro = st.date_input("Fecha de Registro", datetime.now())
            hora_inicio = st.time_input("Hora de Inicio")

        with col3:
            hora_final = st.time_input("Hora Final")
            aula = st.text_input("Aula")
            maestro = st.text_input("Maestro")

        submitted = st.form_submit_button("Registrar Matrícula")

        if submitted:
            if nombre_estudiante and codigo and maestro:
                new_data = pd.DataFrame([{
                    "Estudiante": nombre_estudiante,
                    "Asignatura": asignatura,
                    "Código": codigo,
                    "Fecha de Registro": fecha_registro,
                    "Hora Inicio": hora_inicio,
                    "Hora Final": hora_final,
                    "Aula": aula,
                    "Maestro": maestro,
                    "Campus": campus
                }])
                
                st.session_state.asignaturas = pd.concat(
                    [st.session_state.asignaturas, new_data], 
                    ignore_index=True
                )
                st.success("¡Matrícula registrada correctamente!")
                st.rerun()
            else:
                st.error("Por favor completa el Nombre del Estudiante, Código y Maestro.")

st.divider()

st.subheader("Reporte de Asignaturas por Campus")

if not st.session_state.asignaturas.empty:
    campuses_activos = st.session_state.asignaturas["Campus"].unique()
    
    for campus in campuses_activos:
        st.markdown(f"### 🏫 Campus {campus}")
        
        df_campus = st.session_state.asignaturas[
            st.session_state.asignaturas["Campus"] == campus
        ].drop(columns=["Campus"])
        
        st.dataframe(
            df_campus,
            use_container_width=True,
            hide_index=True
        )
else:
    st.info("No hay matrículas registradas aún.")
