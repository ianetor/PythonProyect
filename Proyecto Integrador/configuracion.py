import PySimpleGUI as sg
import os.path
import json
import menu_principal_ventana
class Configuracion:
            

    def __init__(self):
    
        def create_folder_input(texto):
            return sg.Column([[sg.Text(texto,font=('Arial',12),background_color='white',text_color='black')],
                            [sg.In(size=(25,1),enable_events=True, key=texto),sg.FolderBrowse(button_text='Seleccionar',button_color='black')],
                            [sg.Text('',size=(1,10),background_color='white')]],size=(450,90),background_color='white')
    
        relative_path = "botones/botonVolver2.png"
        relative_path2 = "botones/salvar.png"

        boton_volver = os.path.join('./', relative_path)
        boton_guardar = os.path.join('./', relative_path2)
 
        titulo= [sg.Text('Configuración',font=('Arial',17),background_color='white',text_color='black')]
        elem_col1= [titulo]
        espacio1= [sg.Text('',size=(1,25),background_color='white')]

        textos=['Repositorio de imagenes', 'Directorio de collages','Directorio de memes']

        columnas= [create_folder_input(textos[i]) for i in range(3)]
        columna_vacia= sg.Column([],size=(450,120),background_color='white')

        boton_volver= [sg.Button(enable_events=True,image_subsample=(10),button_color='white',border_width=0,image_size=(50,50),image_filename=boton_volver,key='VOLVER')]
        boton_guardar= [sg.Button(image_filename=boton_guardar,image_size=(50,50),button_color='white',enable_events=True,border_width=0,image_subsample=(9),key='GUARDAR')]

        elem_col3=[boton_volver,espacio1,boton_guardar]

        col1= sg.Column(elem_col1,size=(150,600),background_color='white')
        col2= sg.Column([[columna_vacia]] + [[col] for col in columnas],size=(450,600),justification='center',vertical_alignment='center',background_color='white')
        col3 = sg.Column(elem_col3,size=(100,600),background_color='white')

        layout1=[[col1,sg.Push(background_color='white'),col2,col3]]

        self.window = sg.Window('UNLPImage',background_color='white' ,element_padding=(0,3),size=(800,600),layout=layout1)
    
    def abrir_configuracion(self,perfil_act):
        datos=dict()
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            
            elif event == 'Repositorio de imagenes':
                self.carpeta_repositorio_imagenes=values["Repositorio de imagenes"]
                datos[event]=self.carpeta_repositorio_imagenes
    
            elif event == 'Directorio de collages':
                self.carpeta_directorio_collages=values["Directorio de collages"]
                datos[event]=self.carpeta_directorio_collages

            elif event == 'Directorio de memes':
                self.carpeta_directorio_memes=values["Directorio de memes"]
                datos[event]=self.carpeta_directorio_memes

            elif event == 'GUARDAR':
                with open("data.json","w",encoding='utf-8') as archivo:
                    json.dump(datos,archivo)

            elif event == 'VOLVER':
                self.window.close()
                menu_ventana = menu_principal_ventana.VentanaMenu(perfil_act)
                menu_ventana.iniciar_ventana()
        self.window.close()