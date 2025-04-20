import tkinter as tk
from tkinter import ttk, messagebox

def calcular_distribucion():
    try:
        agua_total = float(entry_agua.get())
        hombres = int(entry_hombres.get())
        mujeres = int(entry_mujeres.get())
        ninos = int(entry_ninos.get())
        ancianos = int(entry_ancianos.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
        return

    consumo = {
        "hombre": 50,
        "mujer": 45,
        "niño": 30,
        "anciano": 40
    }

    demanda_total = (hombres * consumo["hombre"] +
                     mujeres * consumo["mujer"] +
                     ninos * consumo["niño"] +
                     ancianos * consumo["anciano"])

    resultado = f"Demanda total: {demanda_total:.2f} litros\n"

    if agua_total >= demanda_total:
        resultado += "\nEl agua es suficiente.\nDistribución por persona:\n"
        resultado += f"  Hombres: {consumo['hombre']} L\n"
        resultado += f"  Mujeres: {consumo['mujer']} L\n"
        resultado += f"  Niños: {consumo['niño']} L\n"
        resultado += f"  Ancianos: {consumo['anciano']} L\n"
    else:
        proporcion = agua_total / demanda_total
        resultado += f"\nEl agua no es suficiente.\nDistribución ajustada ({proporcion*100:.2f}%):\n"
        resultado += f"  Hombres: {consumo['hombre'] * proporcion:.2f} L\n"
        resultado += f"  Mujeres: {consumo['mujer'] * proporcion:.2f} L\n"
        resultado += f"  Niños: {consumo['niño'] * proporcion:.2f} L\n"
        resultado += f"  Ancianos: {consumo['anciano'] * proporcion:.2f} L\n"

    text_resultado.config(state="normal")
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)
    text_resultado.config(state="disabled")

# --- INTERFAZ GRÁFICA MEJORADA ---
root = tk.Tk()
root.title("Sistema Inteligente de Distribución de Agua")
root.configure(bg="#e6f2ff")

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11), background="#e6f2ff")
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TEntry", padding=4)

# Título
titulo = ttk.Label(root, text="Gestión Inteligente de Agua", font=("Segoe UI", 16, "bold"), background="#e6f2ff", foreground="#004080")
titulo.pack(pady=(10, 5))

# Sección informativa de consumos promedio
info_frame = ttk.Frame(root, padding=10)
info_frame.pack()

info_text = (
    "Promedio de consumo diario por persona:\n"
    "  • Hombre:   50 litros\n"
    "  • Mujer:    45 litros\n"
    "  • Niño:     30 litros\n"
    "  • Anciano:  40 litros"
)
label_info = ttk.Label(info_frame, text=info_text, justify="left", font=("Segoe UI", 10), foreground="#003366")
label_info.pack()

# Marco de entrada
frame_entrada = ttk.Frame(root, padding=15)
frame_entrada.pack()

def agregar_entrada(etiqueta, fila):
    lbl = ttk.Label(frame_entrada, text=etiqueta)
    lbl.grid(row=fila, column=0, sticky="e", padx=5, pady=5)
    entrada = ttk.Entry(frame_entrada, width=20)
    entrada.grid(row=fila, column=1, padx=5, pady=5)
    return entrada

entry_agua = agregar_entrada("Litros de agua disponibles:", 0)
entry_hombres = agregar_entrada("Número de hombres:", 1)
entry_mujeres = agregar_entrada("Número de mujeres:", 2)
entry_ninos = agregar_entrada("Número de niños:", 3)
entry_ancianos = agregar_entrada("Número de ancianos:", 4)

# Botón
btn_calcular = ttk.Button(root, text="Calcular distribución", command=calcular_distribucion)
btn_calcular.pack(pady=10)

# Marco de resultados
frame_resultado = ttk.Frame(root, padding=10)
frame_resultado.pack()

text_resultado = tk.Text(frame_resultado, height=10, width=60, state="disabled", bg="#f2f9ff", font=("Consolas", 10))
text_resultado.pack()

root.mainloop()
