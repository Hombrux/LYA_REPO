#Importaciones
from tkinter import *
from PIL import ImageTk, Image 
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from functools import partial

import os
import re
import speech_recognition as sr
import tkinter as tk
import tkinter.font as tkFont

import AnalizadorLexico as al
import AnalizadorSintactico as asx

'''
a) ...   

'''

#=============== Analasis Lexico y Sintactico ===============
def analizar():
    al.analizaar(txtBox1,txtBox2)
    asx.BuscarS(al.b)
    
    #Imprimir los errores sintacticos 
    concatena=""
    i=0
    while(len(asx.Errores)>i):
        concatena += asx.Errores[i] + '\n'
        i+=2
    #print(asx.Errores)       
    txtBox3.delete('1.0', END)
    txtBox3.insert(END, concatena)

    if(concatena == ""):
        txtBox3.insert(END, 'Completado Exitosamente')
    
    else:
        #Etiquetas para los errores
        i=0
        ie=0
        while(len(asx.Errores)>i):
            n = str(ie)
            f = str(ie+1)
            imge = asx.Errores[i+1]
            txtBox3.tag_add('Error'+n,n+'.0',f+'.end - 1c')
            txtBox3.tag_config('Error'+n,underline=True)
           
            weboz = partial(getInx,numero=imge)
            txtBox3.tag_bind('Error'+n,'<Button-3>',imagen)
            txtBox3.tag_bind('Error'+n,'<Button-1>',weboz)
            

            ie+=1
            i+=2
    c.configure(image = None)
    c.image = None    


#RUTA PARA LAS IMAGENES
base_folder = os.path.dirname(__file__)
a = base_folder.split(os.sep)
a[len(a)-1]= 'ARCHIVOS'+os.sep+'IMAGENES'
base_folder = ''
i=0
while(i<len(a)):
    base_folder+= a[i] + os.sep
    i+=1

global lista
lista=[]
#Guardar los indices de las imagenes
def getInx(event,numero):
    lista.append(numero)
    #print(lista)
    #print(len(lista))

#Desplegar las imagenes
def imagen(event):
    global lista
    if not lista:
        return
    img = lista[0]
    ruta=base_folder+img
    lista.clear()
    imagen = Image.open(ruta)
    imgRes = imagen.resize((400,200), Image.ANTIALIAS)
    automata = ImageTk.PhotoImage(imgRes)
    c.configure(image=automata)#image=PhotoImage(file=ruta))
    c.image=automata
    c.pack(fill=BOTH)
    im.update_idletasks()


#===================== COLOREAR =======================
def colorear(Palabra,color):
    contenido = txtBox1.get(1.0,'end-1c')
    contenido = contenido.upper()
    palabras = contenido.split()
    indiceInicial = "1.0"

    i=0

    while i<len(palabras):
        
        if palabras[i] == Palabra:
            #Busca la palabra
            iniFeak = txtBox1.search(Palabra,index=indiceInicial ,stopindex='end',nocase=True,count=len(Palabra),regexp=True)
            inxFin = iniFeak + " + "+ str(len(Palabra)) +"c" 
            
            #Crear una etiqueta para el color 
            txtBox1.tag_add(Palabra+str(i),iniFeak,inxFin)
            txtBox1.tag_config(Palabra+str(i),foreground=color)
            indiceInicial=inxFin 
        i+=1

def BuscarP(event):
    contenido = txtBox1.get(1.0,'end-1c')
    contenido = contenido.upper()
    palabras = contenido.split()

    i=0
    while i<len(palabras):
        if palabras[i] == "IMPORT":
            colorear(Palabra="IMPORT",color="blue")
        elif palabras[i] == "DEF":
            colorear(Palabra="DEF",color="blue")  
        elif palabras[i] == "CLASS":
            colorear(Palabra="CLASS",color="blue")  
        elif palabras[i] == "IF":
            colorear(Palabra="IF",color="indigo")  
        elif palabras[i] == "ELSE":
            colorear(Palabra="ELSE",color="indigo") 
        elif palabras[i] == "FOR":
            colorear(Palabra="FOR",color="red")
        elif palabras[i] == "IN":
            colorear(Palabra="IN",color="green")     
        elif palabras[i] == "RANGE":
            colorear(Palabra="RANGE",color="green") 
        elif palabras[i] == "SELF":
            colorear(Palabra="SELF",color="blue") 
        elif palabras[i] == "WHILE":
            colorear(Palabra="WHILE",color="red") 
        elif palabras[i] == "TRY":
            colorear(Palabra="TRY",color="green") 
        elif palabras[i] == "EXCEPT":
            colorear(Palabra="EXCEPT",color="green")
        elif palabras[i] == "RETURN":
            colorear(Palabra="RETURN",color="red") 
        elif palabras[i] == "BREAK":
            colorear(Palabra="BREAK",color="aqua")
        elif palabras[i] == "NEXT":
            colorear(Palabra="NEXT",color="green")

        elif palabras[i] == "INPUT":
            colorear(Palabra="INPUT",color="green")
        elif palabras[i] == "PRINT":
            colorear(Palabra="PRINT",color="green")
        elif palabras[i] == "INT":
            colorear(Palabra="INT",color="orange")
        elif palabras[i] == "FLOAT":
            colorear(Palabra="FLOAT",color="midnightblue")
        elif palabras[i] == "BOOLEAN":
            colorear(Palabra="BOOLEAN",color="midnightblue")
        elif palabras[i] == "STRING":
            colorear(Palabra="STRING",color="midnightblue")
        
        elif palabras[i] == "POWER":
            colorear(Palabra="POWER",color="gold")
        elif palabras[i] == "SQRT":
            colorear(Palabra="SQRT",color="gold")
        elif palabras[i] == "AND":
            colorear(Palabra="AND",color="magenta")
        elif palabras[i] == "OR":
            colorear(Palabra="OR",color="magenta")
        elif palabras[i] == "NOT":
            colorear(Palabra="NOT",color="magenta")
        elif palabras[i] == "BEGIN":
            colorear(Palabra="BEGIN",color="red")
        elif palabras[i] == "END":
            colorear(Palabra="END",color="red")
                                                              
        i+=1
    
#=================Archivo=================
def file1():    
    if not txtBox1.edit_modified():      
        txtBox1.delete('1.0', END)
    else:        
        savefileas()
          
        txtBox1.delete('1.0', END)  
    
    txtBox1.edit_modified(0)
#=============Abrir archivo==================
def openfile():
    
    if not txtBox1.edit_modified():       
        try:            
            path = filedialog.askopenfile(filetypes = (("All files", "*.*"), ("Text files", "*.txt"))).name          
            
            ventana.title('Compilador - ' + path)

            with open(path, 'r') as f:             
                content = f.read()
                txtBox1.delete('1.0', END)
                txtBox1.insert('1.0', content)
                                
                txtBox1.edit_modified(0)
             
        except:
            pass   
    
    else:       
        savefileas()      
        
        txtBox1.edit_modified(0)              
        openfile()   
#========================Guardar como==========================
def savefile():    
    try:
        
        path = ventana.title().split('-')[1][1:]   
    
    except:
        path = ''
    
    if path != '':
        
        with open(path, 'w') as f:
            content = txtBox1.get('1.0', END)
            f.write(content)
      
    else:
        savefileas()    
    
    txtBox1.edit_modified(0)

def savefileas():    
    try:
        path = filedialog.asksaveasfile(filetypes = (("All files", "*.*"), ("Text files", "*.txt"))).name
        ventana.title('Compilador - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(txtBox1.get('1.0', END))

#Voz
def Voz():
    r = sr.Recognizer() 

    with sr.Microphone() as source:
        print('Habla: ')
        audio = r.listen(source)
 
    try:
        text = r.recognize_google(audio, language='es-MX').lower()
        print('Lo que dijo: {}'.format(text))

        text = text.replace('abre paréntesis', '(')
        text = text.replace('cerrar paréntesis', ')')
        text = text.replace('abre corchete', '[')
        text = text.replace('cerrar corchetes', ']')
        text = text.replace('abre llave', '{\n')
        text = text.replace('cerrar llave', '}\n')
        text = text.replace('letra', '')
        text = text.replace('punto y coma', ';\n')
        text = text.replace('punto', '.')
        text = text.replace('comilla', '\'')
        text = text.replace('coma', ',\n')
        text = text.replace('fin de comentario', '\n')
        text = text.replace('comentario', '#')
        text = text.replace('mayor o igual que', '>=')
        text = text.replace('menor o igual que', '<=')
        text = text.replace('mayor que', '>')
        text = text.replace('menor que', '<')
        text = text.replace('á', 'a')
        text = text.replace('é', 'e')
        text = text.replace('í', 'i')
        text = text.replace('ó', 'o')
        text = text.replace('ú', 'u')
        text = text.replace('sino', 'ELSE')
        text = text.replace('si', 'IF')
        text = text.replace('mas', '+')
        text = text.replace('menos', '-')
        text = text.replace('por', '*')
        text = text.replace('entre', '/')
        text = text.replace('diferente', '!=')
        text = text.replace('iniciar', 'BEGIN\n')
        text = text.replace('terminar', 'END\n')
        text = text.replace('terminal', 'END\n')
        text = text.replace('mientras', 'WHILE')
        text = text.replace('do', 'DO')
        text = text.replace('definir', 'DEF')
        text = text.replace('clase', 'CLASS')
        text = text.replace('entero', 'INT')
        text = text.replace('flotante', 'FLT')
        text = text.replace('cadena', 'STR')
        text = text.replace('igual', '=')

        txtBox1.insert(END,text)

        
    except:
        print('No te pude escuchar')
    BuscarP(event=None)    

    

#Ventana y cosas
ventana = Tk()
ventana.geometry("1920x1080")
ventana.title("Compilador")
ventana.state('zoomed')
ventana.resizable(0,0) 
ventana.configure(background='#777777') 
ventana.grid_propagate(False)

menubar = Menu(ventana)
ventana.config(menu = menubar)

#Tamaño Letra
LetraSize=12

#FRAME
my_frame = Frame(ventana,width=1100,height=550)
my_frame.grid(column=0,row=1)
my_frame.pack_propagate(False)
frameBotones = Frame(ventana, width=50)
frameBotones.grid(column=2,row=3)
frameBotones.pack_propagate(True)
frameBotones.config(background='#777777')

#No. Lineas
txtNo = Text(my_frame,width = 2, height = 35)
txtNo.pack_propagate(False)
txtNo.pack(fill=BOTH, side=LEFT)
txtNo.insert(1.0, '1')

#Enumera las lineas del programa
def contarLineas(event):
    final_index = str(txtBox1.index(tk.END))
    num_of_lines = final_index.split('.')[0]
    line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
    txtNo.delete(1.0, tk.END)
    txtNo.insert(1.0, line_numbers_string)
    BuscarP(None)

#Pantalla
btnAnalizar = Button(frameBotones, text = "Analizar",command=analizar)
btnGuardar = Button(frameBotones, text = "Guardar")
btnSalir = Button(frameBotones, text = "Salir",command = ventana.quit)

btnAnalizar.grid(column=0,row=0, ipady = 3, pady = 5, padx = 5)
btnGuardar.grid(column=1,row=0, ipady = 3, pady = 5, padx = 5)
btnSalir.grid(column=2,row=0, ipady = 3, pady = 5, padx = 5, ipadx=10)

txtBox1 = ScrolledText(my_frame,width = 110, height = 35)
txtBox1.pack(fill=BOTH, side=LEFT)
myFont = tkFont.Font(family="Courier", size=LetraSize)
txtBox1.configure(font=myFont)
txtNo.configure(font=myFont)        


im = Frame(ventana,width=400,height=550)
im.grid(column=2,row=1)
im.pack_propagate(False)

lbl2 = Label(ventana, text = "Tokens: ")
lbl2.grid(column= 2, row = 0)
lbl2.configure(background='#777777')
txtBox2 = Text(im,width = 50, height = 22)
txtBox2.grid(column= 2, row = 1,padx=50)
txtBox2.configure(background='#adadad')
txtBox2.pack(side=TOP)


c = Label(im)


lbl3 = Label(ventana, text = "Terminal: ")
lbl3.grid(column= 0, row = 2)
lbl3.configure(background='#777777' )
txtBox3 = Text(width = 137, height = 13)
txtBox3.grid(column = 0, row = 3)
txtBox3.configure(background='#adadad')

#Aumenta o disminuye el tamaño de la fuente con el Scroll
def AumentarFuente(event):        
    global LetraSize
    if event.delta > 0: 
        LetraSize+=1
    else:
        LetraSize-=1
    myFont.configure(size=LetraSize)
    txtBox1.configure(font=myFont)
    txtNo.configure(font=myFont)

#===================== MENUS =======================
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo",command=file1)
filemenu.add_command(label="Abrir",command=openfile)
filemenu.add_command(label="Guardar",command=savefile)
filemenu.add_command(label="Guardar como...",command=savefileas)
filemenu.add_separator()
filemenu.add_command(label="Salir", command = ventana.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


voicemenu = Menu(menubar, tearoff=0)
voicemenu.add_command(label="Grabacion",command=Voz)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu = filemenu)
menubar.add_cascade(label="Editar", menu = editmenu)
menubar.add_cascade(label="Voz", menu = voicemenu)
menubar.add_cascade(label="Ayuda", menu = helpmenu)

#Activan los eventos para agrandar Letra, enumerar filas y colorear tokens
txtBox1.bind('<Return>',contarLineas)
txtBox1.bind('<Control-MouseWheel>',AumentarFuente)
txtBox1.bind('<Key-space>',BuscarP)

ventana.mainloop()