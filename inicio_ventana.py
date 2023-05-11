import PySimpleGUI as sg
import json
import os
import menu_principal_ventana

class VentanaPrincipal:
    def __init__(self, indice_perfiles=0):
        current_dir = os.path.abspath(__file__)

        relative_path = "icons\\icon_add.png"
        relative_path_2 = "icons\\ver_mas.png"

        icon_add = os.path.join('./', relative_path)
        ver_mas = os.path.join('./', relative_path_2)

        with open('perfiles.json', 'r', encoding='utf-8') as archivo: 
            datos = json.load(archivo) #nos guardamos los perfiles del json

        agregar_perfil = sg.Button(enable_events=True, key='add', button_color='white', border_width=0, image_subsample=(4), image_filename=icon_add) #boton para añadir perfiles
        otros_perfiles = [sg.Button(enable_events=True, key='otros', button_color='white', border_width=0, size=(20,5), pad=(135,10), image_subsample=(3), image_filename=ver_mas)]

        perfiles = [agregar_perfil]

        if (indice_perfiles >= len(datos['perfiles'])):
            indice_perfiles = len(datos['perfiles'])-2

        for perfil in datos['perfiles'][indice_perfiles:]:
            perfil_boton = sg.Button(enable_events=True, key=perfil['nombre'], button_color='white', border_width=0, image_filename=perfil['imagen'])
            perfiles.append(perfil_boton)
        #front end

        titulo = [sg.Text('UNLP Image', auto_size_text=True, text_color='black', background_color='white', font=('GabrielWeiss'))]

        columna_vacia = [sg.Column([], background_color='white', size=(400,215))]
        columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

        column2_layout = [columna_vacia, perfiles, otros_perfiles, columna_vacia2]
        column1_layout = [titulo]

        column1 = sg.Column(column1_layout, size=(175,600), background_color="white")
        column2 = sg.Column(column2_layout, size=(415, 600), background_color="white", key='-column2-')

        layout = [[column1, column2]]

        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))

    def iniciar_ventana(self, cant=2):
        menu_check = False
        otros = False
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'otros':
                otros = True
                break
            else:
                menu_check = True
                perfil_act = event
                break
        self.window.close()

        if (menu_check == True):
            menu = menu_principal_ventana.VentanaMenu(perfil_act)
            menu.iniciar_ventana()
        elif (otros == True):
            self.__init__(cant)
            self.iniciar_ventana(cant+2)