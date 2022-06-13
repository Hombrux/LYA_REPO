#Arreglo donde se almacenan los errores
Errores = []

#========================= Buscar entre los tokens ======================
def BuscarS(tokens):
    #l = locals()
    #print(l)
    #Limpiar el arreglo de errores
    Errores.clear()
    
    i=0
    while i<len(tokens):
        
        if tokens[i].type == "INT":
            gINT(tokens,i)
          
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

  