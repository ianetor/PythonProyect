import PySimpleGUI as sg
import json
import os
import menu_principal_ventana
import nuevoPerfil
class VentanaPrincipal:

    '''Metodo que se encarga de preparar la ventana previamente a ser iniciada, recibe un parametro opcional que nos indica a partir de que perfil mostrar en pantalla'''
    def __init__(self, indice_perfiles=0):

        '''Nos preparamos todas las rutas que vamos a usar en la ventana'''

        current_dir = os.path.abspath(__file__)
        relative_path = "botones/icon_add.png"
        relative_path_2 = "botones/ver_mas.png"

        icon_add = os.path.join('./', relative_path)
        ver_mas = os.path.join('./', relative_path_2)

        '''Abrimos el archivo de perfiles, previamente generado, y nos guardamos los mismos'''
        with open('perfil.json', 'r', encoding='utf-8') as archivo: 
            self.datos = json.load(archivo)

        '''Generamos todos los objetos con los que vamos a interactuar en la ventana'''

        agregar_perfil = sg.Button(enable_events=True, key='add', button_color='white', border_width=0, image_subsample=(4), image_filename=icon_add) #boton para añadir perfiles
        otros_perfiles = [sg.Button(enable_events=True, key='otros', button_color='white', border_width=0, size=(20,5), pad=(135,10), image_subsample=(3), image_filename=ver_mas)]

        perfiles = [agregar_perfil]


        if (indice_perfiles >= len(self.datos)):
            indice_perfiles = len(self.datos)-1
        

        for perfil in self.datos[indice_perfiles:]:
            perfil_boton = sg.Button(enable_events=True, key=perfil['nick'], button_color='white', border_width=0, image_filename=perfil['imagen'])
            perfiles.append(perfil_boton)

        titulo = [sg.Text('UNLP Image', auto_size_text=True, text_color='black', background_color='white', font=('GabrielWeiss'))]

        columna_vacia = [sg.Column([], background_color='white', size=(400,215))]
        columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

        column2_layout = [columna_vacia, perfiles, otros_perfiles, columna_vacia2]
        column1_layout = [titulo]

        column1 = sg.Column(column1_layout, size=(175,600), background_color="white")
        column2 = sg.Column(column2_layout, size=(415, 600), background_color="white", key='-column2-')

        layout = [[column1, column2]]

        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))

    '''Metodo que se encarga de iniciar la ventana'''
    def iniciar_ventana(self, cant=2):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'otros':
                self.window.close()
                self.__init__(cant)
                self.iniciar_ventana(cant+2)
            elif event == 'add':
                self.window.close()
                new=nuevoPerfil.NuevoPerfil()
                new.iniciar_ventana()
            else:
                self.window.close()
                menu = menu_principal_ventana.VentanaMenu(event)
                menu.iniciar_ventana()
        self.window.close()
    
