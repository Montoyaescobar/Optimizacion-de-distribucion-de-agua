import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------- OBJETIVOS Y REQUERIMIENTOS ------------------------

OBJETIVO = "Distribuir el agua de forma racional según el promedio de consumo de personas para evitar escasez."
REQUERIMIENTO = "El usuario debe ingresar los litros disponibles y el número de personas por tipo."

# ------------------------- CONSUMO PROMEDIO -------------------------------

# Lista con el tipo de personas
tipos_persona = ["Hombre", "Mujer", "Niño", "Anciano"]

# Lista con el consumo promedio (en litros por día) [Hombre, Mujer, Niño, Anciano]
consumo_promedio = [50, 45, 30, 40]

# ------------------------- FUNCIONES DEL PROGRAMA -------------------------

def crear_interfaz():
    root = tk.Tk()
    root.title("Distribución Inteligente del Agua")
    root.configure(bg="#e7f0fa")

    crear_encabezado(root)
    mostrar_info_consumo(root)
    entradas = crear_formulario(root)
    crear_boton_calculo(root, entradas)
    area_resultado = crear_area_resultado(root)

    root.mainloop()

def crear_encabezado(root):
    ttk.Label(root, text="Sistema de Distribución de Agua", font=("Segoe UI", 18, "bold"),
              background="#e7f0fa", foreground="#003366").pack(pady=10)
    ttk.Label(root, text=f"Objetivo: {OBJETIVO}", background="#e7f0fa", font=("Segoe UI", 10)).pack()
    ttk.Label(root, text=f"Requerimiento: {REQUERIMIENTO}", background="#e7f0fa", font=("Segoe UI", 10)).pack()

def mostrar_info_consumo(root):
    frame = ttk.Frame(root, padding=10)
    frame.pack()
    ttk.Label(frame, text="Promedio de consumo diario por persona:", font=("Segoe UI", 11, "underline")).pack(anchor="w")
    for tipo, consumo in zip(tipos_persona, consumo_promedio):
        ttk.Label(frame, text=f"  • {tipo}: {consumo} L", font=("Segoe UI", 10)).pack(anchor="w")

def crear_formulario(root):
    frame = ttk.Frame(root, padding=10)
    frame.pack()
    etiquetas = ["Litros de agua disponibles:"] + [f"Número de {tipo.lower()}s:" for tipo in tipos_persona]
    entradas = []

    for i, etiqueta in enumerate(etiquetas):
        ttk.Label(frame, text=etiqueta).grid(row=i, column=0, sticky="e", padx=5, pady=4)
        entrada = ttk.Entry(frame, width=20)
        entrada.grid(row=i, column=1, padx=5, pady=4)
        entradas.append(entrada)

    return entradas

def crear_boton_calculo(root, entradas):
    ttk.Button(root, text="Calcular distribución", command=lambda: calcular_distribucion(entradas)).pack(pady=10)

def crear_area_resultado(root):
    global resultado_text
    frame = ttk.Frame(root, padding=10)
    frame.pack()
    resultado_text = tk.Text(frame, height=12, width=70, state="disabled", bg="#f4f9ff", font=("Consolas", 10))
    resultado_text.pack()
    return resultado_text

def leer_datos(entradas):
    try:
        litros = float(entradas[0].get())
        personas = [int(entrada.get()) for entrada in entradas[1:]]
        return litros, personas
    except ValueError:
        messagebox.showerror("Error", "Introduce valores válidos en todos los campos.")
        return None, None

def construir_matriz_consumo(personas):
    matriz = []
    for i in range(len(personas)):
        fila = [personas[i], consumo_promedio[i], personas[i] * consumo_promedio[i]]
        matriz.append(fila)
    return matriz

def calcular_total(matriz):
    total = 0
    for fila in matriz:
        total += fila[2]
    return total

def ajustar_distribucion(matriz, litros_disponibles, total_necesario):
    proporcion = litros_disponibles / total_necesario
    distribucion = []
    for fila in matriz:
        litros_por_persona = fila[1] * proporcion
        distribucion.append(round(litros_por_persona, 2))
    return distribucion, proporcion

def mostrar_resultados(matriz, litros_disponibles, total_necesario, distribucion=None):
    resultado_text.config(state="normal")
    resultado_text.delete("1.0", tk.END)

    resultado_text.insert(tk.END, f"Total de litros disponibles: {litros_disponibles} L\n")
    resultado_text.insert(tk.END, f"Demanda total calculada: {total_necesario} L\n\n")

    for i, fila in enumerate(matriz):
        nombre = tipos_persona[i]
        if distribucion:
            resultado_text.insert(tk.END, f"{nombre:<8}: {fila[0]} personas x {distribucion[i]} L = {fila[0]*distribucion[i]:.2f} L\n")
        else:
            resultado_text.insert(tk.END, f"{nombre:<8}: {fila[0]} personas x {fila[1]} L = {fila[2]:.2f} L\n")

    if distribucion:
        resultado_text.insert(tk.END, "\nDistribución ajustada debido a escasez de agua.")
    else:
        resultado_text.insert(tk.END, "\nEl agua es suficiente. Distribución estándar aplicada.")

    resultado_text.config(state="disabled")

def calcular_distribucion(entradas):
    litros, personas = leer_datos(entradas)
    if litros is None or personas is None:
        return

    matriz = construir_matriz_consumo(personas)
    total_necesario = calcular_total(matriz)

    if litros >= total_necesario:
        mostrar_resultados(matriz, litros, total_necesario)
    else:
        distribucion_ajustada, proporcion = ajustar_distribucion(matriz, litros, total_necesario)
        mostrar_resultados(matriz, litros, total_necesario, distribucion_ajustada)

# ----------------------------- INICIO DEL PROGRAMA ---------------------------

crear_interfaz()
