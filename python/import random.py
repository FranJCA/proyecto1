import random

# Definimos una lista vacía para almacenar los resultados de los lanzamientos
resultados = []
contar =0
impar =0

# Simulamos el lanzamiento de la moneda 60 veces
for i in range(100):
    # Generamos un número aleatorio entre 0 y 1, donde 0 representa "cara" y 1 representa "cruz"
    lanzamiento = random.randint(0, 1)
    if lanzamiento==1 :
        contar=contar +1
    else:
        impar=impar+1
    # Almacenamos el resultado del lanzamiento en la lista "resultados"
    resultados.append(lanzamiento)
    
# Imprimimos los resultados
print("Resultados de los lanzamientos: ", resultados)
print( contar , "cara" ," sello " , impar)