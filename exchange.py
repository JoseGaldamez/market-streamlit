import streamlit as st

def main():
    st.set_page_config(
        page_title="Conversor de Moneda USD -> HNL",
        page_icon="",
        layout="centered"
    )

    st.markdown("""
        <style>
        .main {
            background-color: #f5f7f9;
        }
        .stApp {
            max-width: 100%;
            padding: 20px;
        }
        .title-text {
            color: #1e3a8a;
            font-family: 'Helvetica Neue', sans-serif;
            text-align: center;
            font-weight: 700;
            margin-bottom: 2rem;
        }
        .result-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 20px;
        }
        .result-text {
            font-size: 24px;
            color: #333;
            font-weight: 500;
        }
        .result-value {
            font-size: 48px;
            color: #2563eb;
            font-weight: 700;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title-text'>Conversor USD a Lempiras</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.header("Configuración")
        st.write("Ajusta la tasa de cambio actual.")
        tasa_cambio = st.number_input(
            "Tasa de Cambio (HNL/USD)",
            min_value=1.0,
            value=25.40,
            step=0.01,
            format="%.2f"
        )
        st.info(f"Tasa actual: **1 USD = {tasa_cambio} HNL**")

    col1, col2 = st.columns([1, 2])

    with col2:
        st.write("### Ingrese el monto")
        usd_amount = st.number_input(
            "Monto en Dólares ($)",
            min_value=0.0,
            value=1.0,
            step=1.0,
            format="%.2f"
        )

    hnl_amount = usd_amount * tasa_cambio

    st.markdown(f"""
        <div class="result-box">
            <p class="result-text">Monto convertido:</p>
            <p class="result-value">L {hnl_amount:,.2f}</p>
            <p class="result-text" style="font-size: 16px; color: #666;">
                ({usd_amount:,.2f} USD * {tasa_cambio} HNL/USD)
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
