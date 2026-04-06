# NatuClean-NLP-Explorer
Trabajo de NLP

# Explorador Semántico: Análisis de Arquitecturas de IA (NatuClean)

Este proyecto implementa una herramienta interactiva diseñada para explorar relaciones semánticas en documentos técnicos de Inteligencia Artificial. Utiliza un modelo neuronal para comprender el contexto de las palabras y una interfaz web para facilitar la interacción dinámica.

## Características Técnicas
- **Modelo de Lenguaje:** Word2Vec (Gensim) entrenado con un corpus de documentos técnicos sobre arquitecturas de IA.
- **Motor de Análisis:** Cálculo de **Similitud Coseno** y operaciones vectoriales para resolución de analogías.
- **Interfaz:** Aplicación web dinámica desarrollada con **Streamlit**.
- **Documentación:** El proyecto forma parte del desarrollo del sistema **NatuClean**.

## Contenido del Repositorio
* `app.py`: Script principal de la interfaz de Streamlit.
* `modelo_word2vec.model`: El modelo entrenado que contiene el vocabulario y los vectores.
* `Procesamiento_de_Lenguaje_Natural_(NLP).ipynb`: Cuaderno de trabajo original de Google Colab.
* `requirements.txt`: Lista de librerías necesarias (Gensim, Streamlit, Pandas).
* `7305_Chatboty_de_NatuClean (1).pdf`: Documento para colocarlo en archivos (dentro de colab) cuando se use el modelo.

## Instalación y Uso Local
Para ejecutar este explorador en tu propia máquina:

1. **Clonar el repositorio:**
   ```bash
   https://github.com/Noga32/NatuClean-NLP-Explorer.git

2. ## Instalar dependencias:
   streamlit run app.py

3. ## Lanzar la aplicación:
   streamlit run app.py 

   
