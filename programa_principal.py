import pandas as pd
import numpy as np

def cosine_distances(vector1, vector2):
    cosine_sim = cosine_similarity(vector1, vector2)
    cosine_dist = 1 - cosine_sim
    return cosine_dist


def jaccard_distances(vector1, vector2):
    # Convierte los vectores en conjuntos
    set1 = set(vector1.toarray()[0])
    set2 = set(vector2.toarray()[0])
    
    # Calcula la distancia de Jaccard como 1 - coeficiente de Jaccard
    jaccard_dist = 1 - len(set1.intersection(set2)) / len(set1.union(set2))
    return jaccard_dist

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
