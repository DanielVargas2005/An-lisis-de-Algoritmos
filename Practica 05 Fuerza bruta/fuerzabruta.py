import math
import random
import tkinter as tk 
from tkinter import ttk, messagebox

VAL_MIN = 0
VAL_MAX = 40
N = 10

p1 = [1,2]
p2 = [3,4]
puntos = []

def generar_datos():
    global puntos
    datos = [random.randint(VAL_MIN, VAL_MAX) for _ in range(N)]
    for i in range(0, len(datos), 2):
        par = [datos[i], datos[i+1]]
        puntos.append(par)

def distancia(punto_1,punto_2):
    return math.sqrt(((punto_2[0]-punto_1[0])**2) + ((punto_2[1]-punto_1[1])**2))

def puntos_cercanos():


root = tk.Tk()
root.title("Dos puntos más cercanos")


root.mainloop()