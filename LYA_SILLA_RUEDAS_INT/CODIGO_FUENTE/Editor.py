'''
#Importaciones
from threading import local
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from tkinter import filedialog
import lex
import re
import codecs
import os
import sys
from tkinter import *
import speech_recognition as sr

def limpiar1 ():
    txtBox1.delete('1.0', END)
    txtBox1.insert(END, '')
    limpiar2

def limpiar2 ():
    txtBox2.delete('1.0', END)
    txtBox2.insert(END, '')

#Colorzitos
def colorear(Palabra,color):
    contenido = txtBox1.get(1.0,'end-1c')
    contenido = contenido.upper()
    palabras = contenido.split()
    indiceInicial = "1.0"
    #tagFeak = 'feak'
    #CuatroFeak = 4
  
    i=0

    while i<len(palabras):
        
        if palabras[i] == Palabra:
            #Busca la palabra
            iniFeak = txtBox1.search(Palabra,index=indiceInicial ,stopindex='end',nocase=True,count=len(Palabra))
            inxFin = iniFeak + " + "+ str(len(Palabra)) +"c" 
            #Crear una etiqueta para el color 
            txtBox1.tag_add(Palabra+str(i),iniFeak,inxFin)
            txtBox1.tag_config(Palabra+str(i),foreground=color)
            indiceInicial=inxFin 

            l = locals()
            print(l)
        
        i+=1

def BuscarP(event):
    contenido = txtBox1.get(1.0,'end-1c')
    contenido = contenido.upper()
    palabras = contenido.split()
    #l = locals()
    #print(l)
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
            colorear(Palabra="INT",color="midnightblue")
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
#==========Guardar como=============
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
        print('Speak Anything : ')
        audio = r.listen(source)
 
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        txtBox1.insert('1.0',text)
        
    except:
        print('Sorry could not hear')
    BuscarP(event=None)    

    

#Ventana y cosas
ventana = Tk()
ventana.geometry("1920x1080")
ventana.title("Compilador")
ventana.state('zoomed')

menubar = Menu(ventana)
ventana.config(menu = menubar)

#Pantalla
lbl1 = Label(ventana, text = "Cadena a Analizar: ")
lbl1.grid(row = 0, column = 0)
txtBox1 = ScrolledText()
txtBox1.grid(row = 2, column = 0)

lbl2 = Label(ventana, text = "Tokens: ")
lbl2.grid(row = 3, column = 0)
txtBox2 = ScrolledText()
txtBox2.grid(row = 4, column = 0)

btn = Button(ventana, text = "Analizar Lexico")
btn.grid(column=1,row=2)

btn = Button(ventana, text = "Analizar Sintaxis")
btn.grid(column=1,row=3)


#Menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command = file1)
filemenu.add_command(label="Abrir", command = openfile)
filemenu.add_command(label="Guardar", command = savefile)
filemenu.add_command(label="Guardar como...", command = savefileas)
filemenu.add_separator()
filemenu.add_command(label="Salir", command = ventana.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

voicemenu = Menu(menubar, tearoff=0)
voicemenu.add_command(label="Grabacion",command= Voz)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu = filemenu)
menubar.add_cascade(label="Editar", menu = editmenu)
menubar.add_cascade(label="Voz", menu = voicemenu)
menubar.add_cascade(label="Ayuda", menu = helpmenu)

#Activan los eventos para colorear despues de un espacio o enter
txtBox1.bind('<Key-space>',BuscarP)
txtBox1.bind('<Return>',BuscarP)



ventana.mainloop()'''