import math
import random
import tkinter as tk 
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

VAL_MIN = 0
VAL_MAX = 40
N = 10

puntos = []
mejor_par = ()
mejor_dist = float('inf')
entradas = []

def generar_puntos():
    global puntos
    puntos.clear()
    datos = [random.randint(VAL_MIN, VAL_MAX) for _ in range(N)]
    for i in range(0, len(datos), 2):
        par = [datos[i], datos[i+1]]
        puntos.append(par)
    actualizar_tabla()
    dibujar_puntos()
    entry_distancia.delete(0, tk.END)
    btn_limpiar.config(state="normal")

def distancia_puntos(punto_1,punto_2):
    return math.sqrt(((punto_2[0]-punto_1[0])**2) + ((punto_2[1]-punto_1[1])**2))

def puntos_cercanos():
    global mejor_dist, mejor_par
    mejor_par = (puntos[0], puntos[1])
    mejor_dist = distancia_puntos(puntos[0], puntos[1])
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            distancia = distancia_puntos(puntos[i], puntos[j])
            if distancia < mejor_dist:
                mejor_par = (puntos[i], puntos[j])
                mejor_dist = distancia

def actualizar_tabla():
    for i, (x, y) in enumerate(puntos):
        entradas[i][1].delete(0, tk.END)
        entradas[i][1].insert(0, str(int(x)) if x == int(x) else str(x))
        entradas[i][2].delete(0, tk.END)
        entradas[i][2].insert(0, str(int(y)) if y == int(y) else str(y))
        entradas[i][0].config(bg="#3c3c3c", fg="white")
        entradas[i][1].config(bg="white", fg="black")
        entradas[i][2].config(bg="white", fg="black")

def dibujar_puntos():
    ax.clear()
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 40)
    ax.set_xticks(range(0, 41, 5))
    ax.set_yticks(range(0, 41, 5))
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")
    ax.set_facecolor("#3c3c3c")
    if puntos:
        xs = [p[0] for p in puntos]
        ys = [p[1] for p in puntos]
        ax.scatter(xs, ys, c="#4da6ff")
        for i, (x, y) in enumerate(puntos):
            ax.text(x+0.5, y+0.5, f"P{i+1}", color="white", fontsize=9)
    canvas.draw()

def generar():
    generar_puntos()

def calcular():
    global puntos
    puntos.clear()
    for ent in entradas:
        try:
            x = float(ent[1].get())
            y = float(ent[2].get())
            if not (0 <= x <= 40) or not (0 <= y <= 40):
                messagebox.showwarning("Valor inválido", "Por favor ingrese valores entre 0 y 40.")
                return
            puntos.append([x, y])
        except ValueError:
            messagebox.showwarning("Datos faltantes", "Por favor ingrese o genere valores antes de calcular.")
            return
    puntos_cercanos()
    actualizar_tabla()
    for i, (x, y) in enumerate(puntos):
        if [x, y] in mejor_par:
            entradas[i][0].config(bg="#2e7d32", fg="white")
            entradas[i][1].config(bg="#2e7d32", fg="white")
            entradas[i][2].config(bg="#2e7d32", fg="white")
    dibujar_puntos()
    x_vals = [mejor_par[0][0], mejor_par[1][0]]
    y_vals = [mejor_par[0][1], mejor_par[1][1]]
    ax.plot(x_vals, y_vals, c="#66bb6a", linewidth=2)
    canvas.draw()
    entry_distancia.delete(0, tk.END)
    entry_distancia.insert(0, f"{mejor_dist:.2f}")
    imprimir_resultados()

def imprimir_resultados():
    print("\nPuntos ingresados o generados:")
    for i, (x, y) in enumerate(puntos):
        print(f"P{i+1}: ({x}, {y})")
    print(f"\nLos dos puntos más cercanos son: {mejor_par[0]} y {mejor_par[1]}")
    print(f"Distancia : {mejor_dist:.2f}")

def limpiar():
    global puntos, mejor_par, mejor_dist
    puntos.clear()
    mejor_par = ()
    mejor_dist = float('inf')
    for i in range(len(entradas)):
        entradas[i][1].delete(0, tk.END)
        entradas[i][2].delete(0, tk.END)
        entradas[i][0].config(bg="#3c3c3c", fg="white")
        entradas[i][1].config(bg="white", fg="black")
        entradas[i][2].config(bg="white", fg="black")
    entry_distancia.delete(0, tk.END)
    ax.clear()
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 40)
    ax.set_xticks(range(0, 41, 5))
    ax.set_yticks(range(0, 41, 5))
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")
    ax.set_facecolor("#3c3c3c")
    canvas.draw()
    btn_limpiar.config(state="disabled")

root = tk.Tk()
root.title("Dos puntos más cercanos")
root.configure(bg="#2b2b2b")

frame_izq = tk.Frame(root, bg="#2b2b2b")
frame_izq.pack(side="left", fill="y", padx=10, pady=10)

frame_tabla = tk.LabelFrame(frame_izq, text=" Puntos ", bg="#2b2b2b", fg="white", padx=10, pady=10)
frame_tabla.pack(pady=10)

tk.Label(frame_tabla, text=" ", width=10, bg="#2b2b2b", fg="white").grid(row=0, column=0)
tk.Label(frame_tabla, text="X", width=5, bg="#2b2b2b", fg="white").grid(row=0, column=1)
tk.Label(frame_tabla, text="Y", width=5, bg="#2b2b2b", fg="white").grid(row=0, column=2)

entradas = []
for i in range(N//2):
    lbl = tk.Label(frame_tabla, text=f"Punto {i+1}", width=10, bg="#3c3c3c", fg="white")
    lbl.grid(row=i+1, column=0, padx=5, pady=2)
    ent_x = tk.Entry(frame_tabla, width=5, justify="center")
    ent_x.grid(row=i+1, column=1, padx=5, pady=2)
    ent_y = tk.Entry(frame_tabla, width=5, justify="center")
    ent_y.grid(row=i+1, column=2, padx=5, pady=2)
    entradas.append((lbl, ent_x, ent_y))

frame_botones = tk.LabelFrame(frame_izq, text=" Acciones ", bg="#2b2b2b", fg="white", padx=10, pady=10)
frame_botones.pack(fill="x", pady=10)

btn_generar = tk.Button(frame_botones, text="Generar Puntos Aleatorios", command=generar, bg="#4f4f4f", fg="white", relief="flat")
btn_generar.pack(fill="x", pady=4)
btn_calcular = tk.Button(frame_botones, text="Calcular", command=calcular, bg="#4f4f4f", fg="white", relief="flat", state="normal")
btn_calcular.pack(fill="x", pady=4)
btn_limpiar = tk.Button(frame_botones, text="Limpiar tabla y gráfica", command=limpiar, bg="#4f4f4f", fg="white", relief="flat", state="disabled")
btn_limpiar.pack(fill="x", pady=4)

frame_resultado = tk.LabelFrame(frame_izq, text=" Distancia ", bg="#2b2b2b", fg="white", padx=10, pady=10)
frame_resultado.pack(fill="x", pady=10)

entry_distancia = tk.Entry(frame_resultado, width=10, justify="center", font=("Arial", 12))
entry_distancia.pack()

frame_der = tk.LabelFrame(root, text=" Gráfica de puntos", bg="#2b2b2b", fg="white", padx=10, pady=10)
frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

fig, ax = plt.subplots(figsize=(5,5))
fig.patch.set_facecolor("#2b2b2b")
ax.set_facecolor("#3c3c3c")
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
ax.set_xticks(range(0, 41, 5))
ax.set_yticks(range(0, 41, 5))
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_color("white")

canvas = FigureCanvasTkAgg(fig, master=frame_der)
canvas.get_tk_widget().pack(fill="both", expand=True)

root.mainloop()

