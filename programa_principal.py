import pandas as pd
import numpy as np

#seleccionar los datos de la base de datos que se ocuparán
datos_seleccionados = ["Title", "Genres", "Director", "Actor1", "Actor2", "Actor3"]

#Cargamos la base de datos
df = pd.read_excel('/content/movie-DB-2000s.xlsx', usecols = datos_seleccionados)

vector_entrada = np.array(vector_entrada)  # Convierte la lista en un array NumPy
vectores_bolsa = [np.array(vector) for vector in vectores_bolsa]  # Convierte cada lista en un array NumPy

# Calcula la similitud coseno
similarity_scores = cosine_similarity(vector_entrada.reshape(1, -1), np.stack(vectores_bolsa))

# Obtener los índices de las entradas más similares
top_indices = np.argsort(similarity_scores, axis=1)[:, -5:]

# Obtener las 5 mejores recomendaciones
top_recommendations = df.iloc[top_indices[0]]
