import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    st.title("Streamlit Demo")

    df = pd.DataFrame(np.random.randn(20,20), columns = [f'col_{i}' for i in range(20)])
    st.dataframe(df)