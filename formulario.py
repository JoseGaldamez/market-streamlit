import streamlit as st

st.title("Formulario")

with st.form("formulario"):
    st.write("Dentro del formulario")
    name = st.text_input("Nombre")
    age = st.number_input("Edad", min_value=0, max_value=120)
    country = st.selectbox("País", ["Honduras", "Colombia", "Perú", "Argentina"])
    slider_val = st.slider("Slider", min_value=0, max_value=100)
    checkbox_val = st.checkbox("Checkbox")

    # Este botón envía el formulario
    submitted = st.form_submit_button("Enviar")
    if submitted:
        st.write("Nombre: ", name)
        st.write("Edad: ", age)
        st.write("País: ", country)
        st.write("Slider: ", slider_val)
        st.write("Checkbox: ", checkbox_val)


