import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titel der App
st.title("Beispiel-Dataset Viewer")

# Laden des Beispiel-Datasets
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Anzeige der Rohdaten
if st.checkbox("Rohdaten anzeigen"):
    st.write(data)

# Auswahl der Spalte für die Darstellung
st.sidebar.header("Darstellungsoptionen")
plot_type = st.sidebar.radio("Wähle die Art der Darstellung", ("Tabelle", "Grafik"))

# Anzeige der Daten in Tabellenform
if plot_type == "Tabelle":
    st.write(data)
else:
    # Auswahl der zu plottenden Spalten
    x_axis = st.sidebar.selectbox("X-Achse", data.columns)
    y_axis = st.sidebar.selectbox("Y-Achse", data.columns)


    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)
