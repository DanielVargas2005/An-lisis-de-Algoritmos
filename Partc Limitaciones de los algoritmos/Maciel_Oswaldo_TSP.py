# Maciel Vargas Oswaldo Daniel
# Problema del Viajero (Travelling Salesman Problem)
import numpy as np
import itertools

def resolver_tsp_numpy(distancias, ciudades):
    n = len(ciudades)
    indices = np.arange(n)
    punto_partida = indices[0]
    ciudades_a_permutar = indices[1:]
    
    mejor_ruta = None
    minima_distancia = np.inf 
    
    print("--- Evaluando todas las rutas ---")
    
    # Usamos Fuerza bruta para generar y probar todas las combinaciones posibles de rutas.
    for permutacion in itertools.permutations(ciudades_a_permutar):
        ruta_indices = [punto_partida] + list(permutacion) + [punto_partida]
        distancia_actual = 0
        
        # Para calcular las distancias recorremos la ruta sumando las distancias 
        # de la matriz para cada par consecutivo (origen -> destino).
        for i in range(len(ruta_indices) - 1):
            origen = ruta_indices[i]
            destino = ruta_indices[i+1]
            distancia_actual += distancias[origen, destino]
            
        nombres_ruta = [ciudades[i] for i in ruta_indices]
        print(f"Ruta: {nombres_ruta} -> Costo: {distancia_actual}")
        
        if distancia_actual < minima_distancia:
            minima_distancia = distancia_actual
            mejor_ruta = ruta_indices

    return mejor_ruta, minima_distancia

# El conjunto de ciudades se representa con letras y una matriz de distancias
nombres_ciudades = ["A", "B", "C", "D", "E"]

matriz_distancias = np.array([
    [0,  10, 15, 20, 25], 
    [10, 0,  35, 25, 15], 
    [15, 35, 0,  30, 20], 
    [20, 25, 30, 0,  10],
    [25, 15, 20, 10, 0]
])

# --- EJECUCIÓN ---
ruta_indices, costo_total = resolver_tsp_numpy(matriz_distancias, nombres_ciudades)

print("\n" + "="*30)
print("RESULTADO FINAL")
print("="*30)

ruta_nombres = [nombres_ciudades[i] for i in ruta_indices]
print(f"Mejor ruta encontrada: {' -> '.join(ruta_nombres)}")
print(f"Distancia total: {costo_total}")