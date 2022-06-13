#Importaciones
from ast import Global
from ctypes import alignment
from lib2to3.pgen2 import token
from threading import local
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog
import lex
import re
import codecs
import os
import sys
from tkinter import *
from turtle import width
import speech_recognition as sr

#Diccionario de palabras reservadas
reservadas =  [
    'IMPORT',
    'DEF',
    'CLASS',
    'IF',
    'ELSE',
    'FOR',
    'IN',
    'RANGE',
    'SELF',
    'WHILE',
    'TRY',
    'EXCEPT',
    'RETURN',
    'BREAK',
    'NEXT',

    'INPUT',
    'PRINT',
    'INT',
    'FLOAT',
    'BOOLEAN',
    'STRING',

    'POWER',
    'SQRT',
    'AND',
    'OR',
    'NOT',
    'BEGIN',
    'END'
]


#Lista de Tokens que usaran los metodos
        #Basicas
tokens = reservadas + ['ID', 'NUMERO','SUMA','ASIGNACION','RESTA','DIVISION','MULTIPLICACION',
         #Operadores 
          'IGUAL','DIFERENTE','MAYORQUE','MENORQUE','MAYORIGUALQUE','MENORIGUALQUE',
         #Separadores 
          'PUNTO','COMA','DOSPUNTOS','PUNTOCOMA','COMILLASIMPLE','COMILLADOBLE','PARENTESISABIERTO',
          'PARENTESISCERRADO','LLAVEABIERTO','LLAVECERRADO','CORCHETEABIERTO','CORCHETECERRADO','ESPACIO',
         #Pasos
          'INCREMENTO','DECREMENTO']
          

t_ignore = '\t'

#Operadores matematicos
t_SUMA = r'\+'
t_ASIGNACION = r'='
t_RESTA = r'\-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'

#Operadores
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='

t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
t_PUNTOCOMA = r'\;'
t_COMILLASIMPLE = r'\''
t_COMILLADOBLE = r'\"'
t_PARENTESISABIERTO = r'\('
t_PARENTESISCERRADO = r'\)'
t_LLAVEABIERTO = r'\{'
t_LLAVECERRADO = r'\}'
t_CORCHETEABIERTO = r'\['
t_CORCHETECERRADO = r'\]'
#t_ESPACIO = r'\s'

t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_error(t):
    t.value = t.value[0]
    t.lexer.skip(1)
    pass

a = []
b = []
s = []
def analiza(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    a.clear()
    b.clear()
    s.clear()
    while True:
        tok = analizador.token()
        if not tok : break
        b.append(tok)
        a.append(str(tok))
    return a

def analizaar():
    concatena = ""
    cadena = ''
    cadena = txtBox1.get(1.0, "end-1c")
    analiza(cadena)
    for i in a:
        concatena += i + '\n'
    txtBox2.delete('1.0', END)
    txtBox2.insert(END, concatena)
    BuscarS()
    concatena=""
    
    for i in s:
        concatena += i + '\n'
    txtBox3.delete('1.0', END)
    txtBox3.insert(END, concatena)
    if(concatena == ""):
        txtBox3.insert(END, 'Completado Exitosamente')
        
def BuscarS():
    #l = locals()
    #print(l)
    i=0
    while i<len(b):
        if b[i].type == "INT" or b[i].type == "INT":
            #try:
                gINT(b,i)
            #except:
                #print('Error: No hay continuacion del programa, se esparaba: ID | Linea:'+str(b[i].lineno))    
        i+=1     

def gINT(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            s.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return  
    else: 
        s.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return        
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsign(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            s.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))   
    else: 
        s.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
 # int a; 3
 # int a = 3; 5
def gAsign(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            s.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return  
    else:
        s.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return
    if(len(t)>i+2):
        if(t[i+2].type != 'PUNTOCOMA'):
            s.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))   
    else: 
        s.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))     
    

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

            #l = locals()
            #print(l)
        
        i+=1


#=======================COLOREAR=======================
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
#===============0=========Guardar como==========================
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
ventana.geometry("1366x768")
ventana.title("Compilador")
ventana.state('zoomed')
ventana.resizable(0,0) 
ventana.configure(background='#777777') 

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
txtNo.pack(fill=BOTH, side=LEFT)
txtNo.insert(1.0, '1')

def contarLineas(event):
    final_index = str(txtBox1.index(tk.END))
    num_of_lines = final_index.split('.')[0]
    line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
    txtNo.delete(1.0, tk.END)
    txtNo.insert(1.0, line_numbers_string)

#Pantalla
btnAnalizar = Button(frameBotones, text = "Analizar",command=analizaar)
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


lbl2 = Label(ventana, text = "Tokens: ")
lbl2.grid(column= 2, row = 0)
lbl2.configure(background='#777777')
txtBox2 = Text(width = 40, height = 34)
txtBox2.grid(column= 2, row = 1,padx=50)
txtBox2.configure(background='#adadad')

lbl3 = Label(ventana, text = "Terminal: ")
lbl3.grid(column= 0, row = 2)
lbl3.configure(background='#777777' )
txtBox3 = Text(width = 137, height = 13)
txtBox3.grid(column = 0, row = 3)
txtBox3.configure(background='#adadad')


def AumentarFuente(event):        
    global LetraSize
    if event.delta > 0: 
        LetraSize+=1
    else:
        LetraSize-=1
    myFont.configure(size=LetraSize)
    txtBox1.configure(font=myFont)
    txtNo.configure(font=myFont)

#Menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Guardar como...")
filemenu.add_separator()
filemenu.add_command(label="Salir", command = ventana.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
editmenu.add_command(label="Tamaño fuente")

voicemenu = Menu(menubar, tearoff=0)
voicemenu.add_command(label="Grabacion",)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu = filemenu)
menubar.add_cascade(label="Editar", menu = editmenu)
menubar.add_cascade(label="Voz", menu = voicemenu)
menubar.add_cascade(label="Ayuda", menu = helpmenu)

#Activan los eventos para agrandar Letra y enumerar filas
txtBox1.bind('<Return>',contarLineas)
txtBox1.bind('<MouseWheel>',AumentarFuente)

#Activan los eventos para colorear despues de un espacio o enter
txtBox1.bind('<Key-space>',BuscarP)
txtBox1.bind('<Return>',BuscarP)

ventana.mainloop()
