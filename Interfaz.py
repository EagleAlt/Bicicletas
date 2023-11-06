from tkinter import *
from datetime import datetime
import tkinter.font as font      # This lets us use different fonts.
import funciones

INTERVALO_REFRESCO_RELOJ = 300  # En milisegundos


def obtener_hora_actual():
    return datetime.now().strftime('Fecha: %d-%m-%Y\n Hora: %H:%M:%S')


def refrescar_reloj():
    global solicitud, fila, estado
    variable_hora_actual.set(obtener_hora_actual())
    ventana.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)
    if solicitud == 1:
        fila, u, estado = funciones.buscar_datos(funciones.buscar_qr())
        usuario.set(u)
        print(fila)
        print(usuario)
        print(estado)
        marco_inicio.forget()
        marco_qr.forget()
        marco_rfid.forget()
        marco_guardar.pack(fill='both', expand=1)
    elif solicitud == 2:
        print('rfid')

    solicitud = 0


def centrar_pantalla():
    """
    This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below.
    :return: Nothing
    """
    x_cord = int((ancho_pantalla / 2) - (width / 2))
    y_cord = int((alto_pantalla / 2) - (height / 2))
    ventana.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def cambiar_a_qr():
    """
    This function swaps from the quiz
    frame to the work frame.
    :return: Nothing
    """
    marco_inicio.forget()
    marco_rfid.forget()
    marco_guardar.forget()
    marco_qr.pack(fill='both', expand=1)
    global solicitud
    solicitud = 1


def cambiar_a_rfid():
    """
    This function swaps from the work
    frame to the quiz frame.
    :return: Nothing
    """
    marco_inicio.forget()
    marco_qr.forget()
    marco_guardar.forget()
    marco_rfid.pack(fill='both', expand=1)
    global solicitud
    solicitud = 2


def cambiar_a_inicio():
    """
    This function swaps from the work
    frame to the quiz frame.
    :return: Nothing
    """
    marco_inicio.pack(fill='both', expand=1)
    marco_qr.forget()
    marco_rfid.forget()
    marco_guardar.forget()


# -------------------------------------------------------------------------------------------------
# -------------------------------------------Configuración de ventana----------------------------------------
# -------------------------------------------------------------------------------------------------
ventana = Tk()
ventana.title("Sistema de Almacenamiento para Bicicletas")
ventana.resizable(False, False)
ventana.configure(bg="#545154", padx=10, pady=10)  # "#0f0e0f"
ventana.iconphoto(True, PhotoImage(file='icon.png'))

width, height = 700, 500
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
centrar_pantalla()

variable_hora_actual = StringVar(ventana, value=obtener_hora_actual())
solicitud = 0
fila = 0
usuario = StringVar(ventana, value="")
estado = 0

# -------------------------------------------------------------------------------------------------
# -------------------------------------------Configuración frames----------------------------------------
# -------------------------------------------------------------------------------------------------
marco_inicio = Frame(ventana)
marco_inicio.config(bg="#332f33", padx=5, pady=5)
marco_qr = Frame(ventana)
marco_qr.config(bg="#332f33", padx=5, pady=5)
marco_rfid = Frame(ventana)
marco_rfid.config(bg="#332f33", padx=5, pady=5)
marco_admi = Frame(ventana)
marco_admi.config(bg="#332f33", padx=5, pady=5)
marco_guardar = Frame(ventana)
marco_guardar.config(bg="#332f33", padx=5, pady=5)

# Fuentes para texto.
texto_grande = font.Font(family='Arial', size=26, weight='bold')
texto_mediano = font.Font(family='Arial', size=14)
texto_pequeno = font.Font(family='Georgia', size=10)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------Cuadro inicio----------------------------------------
# -------------------------------------------------------------------------------------------------

# Mensajes inicio.
label_fecha = Label(marco_inicio, textvariable=variable_hora_actual,
                    font=texto_pequeno, bg="#332f33", fg="white")

label_lugares = Label(marco_inicio, text='Lugares\ndisponibles: 6',
                      font=texto_pequeno, bg="#332f33", fg="white")

label_bienvenida = Label(marco_inicio, text='Bienvenido\nSeleccione su método de identificación\npara continuar:',
                         width=30, height=3,
                         font=texto_grande, bg="#332f33", fg="white")

# Botones inicio.
boton_qr = Button(marco_inicio, text='Código QR',
                  font=texto_mediano, bg="#486bf7", fg="white",
                  width=10, height=3, command=cambiar_a_qr)

boton_rfid = Button(marco_inicio, text='Tarjeta',
                    font=texto_mediano, bg="#486bf7", fg="white",
                    width=10, height=3, command=cambiar_a_rfid)

boton_administrador = Button(marco_inicio, text='Administrador',
                             font=texto_pequeno, bg="#486bf7", fg="white",
                             width=10, height=3, command=cambiar_a_rfid)

# Posiciones inicio
label_fecha.grid(row=0, column=0, padx=10, pady=10)
label_lugares.grid(row=0, column=2, padx=10, pady=10)
label_bienvenida.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
boton_qr.grid(row=3, column=0, padx=10, pady=10)
boton_rfid.grid(row=3, column=2, padx=10, pady=10)
boton_administrador.grid(row=4, column=1, padx=10, pady=10)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------Cuadro QR----------------------------------------
# -------------------------------------------------------------------------------------------------

img_flecha_qr = PhotoImage(file='flecha-hacia-abajo.png')
label_flecha_qr = Label(marco_qr, image=img_flecha_qr, bg="#332f33")
# Mensajes.
label_fecha_qr = Label(marco_qr, textvariable=variable_hora_actual,
                       font=texto_pequeno, bg="#332f33", fg="white")

label_lugares_qr = Label(marco_qr, text='Lugares\ndisponibles: 6',
                         font=texto_pequeno, bg="#332f33", fg="white")

label_QR = Label(marco_qr, text='Coloque el QR de su credencial\nsobre el lector',
                 width=30, height=3,
                 font=texto_grande, bg="#332f33", fg="white")

# Botones
btn_cancelar_qr = Button(marco_qr, text='Cancelar',
                         font=texto_pequeno, bg="#486bf7", fg="white",
                         width=10, height=3, command=cambiar_a_inicio)

# Posiciones
label_fecha_qr.grid(row=0, column=0, padx=10, pady=10)
label_lugares_qr.grid(row=0, column=2, padx=10, pady=10)
label_QR.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
btn_cancelar_qr.grid(row=4, column=1, padx=10, pady=10)
label_flecha_qr.grid(row=5, column=0, padx=10, pady=10)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------Cuadro RFID----------------------------------------
# -------------------------------------------------------------------------------------------------

img_flecha_rfid = PhotoImage(file='flecha-hacia-abajo.png')
label_flecha_rfid = Label(marco_rfid, image=img_flecha_qr, bg="#332f33")
# Mensajes.
label_fecha_rfid = Label(marco_rfid, textvariable=variable_hora_actual,
                         font=texto_pequeno, bg="#332f33", fg="white")

label_lugares_rfid = Label(marco_rfid, text='Lugares\ndisponibles: 6',
                           font=texto_pequeno, bg="#332f33", fg="white")

label_rfid = Label(marco_rfid, text='Coloque su tarjeta sobre el lector',
                   width=30, height=3,
                   font=texto_grande, bg="#332f33", fg="white")

# Botones
btn_cancelar_rfid = Button(marco_rfid, text='Cancelar',
                           font=texto_pequeno, bg="#486bf7", fg="white",
                           width=10, height=3, command=cambiar_a_inicio)

# Posiciones
label_fecha_rfid.grid(row=0, column=0, padx=10, pady=10)
label_lugares_rfid.grid(row=0, column=2, padx=10, pady=10)
label_rfid.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
btn_cancelar_rfid.grid(row=4, column=1, padx=10, pady=10)
label_flecha_rfid.grid(row=5, column=2, padx=10, pady=10)

# -------------------------------------------------------------------------------------------------
# -------------------------------------------Cuadro Guardar----------------------------------------
# -------------------------------------------------------------------------------------------------

# Mensajes.
label_guardar = Label(marco_guardar, text='Datos de Acceso',
                      font=texto_grande, bg="#332f33", fg="white")

label_nombre = Label(marco_guardar, text=f'Nombre:',
                     font=texto_mediano, bg="#332f33", fg="white")

label_usuario = Label(marco_guardar, textvariable=usuario,
                      font=texto_mediano, bg="#332f33", fg="white")

# Botones
btn_salir = Button(marco_guardar, text='Cancelar',
                   font=texto_pequeno, bg="#486bf7", fg="white",
                   width=10, height=3, command=cambiar_a_inicio)

# Posiciones
label_guardar.pack()
label_nombre.pack()
label_usuario.pack()
btn_salir.pack()

# -------------------------------------------------------------------------------------------------
# Only the quiz frame needs to be shown
# when the program starts.  The work frame
# will only appear when the Change button
# is clicked.
marco_inicio.pack(fill='both', expand=1)
refrescar_reloj()
ventana.mainloop()
