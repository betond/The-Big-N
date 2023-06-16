import tkinter
from tkinter import *
from tkinter import filedialog
from Hash import *

class GUI:
    #Widgets para la interfaz
    ventana = None
    frame = None
    btn_frame = None
    action_frame = None
    label_file = None
    BTN_chooseFile = None
    BTN_chooseFile2 = None
    BTN_action = None
    label_key = None
    messages_frame = None
    messages_textbox = None
    message_pathfile = ""
    key_pathfile = ""
    temp_widgets = []

    def __init__(self):
        # CREAR VENTANA PRINCIPAL
        self.ventana = Tk()
        self.ventana.title("Integridad - Autenticación - No Repudio - Confidencialidad")
        self.ventana.geometry("800x800")
        self.ventana.resizable(0, 0)

        self.frame = tkinter.Frame(self.ventana)
        self.frame.pack(padx=20, pady=20)

        # LABEL PARA EL TITULO
        self.titulo = Label(self.frame, text="Practica Final", font=("consolas", 16, "bold"),
                       foreground="#17006B", pady=20)
        self.titulo.pack()

        # LABELFRAME PARA BOTONES CIFRADO/DECIFRADO
        self.btn_frame = LabelFrame(self.frame, text="Seleccione la acción que desea realizar", font=("Gotham", 10),
                                           foreground="#650F4E", width="550", height="100", padx=10, pady=20)

        # BOTON PARA CREAR EL FRAME DE WIDGETS PARA CIFRAR
        self.encryptGUI_btn = Button(self.btn_frame, text="CIFRAR y FIRMAR", relief=tkinter.GROOVE,
                                        font=("Helvetica", 10, "bold"),
                                        bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                        command=lambda: self.generateActionFrame("CIFRAR y FIRMAR")
                                        )
        self.encryptGUI_btn.pack()
        self.encryptGUI_btn.place(rely="0.2", relx="0.3")

        # BOTON PARA CREAR EL FRAME DE WIDGETS PARA DESCIFRAR
        self.decryptGUI_btn = Button(self.btn_frame, text="VERIFICAR Y DESCIFRAR", relief=tkinter.GROOVE,
                                        font=("Helvetica", 10, "bold"),
                                        bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                        command=lambda: self.generateActionFrame("VERIFICAR Y DESCIFRAR")
                                        )
        self.decryptGUI_btn.pack()
        self.decryptGUI_btn.place(rely="0.2", relx="0.6")

        # LABELFRAME PARA LOS MENSAJES INFORMATIVOS
        self.messages_frame = LabelFrame(self.frame, text="Informes",
                                         font=("Gotham", 10),
                                         foreground="#650F4E", width="550", height="390", padx=10, pady=20)
        self.messages_textbox = Text(self.messages_frame, bg="#E7F5FD")

        self.btn_frame.pack(fill="x")


    def run(self):
        self.ventana.mainloop()


    def clearActionFrame(self):
        if len(self.temp_widgets) != 0:
            self.action_frame.pack_forget()
            #self.label_file.pack_forget()
            #self.BTN_action.pack_forget()
            #self.RBTN_img.pack_forget()
            #self.RBTN_txt.pack_forget()
            self.messages_frame.pack_forget()
            self.messages_textbox.pack_forget()
            self.messages_textbox.delete("1.0",END)
            self.BTN_chooseFile.pack_forget()
            self.BTN_chooseFile2.pack_forget()

    def generateActionFrame(self, action):
        self.clearActionFrame()
        self.message_pathfile = ''
        self.key_pathfile = ''

        #CREAR DE EL FRAME PARA LA ACCIONA
        self.action_frame = LabelFrame(self.frame, text=action,
                                            font=("Gotham", 10),
                                            foreground="#650F4E", width="550", height="210", padx=10, pady=20)
        self.action_frame.pack()
        self.temp_widgets.append(self.action_frame)

        #WIDGETS PARA BUSCAR EL ARCHIVO A CIFRAR
        self.label_file = Label(self.action_frame, text="Selecciona el archivo que contiene el mensaje",
                            font=("Helvetica", 10, "normal"))
        self.label_file.pack(side=TOP)
        self.label_file.place(rely="0.05", relx="0.1")
        self.temp_widgets.append(self.label_file)

        self.BTN_chooseFile = Button(self.action_frame, command=lambda: self.chooseFile("message_pathfile"), text="Elegir archivo",
                                     overrelief="raised", bd=2, padx=20)
        self.BTN_chooseFile.pack(side=TOP)
        self.BTN_chooseFile.place(rely="0.03", relx="0.65")
        self.temp_widgets.append(self.BTN_chooseFile)


        #WIDGETS PARA INGRESAR LA LLAVE
        self.label_key = Label(self.action_frame, text="Selecciona el archivo de la llave ",
                            font=("Helvetica", 10, "normal"))
        self.label_key.pack()
        self.label_key.place(rely="0.50", relx="0.1")

        self.BTN_chooseFile2 = Button(self.action_frame, command=lambda: self.chooseFile("key_pathfile"), text="Elegir archivo",
                                     overrelief="raised", bd=2, padx=20)
        self.BTN_chooseFile2.pack(side=TOP)
        self.BTN_chooseFile2.place(rely="0.52", relx="0.5")
        self.temp_widgets.append(self.BTN_chooseFile)


        if action == "CIFRAR":
            self.BTN_action = Button(self.action_frame, text="CIFRAR", relief=tkinter.GROOVE,
                                     font=("Helvetica", 10, "bold"),
                                     bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                     background="#0E4C6D", foreground="#FFFFFF",
                                     command=lambda :self.hashFunction()
                                     )
        else:
            self.BTN_action = Button(self.action_frame, text="VERIFICAR", relief=tkinter.GROOVE,
                                     font=("Helvetica", 10, "bold"),
                                     bd=5, activeforeground="#F50743", activebackground="pink", overrelief="raised",
                                     background="#0E4C6D", foreground="#FFFFFF",
                                     command=lambda :self.verify()
                                     )
        self.BTN_action.pack()
        self.BTN_action.place(rely="0.8", relx="0.8")
        self.temp_widgets.append(self.BTN_action)

        #TEXTBOX PARA MENSAJES INFORMATIVOS
        self.messages_frame.pack()
        self.messages_textbox.pack(fill=BOTH)
        self.messages_textbox.insert(END, "Bienvenid@\n")
        self.messages_textbox.bind("<Key>", lambda a: "break")
        self.temp_widgets.append(self.messages_frame)
        self.temp_widgets.append(self.messages_textbox)

    def chooseFile(self, w_file):
        if w_file == "message_pathfile":
            self.message_pathfile = filedialog.askopenfilename(title="Elegir archivo",
                                                        initialdir="D:/xenia/Documents/ESCOM/Octavo-sem/Criptografia/Practicas/PracticaHash-RSA",
                                                        filetypes=[("Archivos de Texto", "*.txt")])

        if w_file == "key_pathfile":
            self.key_pathfile = filedialog.askopenfilename(title="Elegir archivo",
                                                        initialdir="D:/xenia/Documents/ESCOM/Octavo-sem/Criptografia/Practicas/PracticaHash-RSA",
                                                        filetypes=[("Archivo PEM", "*.pem")])

    def areFilesChosen(self):
        if self.key_pathfile != '' and self.message_pathfile != '':
            return True
        else:
            return False

    def hashFunction(self):
        if self.areFilesChosen() == True:
            self.messages_textbox.delete('1.0', END)
            self.messages_textbox.insert(END, f"\nFIRMANDO ARCHIVO\n")
            self.messages_textbox.insert(END, f"Ruta del archivo: {self.message_pathfile}\n")
            hash = HASH()
            hash.setAttributesFile(self.message_pathfile, self.key_pathfile)
            self.messages_textbox.insert(END, "Agregando firma al archivo de texto...\n")
            hash.getDigest()
            self.messages_textbox.insert(END, f"\nEl archivo de texto se firmo correctamente ({hash.namefile})\n")
        else:
            self.messages_textbox.insert(END, "Seleccione los archivos necesarios antes\n")

    def verify(self):
        if self.areFilesChosen() == True:
            self.messages_textbox.delete('1.0', END)
            self.messages_textbox.insert(END, f"\nVERIFICANDO CONTENIDO\n")
            self.messages_textbox.insert(END, f"Ruta del archivo: {self.message_pathfile}\n")
            hash = HASH()
            hash.setAttributesFile(self.message_pathfile, self.key_pathfile)
            self.messages_textbox.insert(END, "Verificando el contenido archivo de texto...\n")
            sentencia = hash.verify()
            self.messages_textbox.insert(END, f"\n{sentencia} \n")

        else:
            self.messages_textbox.insert(END, "Seleccione los archivos necesarios antes\n")