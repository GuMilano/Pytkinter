import tkinter as tk
from tkinter import messagebox

# Função para calcular a soma
def calcular_soma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x200")

# Criando os widgets
label_titulo = tk.Label(janela, text="Calculadora Simples", font=("Arial", 14, "bold"))
label_titulo.pack(pady=10)

frame_entradas = tk.Frame(janela)
frame_entradas.pack()

label_num1 = tk.Label(frame_entradas, text="Número 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_entradas)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(frame_entradas, text="Número 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_entradas)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

btn_calcular = tk.Button(janela, text="Calcular Soma", command=calcular_soma)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

# Executar a interface
janela.mainloop()
