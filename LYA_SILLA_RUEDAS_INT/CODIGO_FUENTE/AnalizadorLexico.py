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
    'TRUE',
    'FALSE',

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

def analiza(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    a.clear()
    b.clear()
    while True:
        tok = analizador.token()
        if not tok : break
        b.append(tok)
        a.append(str(tok))
    return a

def analizaar(txtPrincipal,txtTokens):
    concatena = ""
    cadena = ''
    cadena = txtPrincipal.get(1.0, "end-1c")
    analiza(cadena)
    for i in a:
        concatena += i + '\n'
    txtTokens.delete('1.0', END)
    txtTokens.insert(END, concatena)

    concatena=""
    
    '''
    for i in s:
        concatena += i + '\n'
    txtBox3.delete('1.0', END)
    txtBox3.insert(END, concatena)
    if(concatena == ""):
        txtBox3.insert(END, 'Completado Exitosamente')
    
    '''