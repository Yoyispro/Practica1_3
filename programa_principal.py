import pandas as pd
import numpy as np

#seleccionar los datos de la base de datos que se ocuparán
datos_seleccionados = ["Title", "Genres", "Director", "Actor1", "Actor2", "Actor3"]

#Cargamos la base de datos
df = pd.read_excel('/content/movie-DB-2000s.xlsx', usecols = datos_seleccionados)

vector_entrada = np.array(vector_entrada)  # Convierte la lista en un array NumPy
vectores_bolsa = [np.array(vector) for vector in vectores_bolsa]  # Convierte cada lista en un array NumPy

# Obtener los índices de las entradas más similares
top_indices = np.argsort(similarity_scores, axis=1)[:, -5:]

# Encuentra los índices de las películas con las menores distancias (las más similares)
top_cosine_indices = np.argsort(cosine_distances)[0][:5]
top_jaccard_indices = np.argsort(jaccard_distances)[0][:5]

top_cosine_recommendations = data.iloc[top_cosine_indices]['Title']
top_jaccard_recommendations = data.iloc[top_jaccard_indices]['Title']

print("Recomendaciones basadas en similitud de coseno:")
print(top_cosine_recommendations)

print("\nRecomendaciones basadas en similitud de Jaccard:")
print(top_jaccard_recommendations)
