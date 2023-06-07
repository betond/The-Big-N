import tkinter
from tkinter import *
from tkinter import filedialog
from hash import *
#from Cesar import *

class GUI:
    #Widgets para la interfaz
    ventana = None
    frame = None
    btn_frame = None
    action_frame = None
    label_file = None
    #RBTN_img = None
    RBTN_txt = None
    BTN_chooseFile = None
    BTN_action = None
    #label_key = None
    label_info_key = None
    textbox = None
    messages_frame = None
    messages_textbox = None

    choose_file = False
    selected_option = 0
    path_file = ""
    aes = None
    temp_widgets = []

    def __init__(self):
        # CREAR VENTANA PRINCIPAL
        self.ventana = Tk()
        self.ventana.title("Cifrador HASH")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)

        self.frame = tkinter.Frame(self.ventana)
        self.frame.pack(padx=20, pady=20)

        # LABEL PARA EL TITULO
        self.titulo = Label(self.frame, text="CIFRADOR HASH", font=("consolas", 16, "bold"),
                       foreground="#17006B", pady=20)
        self.titulo.pack()

        # LABELFRAME PARA BOTONES CIFRADO/DECIFRADO
        self.btn_frame = LabelFrame(self.frame, text="Seleccione la acción que desea realizar", font=("Gotham", 10),
                                           foreground="#650F4E", width="550", height="125", padx=10, pady=20)

        # WIDGETS PARA BUSCAR EL ARCHIVO
        self.label_file = Label(self.btn_frame, text="Selecciona un archivo de texto ",
                                font=("Helvetica", 10, "normal"))
        self.label_file.pack(side=TOP)
        self.label_file.place(rely="0.05", relx="0.2")

        self.BTN_chooseFile = Button(self.btn_frame, command=lambda: self.chooseFile(), text="Elegir archivo",
                                     overrelief="raised", bd=2, padx=20)
        self.BTN_chooseFile.pack(side=TOP)
        self.BTN_chooseFile.place(rely="0.03", relx="0.55")

        # BOTON PARA CREAR EL FRAME DE WIDGETS PARA CIFRAR
        self.btnEncrypt = Button(self.btn_frame, text="CIFRAR", relief=tkinter.GROOVE,
                                        font=("Helvetica", 10, "bold"),
                                        bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                        command=lambda: self.encrypt(self.path_file)
                                        )
        self.btnEncrypt.pack()
        self.btnEncrypt.place(rely="0.7", relx="0.3")

        # BOTON PARA CREAR EL FRAME DE WIDGETS PARA DESCIFRAR
        self.btnVerify = Button(self.btn_frame, text="VERIFICAR CONTENIDO", relief=tkinter.GROOVE,
                                        font=("Helvetica", 10, "bold"),
                                        bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                        command=lambda: self.verify(self.path_file)
                                        )
        self.btnVerify.pack()
        self.btnVerify.place(rely="0.7", relx="0.6")

        self.btn_frame.pack(fill="x")

        # LABELFRAME PARA LOS MENSAJES INFORMATIVOS
        self.messages_frame = LabelFrame(self.frame, text="Informes",
                                         font=("Gotham", 10),
                                         foreground="#650F4E", width="550", height="390", padx=10, pady=20)
        self.messages_textbox = Text(self.messages_frame, bg="#E7F5FD")

        self.btn_frame.pack(fill="x")
        self.infoFrame("Bienvenido al cifrador HASH\n")


    def run(self):
        self.ventana.mainloop()

    def chooseFile(self):
        self.path_file = filedialog.askopenfilename(title="Elegir archivo",
                                                    initialdir="D:/xenia/Documents/ESCOM/Octavo-sem/Criptografia/Practicas/PracticaHash",
                                                    filetypes=[("Archivos de Texto", "*.txt")])
        self.choose_file = True

    def infoFrame(self, message):

        # TEXTBOX PARA MENSAJES INFORMATIVOS
        self.messages_frame.pack()
        self.messages_textbox.pack(fill=BOTH)
        self.messages_textbox.insert(END, message)
        self.messages_textbox.bind("<Key>", lambda a: "break")
        self.temp_widgets.append(self.messages_frame)
        self.temp_widgets.append(self.messages_textbox)

    def encrypt(self, path_file):

        if self.choose_file == True:
            self.messages_textbox.insert(END, f"\nCIFRANDO TEXTO\n")
            self.messages_textbox.insert(END, f"Ruta del archivo: {self.path_file}\n")
            hash = HASH()
            hash.setAttributesFile(path_file)
            self.messages_textbox.insert(END, "Cifrando el archivo de texto...\n")
            hash.encryptTXT()
            self.messages_textbox.insert(END, f"\nEl archivo de texto cifrado esta listo {hash.namefile}\n")
        else:
            self.messages_textbox.insert(END, "Seleccione un archivo de texto antes\n")

    def verify(self, path_file):
        if self.choose_file == True:
            self.messages_textbox.insert(END, f"\nVERIFICANDO CONTENIDO\n")
            self.messages_textbox.insert(END, f"Ruta del archivo: {self.path_file}\n")
            hash = HASH()
            hash.setAttributesFile(path_file)
            self.messages_textbox.insert(END, "Verificando el contenido archivo de texto...\n")
            sentencia = hash.verify()
            self.messages_textbox.insert(END, f"\n{sentencia} \n")

        else:
            self.messages_textbox.insert(END, "Seleccione un archivo de texto antes\n")