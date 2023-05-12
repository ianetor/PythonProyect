import PySimpleGUI as sg

# Crear botones
boton1 = sg.Button('Botón 1', key='-BUTTONS-')
boton2 = sg.Button('Botón 2')

# Crear el layout con el botón 1
layout = [[boton1]]

# Crear la ventana
window = sg.Window('Ejemplo de reemplazo de botones', layout)

# Loop principal
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Botón 1':
        # Reemplazar el botón 1 con el botón 2
        window['-BUTTONS-'].update([[boton2]])

# Cerrar la ventana y salir
window.close()


