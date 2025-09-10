# ==============================
# 1. Importar librerías
# ==============================
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# 2. Configuración de la app
# ==============================
st.set_page_config(page_title="Dashboard Segmentación Clientes", layout="wide")
st.title("📊 Dashboard - Segmentación de Clientes")
st.markdown("Exploración y análisis descriptivo de clientes de una entidad financiera.")

# ==============================
# 3. Cargar datos
# ==============================
df = pd.read_excel("buenosclientes.xlsx")

# ==============================
# 4. Filtros
# ==============================
st.sidebar.header("⚙️ Filtros")
segmento_filter = st.sidebar.multiselect(
    "Selecciona segmentos:",
    options=df["segmento cash"].unique(),
    default=df["segmento cash"].unique()
)
df_filtered = df[df["segmento cash"].isin(segmento_filter)]

# ==============================
# 5. Pestañas para análisis
# ==============================
tab1, tab2, tab3, tab4 = st.tabs(["📑 Vista de Datos", "📌 Estadísticas", "📊 Distribuciones", "📈 Relaciones"])

# --- TAB 1: Vista de datos ---
with tab1:
    st.subheader("👀 Vista previa de los datos filtrados")
    st.dataframe(df_filtered.head(20))

# --- TAB 2: Estadísticas ---
with tab2:
    st.subheader("📌 Estadísticas descriptivas")
    st.write(df_filtered.describe(include="all"))

    st.subheader("📊 Conteo de clientes por segmento")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x="segmento cash", data=df_filtered, order=df_filtered["segmento cash"].value_counts().index, palette="Set2", ax=ax)
    st.pyplot(fig)

# --- TAB 3: Distribuciones ---
with tab3:
    st.subheader("📊 Distribución de variables numéricas")
    numeric_cols = df_filtered.select_dtypes(include=["int64","float64"]).columns

    if len(numeric_cols) > 0:
        var = st.selectbox("Selecciona variable numérica", numeric_cols)
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df_filtered[var].dropna(), kde=True, bins=20, ax=ax, color="skyblue")
        ax.set_title(f"Distribución de {var}")
        st.pyplot(fig)

# --- TAB 4: Relaciones ---
with tab4:
    st.subheader("📈 Relación entre variables")
    if len(numeric_cols) > 1:
        x_var = st.selectbox("Variable X", numeric_cols, index=0)
        y_var = st.selectbox("Variable Y", numeric_cols, index=1)

        fig, ax = plt.subplots(figsize=(6,4))
        sns.scatterplot(x=df_filtered[x_var], y=df_filtered[y_var], hue=df_filtered["segmento cash"], palette="Set1", ax=ax)
        ax.set_title(f"{x_var} vs {y_var} por segmento")
        st.pyplot(fig)

    st.subheader("📉 Correlación entre variables numéricas")
    corr = df_filtered[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
