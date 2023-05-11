import PySimpleGUI as sg
import os
import json
import inicio_ventana
import configuracion
import editar_perfil
import generador_memes
class VentanaMenu:
    def __init__(self, perfil_act):
        current_dir = os.path.abspath(__file__)

        relative_path = "icons/config.png"
        relative_path_2 = "icons/help.png"
        config_img = os.path.join('./', relative_path)
        help_img = os.path.join('./', relative_path_2)

        #front end
        with open('perfiles.json', 'r', encoding='utf-8') as archivo: 
            datos = json.load(archivo) #nos guardamos los perfiles del json
        
        for perfil in datos['perfiles'][0:]:
            if (perfil['nombre'] == perfil_act):
                perfil_boton = [sg.Button(enable_events=True, key=perfil['nombre'], button_color='white', border_width=0, image_filename=perfil['imagen'])]

        self.perf=perfil_act

        etiquetar_imagenes = [sg.Button('Etiquetar Imagenes', key= 'imagenes')]
        generar_meme = [sg.Button('Generar Meme', key= 'meme')]
        generar_collage= [sg.Button('Generar Collage', key='collage')]
        salir = [sg.Button('Salir', key= 'salir')]

        config = [sg.Button(key= 'config', image_filename=config_img, border_width=0, button_color="white", image_subsample=(3))]
        ayuda = [sg.Button(key= 'help', image_filename=help_img, border_width=0, button_color="white")]

        columna_vacia = [sg.Column([], background_color='white', size=(400,215))]
        columna_vacia2 = [sg.Column([], background_color='white', size=(400,400))]

        column1_layout = [perfil_boton]
        column2_layout = [columna_vacia, etiquetar_imagenes, generar_meme, generar_collage, salir, columna_vacia2]
        column3_layout = [config]
        column4_layout = [ayuda]

        column1 = sg.Column(column1_layout, size=(300, 600), background_color="white")
        column2 = sg.Column(column2_layout, size=(250, 600), background_color="white")
        column3 = sg.Column(column3_layout, size=(82, 600), background_color="white")
        column4 = sg.Column(column4_layout, size=(82, 600), background_color="white")

        layout = [[column1, column2, column3, column4]]


        self.window = sg.Window("UNLP Image", layout, background_color='white', size=(800,600))
    def iniciar_ventana(self):
        ok=False
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'salir':
                ok = True
                break
            elif event == 'config':
                self.window.close()
                self.config=configuracion.Configuracion()
                self.config.abrir_configuracion(self.perf)
            elif event == 'meme':
                self.window.close()
                self.mem= generador_memes.GeneradorMemes()
                self.mem.abrir_ventana(self.perf)
            else:
                self.window.close()
                self.edit=editar_perfil.EditarPerfil(self.perf)
                self.edit.iniciar_ventana(self.perf)
        self.window.close()

        if (ok == True):
            inicio = inicio_ventana.VentanaPrincipal()
            inicio.iniciar_ventana()
