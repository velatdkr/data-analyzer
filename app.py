import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Analyseur de fichiers CSV")

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    st.subheader("Visualisation")
    column = st.selectbox("Choisissez une colonne numérique à visualiser", df.select_dtypes(include="number").columns)

    if column:
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=20)
        ax.set_title(f"Distribution de {column}")
        st.pyplot(fig)
