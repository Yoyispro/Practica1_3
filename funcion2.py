#Columna a vectorizar
columna_genero = df['Genres']

# Crear un vocabulario compartido entre todas las entradas de la columna
vocabulario = set()
for texto in columna_genero:
    palabras = texto.split()
    vocabulario.update(palabras)

# Convierte el vocabulario en una lista y ordénala
vocabulario = list(vocabulario)
vocabulario.sort()

#Función para crear vectores de bolsa de palabras para cada cadena de texto
def text_to_bow(texto, vocabulario):
    vector = np.zeros(len(vocabulario), dtype=int)
    palabras = texto.split()
    for palabra in palabras:
        if palabra in vocabulario:
            vector[vocabulario.index(palabra)] += 1
    return vector

# Aplica la función a cada fila de la columna y crea una nueva columna con los vectores
df['Vector_Bolsa'] = columna_genero.apply(lambda x: text_to_bow(x, vocabulario))
vectores_bolsa = df['Vector_Bolsa']