%%writefile app.py
import streamlit as st
from gensim.models import Word2Vec

# Cargar modelo
modelo = Word2Vec.load("modelo_word2vec.model")

st.title("Explorador Semántico de IA")

st.markdown("Modelo entrenado con documento técnico sobre arquitecturas de IA")

# SIMILITUD
st.header("Similitud entre palabras")

w1 = st.text_input("Palabra 1")
w2 = st.text_input("Palabra 2")

if st.button("Calcular similitud"):
    try:
        sim = modelo.wv.similarity(w1, w2)
        st.success(f"Similitud: {sim:.4f}")
    except:
        st.error("Error en palabras")

# PALABRAS SIMILARES
st.header("Palabras similares")

palabra = st.text_input("Palabra base")

if palabra:
    try:
        similares = modelo.wv.most_similar(palabra)
        st.write(similares)
    except:
        st.error("No encontrada")

# ANALOGÍAS
st.header("Analogías")

p1 = st.text_input("Positivo 1")
p2 = st.text_input("Positivo 2")
n1 = st.text_input("Negativo")

if st.button("Resolver analogía"):
    try:
        resultado = modelo.wv.most_similar(
            positive=[p1, p2],
            negative=[n1]
        )
        st.write(resultado)
    except:
        st.error("Error")

#El modelo fue entrenado sobre un documento técnico real, y su calidad se validó
#mediante métricas de similitud, coherencia semántica y visualización. Además, se implementó una interfaz
#interactiva que permite explorar dinámicamente el conocimiento aprendido.