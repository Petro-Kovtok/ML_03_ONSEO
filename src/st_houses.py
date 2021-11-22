import streamlit as st
from modules.simple_ml_models import HousePriceModel

if __name__=="__main__":
    model = HousePriceModel()

    st.title("House Price Model")

    with st.form("house price form"):
        n_floors = st.number_input("n_floors", 1, 10, value=1)
        area = st.slider("area", 1, 300, value=50)
        heating = st.radio("heating", ("A","B","C","D"))

        submitted = st.form_submit_button("submit")

        if submitted:
            prediction = model(n_floors=n_floors, area=area, heating=heating)
            st.write(f"House Price: {prediction} $")