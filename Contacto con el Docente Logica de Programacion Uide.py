import tkinter as tk
import random

# Configuración general

ANCHO     = 450
ALTO      = 450
CELDA     = 15
VELOCIDAD = 190

# Variables de estado del juego

serpiente    = []
direccion    = [0, 1]
comida       = []
puntaje      = 0
juego_activo = False

# INICIALIZAR JUEGO

def inicializar_juego():
    global serpiente, direccion, comida, puntaje, juego_activo

    # Inicializar Variables
    serpiente    = [[10, 10], [10, 9], [10, 8]]
    direccion    = [0, 1]
    puntaje      = 0
    juego_activo = True

    # Generar Comida Aleatoria

    generar_comida()
    label_puntaje.config(text="Puntaje: 0")

def generar_comida():
    """Genera comida en posición aleatoria libre"""
    global comida
    filas = ALTO // CELDA
    cols  = ANCHO // CELDA
    while True:
        f = random.randint(0, filas - 1)
        c = random.randint(0, cols  - 1)
        if [f, c] not in serpiente:
            comida = [f, c]
            break

# CAPTURAR ENTRADA DEL TECLADO

def cambiar_direccion(event):
    """Actualizar Dirección de la Serpiente"""
    global direccion
    if not juego_activo:
        return
    teclas = {
        "Up":    [-1,  0],
        "Down":  [ 1,  0],
        "Left":  [ 0, -1],
        "Right": [ 0,  1],
    }
    nueva = teclas.get(event.keysym)

    # Evitar dirección opuesta (no puede ir hacia atrás)

    if nueva and (direccion[0] + nueva[0] != 0 or direccion[1] + nueva[1] != 0):
        direccion = nueva

def pausar(event=None):
    """Pausar / reanudar el juego"""
    global juego_activo
    if juego_activo:
        juego_activo = False
        canvas.create_text(ANCHO // 2, ALTO // 2,
                           text="PAUSADO  (P para continuar)",
                           fill="yellow", font=("Arial", 14, "bold"),
                           tags="pausa")
    else:
        juego_activo = True
        canvas.delete("pausa")
        gameloop()

# GAMELOOP PRINCIPAL

def gameloop():
    global puntaje, juego_activo

    # ¿Juego Activo?
    if not juego_activo:
        return

    # Mover Serpiente: calcular nueva cabeza

    nueva_cabeza = [
        serpiente[0][0] + direccion[0],
        serpiente[0][1] + direccion[1],
    ]
    serpiente.insert(0, nueva_cabeza)

    # ¿Colisión con Paredes o Consigo Misma?
    fila, col = nueva_cabeza
    filas = ALTO // CELDA
    cols  = ANCHO // CELDA
    if (fila < 0 or fila >= filas or
        col  < 0 or col  >= cols  or
        nueva_cabeza in serpiente[1:]):
        # Mostrar Game Over
        juego_activo = False
        mostrar_game_over()
        return

    # ¿Comió Comida?

    if nueva_cabeza == comida:

        # Sí → Aumentar Longitud
        # Aumentar Puntaje

        puntaje += 1
        label_puntaje.config(text=f"Puntaje: {puntaje}")
        # Generar Nueva Comida
        generar_comida()

        # Actualizar Velocidad

        actualizar_velocidad()
    else:
        serpiente.pop()

    renderizar()

    # Controlar Velocidad / Delay

    ventana.after(velocidad_actual, gameloop)

def actualizar_velocidad():
    """Aumenta la velocidad cada 4 puntos"""
    global velocidad_actual
    velocidad_actual = max(80, VELOCIDAD - (puntaje // 4) * 20)

# RENDERIZAR EN PANTALLA

def renderizar():
    canvas.delete("all")

    # Dibujar cuadrícula de fondo

    for i in range(0, ANCHO, CELDA):
        canvas.create_line(i, 0, i, ALTO, fill="#16213e")
    for j in range(0, ALTO, CELDA):
        canvas.create_line(0, j, ANCHO, j, fill="#16213e")

    # Dibujar Comida

    x = comida[1] * CELDA
    y = comida[0] * CELDA
    canvas.create_oval(x+3, y+3, x+CELDA-3, y+CELDA-3,
                       fill="red", outline="darkred", width=1)

    # Dibujar Serpiente (cabeza en color distinto)

    for i, seg in enumerate(serpiente):
        x = seg[1] * CELDA
        y = seg[0] * CELDA
        color = "#00ffcc" if i == 0 else "#00aa66"
        canvas.create_rectangle(x+1, y+1, x+CELDA-1, y+CELDA-1,
                                 fill=color, outline="")

# MOSTRAR GAME OVER

def mostrar_game_over():
    renderizar()
    cx, cy = ANCHO // 2, ALTO // 2
    canvas.create_rectangle(cx-160, cy-50, cx+160, cy+50,
                             fill="#0f3460", outline="#00ffcc", width=2)
    canvas.create_text(cx, cy-18, text="GAME OVER",
                       fill="white", font=("Arial", 20, "bold"))
    canvas.create_text(cx, cy+15,
                       text=f"Puntaje: {puntaje}  |  Enter = reiniciar  |  Esc = salir",
                       fill="#aaaaaa", font=("Arial", 9))

def iniciar_o_reiniciar(event=None):
    """Iniciar juego nuevo o reiniciar después de game over"""
    global velocidad_actual
    velocidad_actual = VELOCIDAD
    inicializar_juego()
    gameloop()

def fin_del_juego(event=None):
    """Fin del Juego: cerrar ventana"""
    ventana.destroy()

# CONFIGURAR VENTANA TKINTER

ventana = tk.Tk()
ventana.title("Juego de la Serpiente")
ventana.resizable(False, False)
ventana.configure(bg="#0f3460")

# Encabezado
frame_top = tk.Frame(ventana, bg="#0f3460")
frame_top.pack(pady=5)
tk.Label(frame_top, text="Contacto con el Docente UIDE Juan Gomez", font=("Arial", 14, "bold"),
         fg="#00ffcc", bg="#0f3460").pack(side=tk.LEFT, padx=15)
label_puntaje = tk.Label(frame_top, text="Puntaje: 0",
                          font=("Arial", 13), fg="white", bg="#0f3460")
label_puntaje.pack(side=tk.RIGHT, padx=15)

# Canvas principal

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO,
                   bg="#1a1a2e", highlightthickness=2,
                   highlightbackground="#00ffcc")
canvas.pack(padx=10)

# Instrucciones

tk.Label(ventana,
         text="Enter: iniciar/reiniciar   P: pausar   Esc: salir",
         font=("Arial", 9), fg="gray", bg="#0f3360").pack(pady=5)

#Controles del teclado
ventana.bind("<Up>",     cambiar_direccion)
ventana.bind("<Down>",   cambiar_direccion)
ventana.bind("<Left>",   cambiar_direccion)
ventana.bind("<Right>",  cambiar_direccion)
ventana.bind("<Return>", iniciar_o_reiniciar)
ventana.bind("<p>",      pausar)
ventana.bind("<P>",      pausar)
ventana.bind("<Escape>", fin_del_juego)

# Variable de velocidad actual (puede cambiar durante el juego)
velocidad_actual = VELOCIDAD

# Mensaje de bienvenida
canvas.create_text(ANCHO // 2, ALTO // 2,
                   text="Presiona ENTER para iniciar",
                   fill="white", font=("Arial", 14))

ventana.mainloop()
