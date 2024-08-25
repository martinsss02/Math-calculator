from tkinter import *
import tkinter as tk
from sympy import sympify, SympifyError


# Creacion ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(background="skyblue")
ventana.geometry("+500+80")
ventana.resizable(True, True)
valor_inicial = 0
display = tk.Entry(ventana, font="arial", bd=15, insertwidth=4, justify="right")
ventana.iconbitmap('calcu.ico')
display.grid(row=1, columnspan=4, sticky="NSEW")
display.focus()
error = False


def numeros_pantalla(valor):
    global valor_inicial
    display.insert(END, valor)
    valor_inicial = 0


def limpiar_pantalla():
    global valor_inicial
    display.delete(0, END)
    valor_inicial = 0


def borrar():
    display.delete(0, END)


def resultado():
    global valor_inicial
    ecuacion = display.get()
    try:
        expr = sympify(ecuacion)
        resultado = expr.evalf(n=2)
    except SympifyError:
        display.delete(0, END)
        display.insert(0, 'Error')
        valor_inicial = 0
        return
    resultado = round(float(resultado), 2)
    resultado = str(resultado).rstrip('0').rstrip('.')
    display.delete(0, END)
    display.insert(0, resultado)
    valor_inicial = 0


# Botones 0, Borrar y Porcentaje
tk.Button(ventana, text="0", command=lambda: numeros_pantalla(0)).grid(row=5, column=0, sticky="NSEW")
tk.Button(ventana, text="AC", command=lambda: borrar()).grid(row=5, column=1, sticky="NSEW")
tk.Button(ventana, text="%").grid(row=5, column=2, sticky="NSEW")
# Botones 1,2,3
tk.Button(ventana, text="1", command=lambda: numeros_pantalla(1)).grid(row=4, column=0, sticky="NSEW")
tk.Button(ventana, text="2", command=lambda: numeros_pantalla(2)).grid(row=4, column=1, sticky="NSEW")
tk.Button(ventana, text="3", command=lambda: numeros_pantalla(3)).grid(row=4, column=2, sticky="NSEW")
# Botones 4,5,6
tk.Button(ventana, text="4", command=lambda: numeros_pantalla(4)).grid(row=3, column=0, sticky="NSEW")
tk.Button(ventana, text="5", command=lambda: numeros_pantalla(5)).grid(row=3, column=1, sticky="NSEW")
tk.Button(ventana, text="6", command=lambda: numeros_pantalla(6)).grid(row=3, column=2, sticky="NSEW")
# Botones 7,8,9
tk.Button(ventana, text="7", command=lambda: numeros_pantalla(7)).grid(row=2, column=0, sticky="NSEW")
tk.Button(ventana, text="8", command=lambda: numeros_pantalla(8)).grid(row=2, column=1, sticky="NSEW")
tk.Button(ventana, text="9", command=lambda: numeros_pantalla(9)).grid(row=2, column=2, sticky="NSEW")
# Botones Operaciones
tk.Button(ventana, text="+", command=lambda: numeros_pantalla("+")).grid(row=2, column=3, sticky="NSEW")
tk.Button(ventana, text="-", command=lambda: numeros_pantalla("-")).grid(row=3, column=3, sticky="NSEW")
tk.Button(ventana, text="*", command=lambda: numeros_pantalla("*")).grid(row=4, column=3, sticky="NSEW")
tk.Button(ventana, text="/", command=lambda: numeros_pantalla("/")).grid(row=5, column=3, sticky="NSEW")
tk.Button(ventana, text="=", command=lambda: resultado()).grid(row=6, column=0, columnspan=4, sticky="NSEW")

ventana.mainloop()
