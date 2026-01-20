import streamlit as st
import pandas as pd

st.title("Market")


products = pd.DataFrame({
    "Product": ["Leche", "Azucar", "Carne"],
    "Price": [10, 20, 30],
})

if st.session_state.get("selected_product") is None:
    st.session_state.selected_product = pd.DataFrame({
        "Product": [],
        "Quantity": [],
        "Price": [],
        "Subtotal": [],
    })

selected_product_name = st.selectbox("Select a product", products["Product"])
selected_price = products[products["Product"] == selected_product_name]["Price"].values[0]

col1, col2, col3 = st.columns(3)
with col1:
    quantity = st.number_input("Quantity", min_value=1, max_value=100)
with col2:
    st.metric("Price", f"L. {selected_price:.2f}")
with col3:
    st.metric("Subtotal", f"L. {selected_price * quantity:.2f}")

if st.button("Add to cart"):
    product_to_add = pd.DataFrame({
        "Product": [selected_product_name],
        "Quantity": [quantity],
        "Price": [selected_price],
        "Subtotal": [selected_price * quantity],
    })

    for index, row in st.session_state.selected_product.iterrows():
        if row["Product"] == selected_product_name:
            st.session_state.selected_product.at[index, "Quantity"] += quantity
            st.session_state.selected_product.at[index, "Subtotal"] += selected_price * quantity
            break
    else:
        st.session_state.selected_product = pd.concat([st.session_state.selected_product, product_to_add], ignore_index=True)
    




st.dataframe(st.session_state.selected_product)

st.divider()

col1, col2 = st.columns(2)
with col1:
    subtotal = st.session_state.selected_product["Subtotal"].sum()
    iva = subtotal * 0.16
    st.metric("IVA", f"L. {iva:.2f}")
with col2:
    st.metric("Total", f"L. {subtotal + iva:.2f}")