import tkinter as tk 
from tkinter import ttk, messagebox
import time
import algorithms
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data_list = []
lineal_times = [0, 0, 0, 0]
binary_times = [0, 0, 0, 0]
num_data = 0

def add_data():
    global num_data, data_list
    num_data = int(combo.get())
    data_list = algorithms.generate_data(num_data)

    listbox.delete(0, tk.END)
    for num in data_list:
        listbox.insert(tk.END, num)

    lbl_resultado.config(text=f"Lista generada con {num_data} datos")

    btn_lineal_search.config(state="normal")
    btn_binary_search.config(state="normal")

def validar_entrada():
    """Valida que la entrada no esté vacía y sea un número entero."""
    value = search_value.get().strip()
    if not value:
        messagebox.showwarning("Entrada inválida", "⚠️ Debes ingresar un número entero.")
        return None
    if not value.isdigit():
        messagebox.showwarning("Entrada inválida", "⚠️ Solo se permiten números enteros.")
        return None
    return int(value)

def btn_click_lineal():
    global num_data, data_list

    x = validar_entrada()
    if x is None:
        return  

    listbox.delete(0, tk.END)
    for num in data_list:
        listbox.insert(tk.END, num)

    start_time = time.perf_counter()
    idx = algorithms.linear_search(data_list, x)
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000  

    if num_data == 100:
        lineal_times[0] = (total_time + lineal_times[0]) / 2
    elif num_data == 1000:
        lineal_times[1] = (total_time + lineal_times[1]) / 2
    elif num_data == 10000:
        lineal_times[2] = (total_time + lineal_times[2]) / 2
    elif num_data == 100000:
        lineal_times[3] = (total_time + lineal_times[3]) / 2

    lbl_size.config(text=f"Tamaño de lista: {num_data}")
    lbl_found.config(text=f"Encontrado: {'Sí (índice ' + str(idx) + ')' if idx != -1 else 'No'}")
    lbl_time.config(text=f"Tiempo ejecución: {total_time:.4f} ms")

    plot_array()

def btn_click_binary():
    global num_data

    x = validar_entrada()
    if x is None:
        return  

    data_list_sorted = sorted(data_list)
    listbox.delete(0, tk.END)
    for num in data_list_sorted:
        listbox.insert(tk.END, num)

    start_time = time.perf_counter()
    idx = algorithms.binary_search(data_list_sorted, x)
    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000  

    if num_data == 100:
        binary_times[0] = (total_time + binary_times[0]) / 2
    elif num_data == 1000:
        binary_times[1] = (total_time + binary_times[1]) / 2
    elif num_data == 10000:
        binary_times[2] = (total_time + binary_times[2]) / 2
    elif num_data == 100000:
        binary_times[3] = (total_time + binary_times[3]) / 2

    lbl_size.config(text=f"Tamaño de lista: {num_data}")
    lbl_found.config(text=f"Encontrado: {'Sí (índice ' + str(idx) + ')' if idx != -1 else 'No'}")
    lbl_time.config(text=f"Tiempo ejecución: {total_time:.4f} ms")

    plot_array()

def plot_array():
    for widget in frame_plot.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(options_data, lineal_times, color="red", label="Búsqueda Lineal")
    ax.plot(options_data, binary_times, color="blue", label="Búsqueda Binaria")

    ax.set_xlabel("Tamaño Lista")
    ax.set_ylabel("Tiempo (ms)")
    ax.set_xscale("log")  
    ax.set_xticks(options_data)
    ax.get_xaxis().set_major_formatter(__import__("matplotlib").ticker.ScalarFormatter())  
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

root = tk.Tk()
root.title("Búsqueda lineal y búsqueda binaria")
root.geometry("1080x720")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

lbl = tk.Label(frame_top, text="Selecciona la cantidad de datos a generar:")
lbl.pack(side=tk.LEFT, padx=5)

options_data = [100, 1000, 10000, 100000]
combo = ttk.Combobox(frame_top, values=options_data, width=10)
combo.current(0)
combo.pack(side=tk.LEFT, padx=5)

btn = tk.Button(frame_top, text="Generar datos", command=add_data)
btn.pack(side=tk.LEFT, padx=5)

lbl_resultado = tk.Label(frame_top, text="")
lbl_resultado.pack(side=tk.LEFT, padx=10)

frame_main = tk.Frame(root)
frame_main.pack(fill="both", expand=True, padx=10, pady=10)

frame_list = tk.Frame(frame_main)
frame_list.pack(side=tk.LEFT, fill="y")

scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, width=30, height=20)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame_plot = tk.Frame(frame_main, bg="white", relief="sunken", bd=2)
frame_plot.pack(side=tk.LEFT, fill="both", expand=True, padx=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

lbl_search = tk.Label(frame_bottom, text="Ingresa el valor a buscar:")
lbl_search.pack(side=tk.LEFT, padx=5)

search_value = tk.Entry(frame_bottom, width=10)
search_value.pack(side=tk.LEFT, padx=5)

btn_lineal_search = tk.Button(frame_bottom, text="Búsqueda lineal", command=btn_click_lineal, state="disabled")  # ⛔ Disabled al inicio
btn_lineal_search.pack(side=tk.LEFT, padx=5)

btn_binary_search = tk.Button(frame_bottom, text="Búsqueda binaria", command=btn_click_binary, state="disabled")  # ⛔ Disabled al inicio
btn_binary_search.pack(side=tk.LEFT, padx=5)

frame_results = tk.LabelFrame(root, text="Resultados", padx=10, pady=10)
frame_results.pack(fill="x", padx=10, pady=10)

lbl_size = tk.Label(frame_results, text="Tamaño de lista: ")
lbl_size.pack(anchor="w")
lbl_found = tk.Label(frame_results, text="Encontrado: ")
lbl_found.pack(anchor="w")
lbl_time = tk.Label(frame_results, text="Tiempo ejecución: ")
lbl_time.pack(anchor="w")

plot_array()

def run():
    root.mainloop()
