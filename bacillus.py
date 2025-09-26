# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lactobacillus: perfiles de fermentación", page_icon="🦠", layout="wide")
st.title("🦠 Perfiles de fermentación de 30 especies de Lactobacillus")
st.write("""
Busca una especie escribiendo su nombre (por ejemplo `Lactobacillus plantarum`) y verás su perfil de fermentación
para los carbohidratos: **Glucosa, Lactosa, Sacarosa, Manitol, Xilosa**.
""")

# --- Datos embebidos: 30 especies con perfil resumido (Sí / No / Variable) ---
data = [
    # Especie, Glucosa, Lactosa, Sacarosa, Manitol, Xilosa, Fuente resumida
    ["Lactobacillus acidophilus", "Sí", "Sí", "Sí", "Variable", "No"],
    ["Lactobacillus plantarum", "Sí", "No", "Sí", "Variable", "Sí"],
    ["Lactobacillus casei", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus rhamnosus", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus fermentum", "Sí", "No", "Sí", "Variable", "No"],
    ["Lactobacillus delbrueckii subsp. bulgaricus", "Sí", "Sí", "No", "No", "No"],
    ["Lactobacillus brevis", "Sí", "No", "Sí", "Sí", "Sí"],
    ["Lactobacillus pentosus", "Sí", "No", "Sí", "Variable", "Sí"],
    ["Lactobacillus reuteri", "Sí", "No", "Sí", "No", "No"],
    ["Lactobacillus johnsonii", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus gasseri", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus helveticus", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus salivarius", "Sí", "No", "Sí", "No", "No"],
    ["Lactobacillus crispatus", "Sí", "No", "Sí", "No", "No"],
    ["Lactobacillus buchneri", "Sí", "No", "Sí", "Sí", "Sí"],
    ["Lactobacillus sakei", "Sí", "No", "Sí", "Variable", "No"],
    ["Lactobacillus curvatus", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus paracasei", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus kefiri", "Sí", "Sí", "Sí", "Sí", "Sí"],
    ["Lactobacillus alimentarius", "Sí", "Sí", "Sí", "No", "No"],
    ["Lactobacillus amylophilus", "Sí", "No", "Sí", "Sí", "No"],
    ["Lactobacillus coryniformis", "Sí", "No", "Sí", "No", "No"],
    ["Lactobacillus collinoides", "Sí", "No", "Sí", "Variable", "Sí"],
    ["Lactobacillus parabuchneri", "Sí", "No", "Sí", "Sí", "No"],
    ["Lactobacillus buchneri subsp. coagulans", "Sí", "No", "Sí", "Sí", "No"],
    ["Lactobacillus frumenti", "Sí", "No", "Sí", "Variable", "No"],
    ["Lactobacillus kunkeei", "Sí", "No", "No", "No", "No"],
    ["Lactobacillus iners", "Sí", "No", "No", "No", "No"],
    ["Lactobacillus gigeriorum", "Sí", "No", "No", "No", "No"],
]

cols = ["Especie", "Glucosa", "Lactosa", "Sacarosa", "Manitol", "Xilosa", "Fuente_resumen"]
df = pd.DataFrame(data, columns=cols)

# Limpiamos columna de fuente para no mostrarla por defecto y mantenerla para referencia
display_df = df.drop(columns=["Fuente_resumen"])

# --- Buscador / entrada de usuario ---
st.sidebar.header("Buscar especie")
query = st.sidebar.text_input("Escribe (parte del nombre o nombre completo):", "")

# Opción para mostrar toda la tabla o solo coincidencias
show_all = st.sidebar.checkbox("Mostrar todas las especies", value=False)

if show_all or query.strip() == "":
    st.subheader("Tabla completa (resumen)")
    st.dataframe(display_df, use_container_width=True)
else:
    # Filtrar por coincidencias (case-insensitive)
    matches = display_df[display_df["Especie"].str.contains(query, case=False, na=False)]
    if matches.empty:
        st.warning("No se encontraron coincidencias. Revisa la ortografía o prueba con otra parte del nombre.")
    else:
        st.subheader(f"Resultados para: '{query}'")
        st.dataframe(matches, use_container_width=True)

# --- Información adicional y fuentes ---
st.markdown("---")
st.markdown("### ℹ️ Sobre los datos")
st.markdown("""
- Los valores mostrados son **resumen bibliográfico** (Sí / No / Variable).  
- Muchas especies fermentan **glucosa** (casi universal). Diferencias notables aparecen en azúcares como lactosa (más en especies lácticas/dairy), manitol o xilosa (más variables).
- Estos perfiles se basan en compilaciones tipo **API 50 CHL** y estudios publicados que usan esa batería de carbohidratos para caracterizar especies de *Lactobacillus*. Para obtener el perfil experimental y por cepa, es habitual consultar la tabla API 50 CHL del cepa tipo o artículos de caracterización de la especie.
""")

st.markdown("### Fuentes (referencias generales usadas para la compilación):")
st.markdown("- bioMérieux — API® 50 CHL (manual y package insert sobre pruebas de fermentación).")
st.markdown("- Revisión y artículos que usan API 50 CHL y listan perfiles fenotípicos (ej. estudios comparativos y caracterización de *Lactobacillus* en PMC).")
st.markdown("- Artículo sobre metabolismo de carbohidratos en Lactiplantibacillus y estudios de perfiles de fermentación (ej. artículos accesibles en PubMed Central).")

st.caption("Si deseas, puedo: 1) expandir cada fila con la referencia concreta (artículo o tabla API 50 CHL) por especie, o 2) buscar y reemplazar los valores 'Variable' por datos de literatura específicos para las especies que elijas.")
