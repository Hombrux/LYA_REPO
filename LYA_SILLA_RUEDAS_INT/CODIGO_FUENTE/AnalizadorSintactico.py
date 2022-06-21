#Arreglo donde se almacenan los errores
Errores = []

#========================= Buscar entre los tokens ======================
def BuscarS(tokens):
    global llavesFaltantes
    llavesFaltantes = 0
    #Limpiar el arreglo de errores
    Errores.clear()

    i=0
    while i<len(tokens):
        if tokens[i].type == "INT":
            gINT(tokens,i)
        if tokens[i].type == "FLOAT":
            gFLOAT(tokens,i)
        if tokens[i].type == "BOOLEAN":
            gBOOLEAN(tokens,i)
        if tokens[i].type == "STRING":
            gSTRING(tokens,i)
        if tokens[i].type == "IF":
            gIF(tokens,i)
        if tokens[i].type == "WHILE":
            gWHILE(tokens,i)
        if tokens[i].type == "FOR":
            gFOR(tokens,i)
        if tokens[i].type == "DEF":
            gDEF(tokens,i)
        if tokens[i].type == "CLASS":
            gCLASS(tokens,i)
        if tokens[i].type == "POWER":
            gPOWER(tokens,i)
        if tokens[i].type == "SQRT":
            gSQRT(tokens,i)
        if tokens[i].type == "MULTIPLICACION":
            gAritmeticos(tokens,i)
        if tokens[i].type == "DIVISION":
            gAritmeticos(tokens,i)
        if tokens[i].type == "SUMA":
            gAritmeticos(tokens,i)
        if tokens[i].type == "RESTA":
            gAritmeticos(tokens,i)

        if tokens[i].type == "LLAVECERRADO":
           llavesFaltantes-=1
        i+=1

    #despues del ciclo, revisa que no falten o sobren llaves
    if llavesFaltantes>0 and (not Errores):
        Errores.append('Faltaron '+str(llavesFaltantes)+' llaves de cerradura.')
    if llavesFaltantes<0 and (not Errores):
        Errores.append('Sobran '+str(abs(llavesFaltantes))+' llaves de cerradura.')

#======================OPERADORES ARITMETICOS=========================
def gAritmeticos(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataARITMETICOS.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataARITMETICOS.png')
        return

#========================== Declarar INT ==========================
def gINT(t,i):
    #Cantidad de elementos len(t)
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataINT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataINT.png')
        return
    #Se cumplio la primera condicion ->
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsign(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataINT.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataINT.png')
 # int a; 3
 # int a = 3; 5

#============================ Asignacion ===================================
def gAsign(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataINT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataINT.png')
        return

    if(len(t)>i+2):
        if(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataINT.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataINT.png')
# a=5
# a=b


 #========================== Declarar BOOLEAN ==========================
def gBOOLEAN(t,i):
    #Cantidad de elementos len(t)
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataBOOLEAN.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataBOOLEAN.png')
        return
    #Se cumplio la primera condicion ->
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsignBOOLEAN(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataBOOLEAN.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataBOOLEAN.png')
 # boolean a = FALSE;
 # boolean a = TRUE;
 # boolean a;


 #========================== Declarar FLOAT ==========================
def gFLOAT(t,i):
    #Cantidad de elementos len(t)
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFLOAT.png')
        return
    #Se cumplio la primera condicion ->
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsignFLOAT(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataFLOAT.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataFLOAT.png')
 # float a; 3.1
 # float a = 3.4; 5.2
 # float a = .5

  #========================== Declarar STRING ==========================
def gSTRING(t,i):
    #Cantidad de elementos len(t)
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataSTRING.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataSTRING.png')
        return
    #Se cumplio la primera condicion ->
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsignSTRING(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataSTRING.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataSTRING.png')
 #STRING A = "AAGRIA";


#============================ AsignacionBOOLEAN ===================================
def gAsignBOOLEAN(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'TRUE') and (t[i+1].type != 'FALSE')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: TRUE o FALSE | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataBOOLEAN.jpg')
            return
    else:
        Errores.append('Error: se espera un tipo de token: TRUE o FALSE | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataBOOLEAN.png')
        return
    if(len(t)>i+2):
        if(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataBOOLEAN.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataBOOLEAN.png')


#============================ AsignacionSTRING ===================================
def gAsignSTRING(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'COMILLADOBLE')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: COMILLADOBLE | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataSTRING.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: COMILLADOBLE | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataSTRING.png')
        return

    if(len(t)>i+2):
        if(t[i+2].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataSTRING.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataSTRING.png')
        return

    if(len(t)>i+3):
        if(t[i+3].type != 'COMILLADOBLE'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: COMILLADOBLE | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataSTRING.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: COMILLADOBLE | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataSTRING.png')
        return

    if(len(t)>i+4):
        if(t[i+4].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+4].lexpos))
            Errores.append('AutomataSTRING.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataSTRING.png')



#============================ AsignacionFLOAT ===================================
def gAsignFLOAT(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO') and (t[i+1].type != 'PUNTO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO o PUNTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO o PUNTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFLOAT.png')
        return

    #El caso si el primer token es un PUNTO
    if(t[i+1].type == 'PUNTO'):
        if(len(t)>i+2):
            if(t[i+2].type != 'NUMERO'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: NUMERO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
                Errores.append('AutomataFLOAT.png')
                return
        else:
            Errores.append('Error: se espera un tipo de token: NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
            return

        if(len(t)>i+3):
            if(t[i+3].type != 'PUNTOCOMA'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o NUMERO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
                Errores.append('AutomataFLOAT.png')
        else:
            Errores.append('Error: se espera un tipo de token: ; o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
    #El caso si el primer token es un ID
    if(t[i+1].type == 'ID'):
        if(len(t)>i+2):
            if(t[i+2].type != 'PUNTOCOMA'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
                Errores.append('AutomataFLOAT.png')
        else:
            Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
    #El caso si el primer token es un NUMERO
    if(t[i+1].type == 'NUMERO'):
        if(len(t)>i+2):
            if(t[i+2].type != 'PUNTO'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: PUNTO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
                Errores.append('AutomataFLOAT.png')
                return
        else:
            Errores.append('Error: se espera un tipo de token: PUNTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
            return

        if(len(t)>i+3):
            if(t[i+3].type != 'NUMERO'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: NUMERO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
                Errores.append('AutomataFLOAT.png')
                return
        else:
            Errores.append('Error: se espera un tipo de token: NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')
            return

        if(len(t)>i+4):
            if(t[i+4].type != 'PUNTOCOMA'):
                Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o NUMERO | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+4].lexpos))
                Errores.append('AutomataFLOAT.png')
        else:
            Errores.append('Error: se espera un tipo de token: ; o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFLOAT.png')

#==============================condicion if===============================
def gIF(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'PARENTESISABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: PARENTESISABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataIF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataIF.png')
        return

    i = Condicion(t,i+1)
    if(i == 0):
        return

    if(len(t)>i):
        if(t[i].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataIF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ) PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataIF.png')
    if(len(t)>i+1):
        if(t[i+1].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataIF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataIF.png')

    global llavesFaltantes
    llavesFaltantes+=1

#funcion reutilizable para cualquier tipo de condicion la cual es recursiva y retorna un 0 si la sintaxis de la condicion esta mal
# y si esta bien la sintaxis retorn el valos de la pisicion en donde termino la condicion del arreglo de tokens
def Condicion(t,i):
    i2=0
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba un tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataCONDICION.png')
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataCONDICION.png')
        return 0

    if(len(t)>i+2):
        if((t[i+2].type != 'IGUAL') and (t[i+2].type != 'DIFERENTE') and (t[i+2].type != 'MAYORQUE') and (t[i+2].type != 'MENORQUE') and (t[i+2].type != 'MAYORIGUALQUE') and (t[i+2].type != 'MENORIGUALQUE') and (t[i+2].type != 'IGUAL')):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba un operador de comparacion:  | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataCONDICION.png')
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: de COMPARACION (<,>,!=,==,<=,>=) | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataCONDICION.png')
        return 0

    if(len(t)>i+3):
        if((t[i+3].type != 'ID') and (t[i+3].type != 'NUMERO') and (t[i+3].type != 'FALSE') and (t[i+3].type != 'TRUE')):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+' '+str(t[i+3].type)+', se esperaba un tipo de token: ID, NUMERO o VALOR BOOLEANO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataCONDICION.png')
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: ID, NUMERO o VALOR BOOLEANO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
        Errores.append('AutomataCONDICION.png')
        return 0

    if(len(t)>i+4):
        if(t[i+4].type == 'AND' or t[i+4].type == 'OR' or t[i+4].type == 'NOT'):
            i2 = Condicion(t,i+4)
            return i2
        '''
        if(t[i+4].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i+4].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+4].lexpos))
            return 0'''

        return i+4
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISCERRADO ")" u OPERADOR LOGICO (AND, OR, NOT)| Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
        Errores.append('AutomataCONDICION.png')
        return 0


#=====================================CICLO DE REPETICION WHILE===========================================
def gWHILE(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'PARENTESISABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: PARENTESISABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataWHILE.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataWHILE.png')
        return

    i = Condicion(t,i+1)
    if(i == 0):
        return

    if(len(t)>i):
        if(t[i].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataWHILE.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ) PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataWHILE.png')
    if(len(t)>i+1):
        if(t[i+1].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataWHILE.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataWHILE.png')
    global llavesFaltantes
    llavesFaltantes+=1

#=====================================CICLO DE REPETICION FOR===========================================
def gFOR(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'PARENTESISABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: PARENTESISABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "("--- | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFOR.png')
        return
    #================================analisis de la declaracion de la variable  para el for==========================================================
    #Cantidad de elementos len(t)
    if(len(t)>i+2):
        if(t[i+2].type != 'INT'):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba otro tipo de token: INT | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: INT | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataFOR.png')
        return

    if(len(t)>i+3):
        if(t[i+3].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataFOR.png')
        return
    #Se cumplio la primera condicion ->
    if(len(t)>i+4):
        m=i+4
        if(t[i+4].type == 'ASIGNACION'):
            i = gAsignFOR(t,i+4)
            if(i==0):
                return
        elif(t[i+4].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+4].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
        Errores.append('AutomataFOR.png')
        return
    #==========================================================================================================================================
    if(m==(i+4)):
        i = Condicion(t,i+4)
    else:
        i = Condicion(t,i)
    if(i == 0):
        print('DIO 0')
        return

    if(len(t)>i):
        if(t[i].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i].value)+', se esperaba un tipo de token: PUNTOCOMA ";" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ";" PUNTOCOMA | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFOR.png')
        return

    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFOR.png')
        return

    if(len(t)>i+2):
        if(t[i+2].type != 'INCREMENTO' and t[i+2].type != 'DECREMENTO'):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba un tipo de token: INCREMENTO o DECREMENTO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: INCREMENTO o DECREMENTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataFOR.png')
        return

    if(len(t)>i+3):
        if(t[i+3].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
        Errores.append('AutomataFOR.png')
        return

    if(len(t)>i+4):
        if(t[i+4].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+4].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+4].lexpos))
            Errores.append('AutomataFOR.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
        Errores.append('AutomataFOR.png')
        return

    global llavesFaltantes
    llavesFaltantes+=1


#============================ Asignacion FOR===================================
def gAsignFOR(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataFOR.png')
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataFOR.png')
        return 0

    if(len(t)>i+2):
        if(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataFOR.png')
    else:
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataFOR.png')
        return 0
    return i+2
# a=5

#función recursiva para parámetros, similar a la de condición
def Parametro(t,i):
    if(len(t)>i+1):
        if((t[i+1].type == 'PARENTESISCERRADO')):
            return i+1
    i2 = 0
    if(len(t)>i+1):
        if((t[i+1].type != 'ID')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataDEF.png')
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataDEF.png')
        return 0
    if(len(t)>i+2):
        if(t[i+2].type == 'COMA'):
            if(len(t)>i+3):
                if(t[i+3].type != 'ID'):
                    Errores.append('Token Inesperado:'+str(t[i+3].value)+' '+str(t[i+3].type)+', se esperaba un tipo de token: ID | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
                    Errores.append('AutomataDEF.png')
            i2 = Parametro(t,i+2)
            return i2

        return i+2
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISCERRADO ")" o COMA ","| Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
        Errores.append('AutomataDEF.png')
        return 0

#======================= DEF (declaracion funciones) ========================
def gDEF(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataDEF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataDEF.png')
        return

    if(len(t)>i+2):
        if(t[i+2].type != 'PARENTESISABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: PARENTESISABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataDEF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataDEF.png')
        return

    i = Parametro(t,i+2)
    if(i == 0):
        return

    if(len(t)>i):
        if(t[i].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataDEF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ) PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataDEF.png')
    if(len(t)>i+1):
        if(t[i+1].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataDEF.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataDEF.png')
    global llavesFaltantes
    llavesFaltantes+=1

#======================= CLASS ========================
def gCLASS(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataCLASS.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataCLASS.png')
        return


    if(len(t)>i+2):
        if(t[i+2].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataCLASS.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataCLASS.png')
    global llavesFaltantes
    llavesFaltantes+=1
#======================= POWER (POTENCIA X^Y) ========================
def gPOWER(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'PARENTESISABIERTO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataPOWER.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataPOWER.png')
        return
    if(len(t)>i+2):
        if((t[i+2].type != 'ID') and (t[i+2].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+' '+str(t[i+2].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataPOWER.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataPOWER.png')
        return

    if(len(t)>i+3):
        if((t[i+3].type != 'COMA')):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+' '+str(t[i+3].type)+', se esperaba otro tipo de token: COMA | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataPOWER.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: COMA | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataPOWER.png')
        return
    if(len(t)>i+4):
        if((t[i+4].type != 'ID') and (t[i+4].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+4].value)+' '+str(t[i+4].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+4].lineno) +' Columna:'+str(t[i+4].lexpos))
            Errores.append('AutomataPOWER.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataPOWER.png')
        return

    if(len(t)>i+5):
        if((t[i+5].type != 'PARENTESISCERRADO')):
            Errores.append('Token Inesperado:'+str(t[i+5].value)+' '+str(t[i+5].type)+', se esperaba otro tipo de token: PARENTESISCERRADO ")" | Linea:'+str(t[i+5].lineno) +' Columna:'+str(t[i+5].lexpos))
            Errores.append('AutomataPOWER.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISCERRADO ")" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataPOWER.png')
#================= raiz cuadrada =================
def gSQRT(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'PARENTESISABIERTO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('AutomataSQRT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataSQRT.png')
        return
    if(len(t)>i+2):
        if((t[i+2].type != 'ID') and (t[i+2].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+' '+str(t[i+2].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            Errores.append('AutomataSQRT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataSQRT.png')
        return

    if(len(t)>i+3):
        if((t[i+3].type != 'PARENTESISCERRADO')):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+' '+str(t[i+3].type)+', se esperaba otro tipo de token: PARENTESISCERRADO ")" | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            Errores.append('AutomataSQRT.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: PARENTESISCERRADO ")" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('AutomataSQRT.png')

#================= INCREMENTO / DECREMENTO =================
def gIncDec(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            Errores.append('feakpelon.png')
            return
    else:
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        Errores.append('feakpelon.png')
        return