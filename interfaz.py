import flet as ft
from numeros import glifos

def main(page: ft.Page):
    page.bgcolor=ft.Colors.WHITE
    page.title="Números"
    page.scroll="always"
    page.window.width=1200
    page.window.height=700
    page.window.resizable=True
    page.update()
    o=glifos()
    ruta=""

#-----CONTENEDOR 1-------------

#---- subir Archivo----------
    def cargarA(e:ft.FilePickerResultEvent):
        nonlocal ruta
        if e.files:
            file = e.files[0]
            ruta = file.path
        if ruta:
            try:
                o.cargar(ruta)
                lista=[]
                for numeros in o.num:
                    linea=str(numeros)
                    lista.append(linea) 
                texto = "\n".join(lista)
                caja_txt1.value=texto
                page.update()

            except Exception as error:                
                msj_exito.value="No se pudo leer el archivo ERROR"
                page.update()
        else:
            msj_exito.value= "Ruta inválida al subir el archivo"
            page.update()

    
    msj_exito=ft.Text(
        "",
        size=15,
        color="#042025",
        text_align=ft.TextAlign.CENTER,
        font_family="Bebas Neue"
    )
    selectorA=ft.FilePicker(on_result=cargarA)
    page.overlay.append(selectorA)

    subirA=ft.ElevatedButton(
        "Subir Archivo",
        on_click=lambda _: selectorA.pick_files(allow_multiple=False),
        width=140,
        height=40,
        icon=ft.Icons.UPLOAD_FILE_OUTLINED,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor="#042025",
            text_style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,)
        ),
    )
    #-----Carga Resultado----------------
    def m_resultados(e):
        nonlocal ruta
        o.num.clear()
        texto=caja_txt1.value.strip()
        lineas=texto.splitlines()
        if texto:
            for linea in lineas:
                if linea =="":
                    continue
                if linea.isdigit():
                    o.num.append(int(linea))
                else:
                    o.num.append(linea)
            ruta=""
            o.diccF.clear()
            o.procesar()
            textoD=""
            for clave, valor in o.diccF.items():
                valor="".join(valor)
                textoD += f"{clave}: {valor}\n\n"
            caja_txt2.value = textoD.strip()
            page.update()
        else:
            msj_exito.value="Text Box vacía Escribe algo para procesar"
            page.update()

    
    #-------Limpiar-----------------------
    def limpiar(e):
        o.diccF.clear()
        o.num.clear()
        caja_txt1.value=""
        caja_txt2.value=""
        msj_exito.value=""
        page.update()

    #------Descargar-----------------
    def downloand(e):
        contenido=caja_txt2.value.strip()
        print(contenido)
        if contenido:
            with open("salidaglifos.txt",'w',encoding="utf-8-sig") as file:
                file.write(contenido)
            msj_exito.value=" Archivo descargado exitosamente."
            page.update()
        else:
            msj_exito.value="¡Primero procesa la informacón!"
            page.update()

    #----cajas de texto-------------------
    caja_txt1=ft.TextField(
        label="\n\nNúmeros a transformar\n",
        label_style=ft.TextStyle(color=ft.Colors.WHITE,font_family="Arial",size=18),
        hint_text="Escribe aquí...",
        hint_style=ft.TextStyle(color=ft.Colors.WHITE, italic=True),
        width=230, 
        filled=True, 
        bgcolor= "#042025",
        border_color="#042025",
        border_radius=10,  
        multiline=True, 
        min_lines=6, 
        max_lines=6,
        text_style=ft.TextStyle( 
        color=ft.Colors.WHITE,
        size=20, 
        weight=ft.FontWeight.W_600,
        font_family="Roboto",
        height=1.5  
        ),
        
    )

    caja_txt2=ft.TextField(
        label="\nResultado",
        read_only=True,
        label_style=ft.TextStyle(color=ft.Colors.WHITE,font_family="Arial",size=18),
        width=230,
        filled=True, 
        bgcolor= "#042025", 
        border_color="#042025",  
        border_radius=10,  
        multiline=True,
        min_lines=6,
        max_lines=6,
        text_style=ft.TextStyle(  
        color=ft.Colors.WHITE,
        size=20, 
        weight=ft.FontWeight.W_600,
        font_family="Roboto",
        height=1.5
        ),       
    )

    fila_caja=ft.Row(
        [caja_txt1,caja_txt2],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    procesar=ft.ElevatedButton(
        "Procesar",
        on_click=m_resultados,
        width=120,
        height=40,
        style=ft.ButtonStyle(
                color="#042025",   
                bgcolor="#FFFFFF", 
                text_style=ft.TextStyle(
                    size=18,
                    weight=ft.FontWeight.BOLD,
                )        
        ),
        icon=ft.Icons.SETTINGS
    )

    limpia=ft.ElevatedButton(
        "Limpiar",
        on_click=limpiar,
        width=120,
        height=40,
        style=ft.ButtonStyle(
                color="#042025",    
                bgcolor="#FFFFFF",
                text_style=ft.TextStyle(
                    size=18,
                    weight=ft.FontWeight.BOLD,
                )        
        ),
        icon=ft.Icons.DELETE
    )

    descargar=ft.ElevatedButton(
        "Descargar",
        on_click=downloand,
        width=130,
        height=40,
        style=ft.ButtonStyle(
                color="#042025",    
                bgcolor="#FFFFFF",
                text_style=ft.TextStyle(
                    size=18,
                    weight=ft.FontWeight.BOLD,
                )        
        ),
        icon=ft.Icons.FILE_DOWNLOAD
    )

    fila_boton1=ft.Row(
        [procesar,descargar,limpia],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )

   

    titulo= ft.Text(
            " Números Glíficos\n Antiguos",      
            size=50,
            weight="bold",
            color="#042025",
            text_align=ft.TextAlign.CENTER,
            font_family="Bebas Neue"
        
        )
    
    subTi=ft.Text(
        " ¡Transforma Tus Números Naturales a Glificos!",      
        size=20,
        color="#042025",
        text_align=ft.TextAlign.CENTER,
        font_family="Bebas Neue"
    )
#------Contenedor1
    contenedor1 = ft.Container(
    margin=ft.Margin(10,20,10,10),
    width=page.width * 0.4 if page.width > 700 else 400,
    height=600,
    bgcolor="#cbe4f3",
    border_radius=30,

    content=ft.Column(
        controls=[
            # Sección de cabecera: Stack con fondo y el boton
            ft.Container(
                height=70,  
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            width=180,
                            height=80,
                            margin=ft.Margin(-0.8,0,0,0),
                            image=ft.DecorationImage(
                                src="assets/esquina_left.png",                            
                               alignment=ft.Alignment(-1.0, -1.0),
                            ),
                            alignment=ft.Alignment(-1.0, -1.0),
                        ),
                        ft.Container(
                            content=subirA,
                            alignment=ft.Alignment(-0.96, -0.7),
                        ),
                    ],
                    expand=True,
                ),
            ),

            # Titulo
            ft.Container(
                content=titulo,
                padding=ft.Padding(0, -30, 0, 30),
            ),

            #Subtitulo
            ft.Container(
                content=subTi,
                padding=ft.Padding(0, -10, 0, 0),
            ),
            #fila de las cajas
            ft.Container(
                content=fila_caja, 
                padding=ft.Padding(0, 10, 0, 0),
            ),
            # mensaje de exito
            ft.Container(
                content=msj_exito,
            ),
            # Fila de botones
            ft.Container(
                content=fila_boton1,
                padding=ft.Padding(0, 0, 0, 0),
            ),
        ],
        spacing=5,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    ),
    expand=True
)
    
#----CONTENEDOR 2-------------

    indica_msj=ft.Container(
        opacity=0.0,
        animate_opacity=300,
        visible=True
    )

    def mostrar_msj(tipo):
        cerrarTodo()
        if tipo =='historia':
            texto=" La antigua y olvidada civilización AETHELGARD y su necesidad para representar cantidades y"\
                    "gestionar el comercio crearon el sistema numérico GLIFICO, el cual poseía ciertas reglas:\n\n"\
                        "•	Los glifos se suman si van de mayor a menor.\n\n"\
                        "•	Si un glifo menor va antes de uno mayor se resta, pero los únicos glifos que se pueden "\
                            "usar para restar son los glifos de 1 como: Σ, Ω, Φ, Ξ.\n\n"\
                        "•	Un mismo glifo no puede repetirse más de 3 veces seguidas.\n\n"\
                        "•	Los glifos del 5 como: Λ, Δ, Ψ no se pueden restar ni repetir.\n\n"\
                    "Este programa transforma los números del sistema decimal, enteros positivos a este fascinante sistema "\
                    "de números glíficos.\n\n"
            titulo='HISTORIA\n'

        if tipo =='instruc':
            texto="Sigue estos pasos:\n\n"\
                "•	Haz click en el botón Subir Archivo para cargar un" \
                    "archivo .txt o escribe directamente en la caja de texto \n los números que deseas " \
                    "trasformar. \n\n"\
                "•	Dale click al botón Procesar para ver la transformación.\n\n"\
                "•	Puedes descargar el resultado haciendo click en " \
                    "Descargar, el archivo guardado se llamará salidaglifos.txt\n\n" \
                "•	Puedes darle click al botón limpiar para borrar todo.\n"
            titulo='INSTRUCCIONES\n'
            
        indica_msj.content=ft.Card(
            elevation=4,
            color="rgba(255, 255, 255, 0.85)",
            content=ft.Container(
                padding=20,
                height=300,
                content=ft.ListView(
                expand=True,
                controls=[
                    ft.Text(titulo, size=20, color="#042025", weight='bold'),
                    ft.Text(texto, color="#042025"),
                    ft.ElevatedButton(
                        "Cerrar",
                        on_click=lambda _: ocultar(),
                        bgcolor="#cbe4f3",
                        color="#042025"
                    )
                ]
            )
        )
    )
        indica_msj.opacity=1.0
        page.update()

    def ocultar():
        indica_msj.opacity=0.0
        page.update()

    instruc=ft.ElevatedButton(
        "Instrucciones",
        on_click=lambda _:mostrar_msj("instruc"),
        width=120,
        height=40,
        style=ft.ButtonStyle(
                color="#042025",
                bgcolor="#cbe4f3",
                text_style=ft.TextStyle(
                    size=15,
                    weight=ft.FontWeight.BOLD,
                )
        )
    )

    historia=ft.OutlinedButton(
        "Historia",
        on_click=lambda _:mostrar_msj("historia"),
        width=120,
        height=40,
        style=ft.ButtonStyle(
                side=ft.BorderSide(width=1, color="#042025"),
                color="#042025",
                bgcolor=ft.Colors.WHITE,
                text_style=ft.TextStyle(
                    size=15,
                    weight=ft.FontWeight.BOLD,
                )
        )
    )
    #----------funsiones de glifo-----------------------
    simbolos = ['Σ', 'Λ', 'Ω', 'Δ', 'Φ', 'Ψ', 'Ξ']
    mensajes = {
        'Σ': 'Nombre: Sigma | Número: 1',
        'Λ': 'Nombre: Lambda | Número: 5',
        'Ω': 'Nombre: Omega | Número: 10',
        'Δ': 'Nombre: Delta | Número: 50',
        'Φ': 'Nombre: Phi | Número: 100',
        'Ψ': 'Nombre: Psi | Número: 500',
        'Ξ': 'Nombre: Xi | Número: 1000',
    }
    filas=[]
    #botones_visible=False
    colum_button=ft.Column(spacing=10,visible=False)

    def cerrarTodo(e=None):
        for _, mensaje in filas:
            mensaje.visible = False
        colum_button.visible=False
        page.update()

    def info_glifo(indicador):
        def manejador(e):
            cerrarTodo()
            colum_button.visible=True
            filas[indicador][1].visible=True
            page.update()
        return manejador

    for i, simbolo in enumerate(simbolos):
        boton = ft.OutlinedButton(
            simbolo,
            style=ft.ButtonStyle(
                color="#042025",
                bgcolor=ft.Colors.WHITE,
                text_style=ft.TextStyle(
                    size=25,
                    weight=ft.FontWeight.BOLD,
                )
            ),
            on_click=info_glifo(i),
            width=60
        )

        mensaje = ft.Container(
            content=ft.Text(mensajes[simbolo], size=15,color=ft.Colors.WHITE,weight='Bold'),
            padding=10,
            bgcolor="#042025",
            border_radius=8,
            visible=False
        )

        f = ft.Row(controls=[boton, mensaje], spacing=10)
        filas.append((f, mensaje))
        colum_button.controls.append(f)

    # interruptor para glifos"
    def interrup(e):
        ocultar()
        if colum_button.visible:
            cerrarTodo()
        else:
            colum_button.visible = True
        page.update()

    glifo=ft.OutlinedButton(
        "Glifos",
        on_click=interrup,
        width=120,
        height=40,
        style=ft.ButtonStyle(
                side=ft.BorderSide(width=1, color="#042025"),
                color="#042025", 
                bgcolor=ft.Colors.WHITE, 
                text_style=ft.TextStyle(
                    size=15,
                    weight=ft.FontWeight.BOLD,
                )
        )
    )

    cabecera2=ft.Row(
        [glifo,historia,instruc],
        spacing=7,
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    contenedor2 = ft.Container(
    margin=ft.Margin(15,20,15,10),
    height=600,
    border_radius=30,
    padding=ft.Padding(0,-0.7,-2,0),

    #fondo
    image=ft.DecorationImage(
            src="assets/imagenf.png",
            fit=ft.ImageFit.COVER,
    ),
    content=ft.Column(
        controls=[
            ft.Container(
                height=100,
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            height=98,
                            alignment=ft.Alignment(1, -1),
                            image=ft.DecorationImage(
                                src="assets/esquina_right.png",
                                alignment=ft.Alignment(1, -1),
                            ),
                            padding=ft.Padding(0, 0, 0, 0),
                        ),

                        ft.Container(
                            content=cabecera2,
                            padding=ft.Padding(0, 0, 8, 0),
                            alignment=ft.Alignment(-0.96, -0.7),
                        ),
                    ],
                    expand=True,
                ),
                
            ),
            ft.Container(
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            content=indica_msj,
                            margin=ft.Margin(130,0,0,0),
                            padding=ft.Padding(0, 20, 8, 0),
                            width=350
                        ),
                        ft.Container(
                            content=colum_button,
                            margin=ft.Margin(130,-20,0,0)
                        ),
                    ]
                )
            )
            
        ],
        spacing=20,
    ),
    expand=True,
    )

    cont_prin=ft.Row(
        [contenedor1,contenedor2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        #wrap=True,
        expand=True
    )

    page.add(cont_prin)

ft.app(target=main)