import configuracion
import PySimpleGUI as sg
import menu_principal_ventana
import inicio_ventana
import generador_memes

ventana_principal = inicio_ventana.VentanaPrincipal()
ventana_principal.iniciar_ventana()

ventana_principal2 = inicio_ventana.VentanaPrincipal(2)
ventana_principal2.iniciar_ventana()

menu_ventana = menu_principal_ventana.VentanaMenu(2)
menu_ventana.iniciar_ventana()


window = sg.Window("UNLP Image", background_color='white', size=(800,600))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

