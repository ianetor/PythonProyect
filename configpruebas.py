import PySimpleGUI as sg
import os.path

def create_folder_input(texto):
    return sg.Column([[sg.Text(texto,font=('Arial',12))],[sg.In(size=(25,1),
            enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(button_text='Seleccionar')],[sg.Text('',size=(1,10))]],size=(450,90))

sg.theme('')

titulo= [
    sg.Text('Configuración',font=('Arial',17))
    ]
elemcol1= [titulo]
espacio1= [sg.Text('',size=(1,30))]

textos=['Repositorio de imagenes', 'Directorio de collages','Directorio de memes']

columnas= [[create_folder_input(textos[i])] for i in range(3)]
columna_vacia= sg.Column([],background_color='white',size=(450,150))
print(columnas)
elemcol2= [columnas]

boton_volver= [sg.Button('< Volver',font=('Arial',10),size=(10,1))]
boton_guardar= [sg.Button('Guardar',font=('Arial',10),size=(10,2))]

elemcol3=[boton_volver,espacio1,boton_guardar]

col1= sg.Column(elemcol1,size=(150,600))
col2= sg.Table(values=elemcol2,size=(450,600),num_rows=3,justification='center')
col3 = sg.Column(elemcol3,size=(100,600))

layout1=[[col1,sg.Push(),col2,col3]]

window = sg.Window('UNLPImage', element_padding=(0,3),size=(800,600),layout=layout1)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "-FOLDER-":
        folder=values["-FOLDER-"]

window.close()
