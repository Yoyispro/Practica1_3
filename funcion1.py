cadena_entrada = input()
# Tokenización y vectorización de la cadena de entrada
vocabulario = set()
palabras_entrada = cadena_entrada.split()
vocabulario.update(palabras_entrada)

# Vectorizar la cadena de entrada
vector_entrada = [palabras_entrada.count(palabra) for palabra in vocabulario]