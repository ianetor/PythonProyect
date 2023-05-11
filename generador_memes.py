import PySimpleGUI as sg
import configuracion
import menu_principal_ventana
import json
import os
from PIL import Image
class GeneradorMemes:
    def __init__ (self):
        with open('data.json','r') as archivo:
            datos=json.load(archivo)
            self.dir_imagenes = datos['Repositorio de imagenes']
        self.archivos_imagenes = self.obtener_imagenes()

        self.elegir_imagen=[[sg.Text('Selecciona una imagen'),sg.Listbox(select_mode='extended',enable_events=True,values=self.archivos_imagenes,size=(30,5),key='imagenes'),sg.Button('Aceptar',key='listo',enable_events=True)]]

        col_vacia1=[[sg.Text('',size=(25,1),text_color=('white'),background_color='white')]]

        self.image_viewer_column = [
            [sg.Image(key="-IMAGE-",size=(300,300))],
        ]       


        self.layout1=[[sg.Column(self.elegir_imagen,background_color='white'),sg.Column(self.image_viewer_column)]]
        self.window = sg.Window('UNLPImage',self.layout1,size=(800,600),background_color='white')
    def obtener_imagenes(self):
        return [
            archivo 
            for archivo in os.listdir(self.dir_imagenes)
            if os.path.isfile(os.path.join(self.dir_imagenes, archivo))
               and archivo.lower().endswith((".png", ".gif"))
        ]
    def abrir_ventana(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event== 'imagenes':
                self.window['imagenes'].update(values=self.obtener_imagenes())
            elif event == 'listo':
                print('hola')
                selected_files = values['imagenes']
                print(values['imagenes'])
                if selected_files:
                    print(values['imagenes'])
                    filename = os.path.join(self.dir_imagenes, selected_files[0])
                    print(filename)
                    image= Image.open(filename)
                    image.thumbnail((300,300))
                    image_data = image.tobytes()
                    self.window["-IMAGE-"].update(data=image_data,size=(300,300))
        self.window.close()