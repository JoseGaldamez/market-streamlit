import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Costos Universitarios",
    page_icon="🎓",
    layout="centered"
)

# Inicializar estado de sesión para guardar las materias
if 'materias_seleccionadas' not in st.session_state:
    st.session_state['materias_seleccionadas'] = []

st.title("🎓 Calculadora de Materias")
st.markdown("Selecciona las materias que deseas matricular para ver el costo total.")

# Sidebar para configuración
with st.sidebar:
    st.header("⚙️ Configuración")
    # Costo por crédito para hacerlo más dinámico
    costo_por_credito = st.number_input("Costo por Crédito (USD)", min_value=0.0, value=50.0, step=5.0)
    moneda = st.selectbox("Moneda", ["USD", "EUR", "COP", "MXN"])
    
    st.divider()
    if st.button("🗑️ Limpiar Lista"):
        st.session_state['materias_seleccionadas'] = []
        st.rerun()

# Definir lista de materias disponibles y sus créditos
# En un caso real, esto podría venir de una base de datos o archivo JSON
materias_disponibles = {
    "Cálculo Diferencial": 4,
    "Física Mecánica": 3,
    "Programación Orientada a Objetos": 3,
    "Base de Datos I": 3,
    "Ingeniería de Software": 4,
    "Algoritmos y Estructuras": 3,
    "Probabilidad y Estadística": 3,
    "Ética Profesional": 2,
    "Electiva de Humanidades": 2
}

# Contenedor para la selección
container_seleccion = st.container(border=True)
with container_seleccion:
    col1, col2 = st.columns([3, 1])

    with col1:
        materia_seleccionada = st.selectbox(
            "Selecciona una materia:", 
            options=list(materias_disponibles.keys())
        )

    with col2:
        # Espacio vertical para alinear el botón con el selectbox
        st.write("") 
        st.write("")
        boton_agregar = st.button("➕ Agregar", use_container_width=True)

    if boton_agregar:
        # Verificar si ya está en la lista para no duplicar
        nombres_en_lista = [m['Materia'] for m in st.session_state['materias_seleccionadas']]
        
        if materia_seleccionada not in nombres_en_lista:
            creditos = materias_disponibles[materia_seleccionada]
            # Guardamos créditos, el costo se calcula dinámicamente al mostrar
            nuevo_item = {
                "Materia": materia_seleccionada,
                "Créditos": creditos
            }
            st.session_state['materias_seleccionadas'].append(nuevo_item)
            st.success(f"✅ {materia_seleccionada} agregada.")
        else:
            st.warning(f"⚠️ {materia_seleccionada} ya está en la lista.")

# Mostrar lista y cálculos
st.divider()

if len(st.session_state['materias_seleccionadas']) > 0:
    # Convertir lista a DataFrame
    df = pd.DataFrame(st.session_state['materias_seleccionadas'])
    
    # Calcular columna de costo basada en el valor actual del sidebar
    df['Costo'] = df['Créditos'] * costo_por_credito
    
    col_izq, col_der = st.columns([2, 1])
    
    with col_izq:
        st.subheader("📋 Resumen de Matrícula")
        st.dataframe(
            df, 
            use_container_width=True,
            column_config={
                "Costo": st.column_config.NumberColumn(
                    "Costo Estimado",
                    format=f"$%.2f {moneda}"
                )
            }
        )
    
    with col_der:
        # Cálculos finales
        total_creditos = df['Créditos'].sum()
        total_pagar = df['Costo'].sum()
        
        st.subheader("💰 Totales")
        st.metric("Total Créditos", total_creditos)
        st.metric("Total a Pagar", f"{total_pagar:,.2f} {moneda}")
        
else:
    st.info("� Selecciona materias arriba y presiona 'Agregar' para comenzar tu plan de estudios.")
