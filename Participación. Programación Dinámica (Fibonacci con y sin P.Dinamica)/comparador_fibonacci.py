import time
import sys
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

sys.setrecursionlimit(2000)

def fibonacci_simple(n):
    if n <= 1:
        return n
    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)

def fibonacci_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    return memo[n]


def wrapper_fib_simple(n):
    fibonacci_simple(n)

def wrapper_fib_dp(n):
    fibonacci_dp(n, {})

def graficar_complejidad_temporal(n_max):
    print(f"Calculando complejidad temporal para n = {n_max}...")
    x_values = range(1, n_max + 1)
    times_simple = []
    times_dp = []

    for i in x_values:
        start_time = time.perf_counter()
        fibonacci_simple(i)
        end_time = time.perf_counter()
        times_simple.append(end_time - start_time)

        start_time = time.perf_counter()
        fibonacci_dp(i, {})
        end_time = time.perf_counter()
        times_dp.append(end_time - start_time)
        
    plt.figure(figsize=(10, 6)) 
    plt.plot(x_values, times_simple, 'r-o', label='Fibonacci Simple (Exponencial)')
    plt.plot(x_values, times_dp, 'g-^', label='Fibonacci con PD (Lineal)')
    plt.title(f"Complejidad Temporal (Tiempo de Ejecución)", fontsize=16)
    plt.xlabel("Valor de N")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    print("Gráfica de tiempo generada.")

def graficar_complejidad_espacial(n_max):
    print(f"Calculando complejidad espacial para n = {n_max}...")
    x_values = range(1, n_max + 1)
    space_simple = []
    space_dp = []

    for i in x_values:
        mem_simple = memory_usage((wrapper_fib_simple, (i,)), interval=0.001, max_usage=True)
        space_simple.append(mem_simple)

        mem_dp = memory_usage((wrapper_fib_dp, (i,)), interval=0.001, max_usage=True)
        space_dp.append(mem_dp)
        
    plt.figure(figsize=(10, 6)) 
    plt.plot(x_values, space_simple, 'b-s', label='Fibonacci Simple (Recursión)')
    plt.plot(x_values, space_dp, 'm-x', label='Fibonacci con PD (Memoización)')
    plt.title(f"Complejidad Espacial (Uso de Memoria)", fontsize=16)
    plt.xlabel("Valor de N")
    plt.ylabel("Uso de Memoria (MiB)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    print("Gráfica de memoria generada.")

if __name__ == "__main__":
    #N para la gráfica de complejidad temporal
    N_PARA_GRAFICA_TIEMPO = 10
    #N para la gráfica de complejidad espacial
    N_PARA_GRAFICA_ESPACIO = 10
    
    graficar_complejidad_temporal(N_PARA_GRAFICA_TIEMPO)
    graficar_complejidad_espacial(N_PARA_GRAFICA_ESPACIO)
    print("\nMostrando gráficas...")
    plt.show()