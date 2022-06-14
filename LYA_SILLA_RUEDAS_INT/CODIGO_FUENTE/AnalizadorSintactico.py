#Arreglo donde se almacenan los errores
Errores = []

#========================= Buscar entre los tokens ======================
def BuscarS(tokens):
    
    #Limpiar el arreglo de errores
    Errores.clear()
    
    i=0
    while i<len(tokens):
        
        if tokens[i].type == "INT":
            gINT(tokens,i)
        if tokens[i].type == "IF":
            gIF(tokens,i)  
        i+=1     

#========================== Declarar INT ==========================
def gINT(t,i):
    #Cantidad de elementos len(t)
    if(len(t)>i+1):
        if(t[i+1].type != 'ID'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ID | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return  
    else: 
        Errores.append('Error: se espera un tipo de token: ID | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return
    #Se cumplio la primera condicion ->            
    if(len(t)>i+2):
        if(t[i+2].type == 'ASIGNACION'):
            gAsign(t,i+2)
        elif(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; o = | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))   
    else: 
        Errores.append('Error: se espera un tipo de token: ; o = | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
 # int a; 3
 # int a = 3; 5

#============================ Asignacion ===================================
def gAsign(t,i):
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba otro tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return  
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return
        
    if(len(t)>i+2):
        if(t[i+2].type != 'PUNTOCOMA'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba otro tipo de token: ; | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))   
    else: 
        Errores.append('Error: se espera un tipo de token: ; | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))     
# a=5
# a=b

#==============================condicion if===============================
def gIF(t,i):
    if(len(t)>i+1):
        if(t[i+1].type != 'PARENTESISABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: PARENTESISABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return  
    else: 
        Errores.append('Error: se espera un tipo de token: PARENTESISABIERTO "(" | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return
    
    i = Condicion(t,i+1)
    if(i == 0):
        return
    
    if(len(t)>i):
        if(t[i].type != 'PARENTESISCERRADO'):
            Errores.append('Token Inesperado:'+str(t[i].value)+', se esperaba un tipo de token: PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i+1].lexpos))
            return
    else: 
        Errores.append('Error: se espera un tipo de token: ) PARENTESISCERRADO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))

    if(len(t)>i+1):
        if(t[i+1].type != 'LLAVEABIERTO'):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+', se esperaba un tipo de token: LLAVEABIERTO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return
    else: 
        Errores.append('Error: se espera un tipo de token: LLAVEABIERTO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
    
    if(len(t)>i+2):
        if(t[i+2].type != 'LLAVECERRADO'):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba un tipo de token: LLAVECERRADO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
            return
    else: 
        Errores.append('Error: se espera un tipo de token: LLAVECERRADO| Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))


#funcion reutilizable para cualquier tipo de condicion la cual es recursiva y retorna un 0 si la sintaxis de la condicion esta mal 
# y si esta bien la sintaxis retorn el valos de la pisicion en donde termino la condicion del arreglo de tokens
def Condicion(t,i):
    i2=0
    if(len(t)>i+1):
        if((t[i+1].type != 'ID') and (t[i+1].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+1].value)+' '+str(t[i+1].type)+', se esperaba un tipo de token: ID o NUMERO | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))
            return 0
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i].lineno) +' Columna:'+str(t[i].lexpos))
        return 0
        
    if(len(t)>i+2):
        if((t[i+2].type != 'IGUAL') and (t[i+2].type != 'DIFERENTE') and (t[i+2].type != 'MAYORQUE') and (t[i+2].type != 'MENORQUE') and (t[i+2].type != 'MAYORIGUALQUE') and (t[i+2].type != 'MENORIGUALQUE') and (t[i+2].type != 'IGUAL')):
            Errores.append('Token Inesperado:'+str(t[i+2].value)+', se esperaba un operador de comparacion:  | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))   
            return 0
    else: 
        Errores.append('Error: se espera un tipo de token: de COMPARACION (<,>,!=,==,<=,>=) | Linea:'+str(t[i+1].lineno) +' Columna:'+str(t[i+1].lexpos))   
        return 0  

    if(len(t)>i+3):
        if((t[i+3].type != 'ID') and (t[i+3].type != 'NUMERO')):
            Errores.append('Token Inesperado:'+str(t[i+3].value)+' '+str(t[i+3].type)+', se esperaba un tipo de token: ID o NUMERO | Linea:'+str(t[i+3].lineno) +' Columna:'+str(t[i+3].lexpos))
            return 0 
    else:
        Errores.append('Error: se espera un tipo de token: ID o NUMERO | Linea:'+str(t[i+2].lineno) +' Columna:'+str(t[i+2].lexpos))
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
        return 0
      