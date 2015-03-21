# -*- coding: cp1252 -*-
import glob
import numpy
import string

def textos(path):
    # listar todos los ficheros con extensión .txt del directorio path:
    filelist = glob.glob(path)
    docs = []

    # bucle sobre todos los ficheros en el directorio:
    for kfile in filelist:   
        fp = file(kfile) # abrir fichero
        txt = fp.read() # leer fichero
        fp.close() # cerrar fichero
        
        # filtrar caracteres: 
        txt = txt.lower() # convertir a minusculas
        # substituir retornos de carro por espacios
        txt = txt.replace('\n',' ')
        # borrar caracteres ASCII que no sean el espacio
        #(ascii 32), o las letras a-z (ascii 97-122):
        char_ok = [32] + range(97,122)
        for i in range(256):
            if i not in char_ok:
                txt = txt.replace(chr(i),'')
                
        # construir una lista con las palabras del texto:
        palabras = txt.split()
        # crear un diccionario:
        dicc = { }
        for ipal in range(len(palabras)):
            pl = palabras[ipal];       
            if len(pl)>4: # excluir palabras de menos de 5 caracteres
                if pl in dicc:
                    dicc[pl].append(ipal) # localización de las apariciones
                else:
                    dicc[pl] = [ipal]
        # añadir número de apariciones al final del diccionario
        for ipal in range(len(palabras)):
            pl = palabras[ipal];
            if pl in dicc:
                #dicc[pl].append(len(dicc[pl])) # número de apariciones
                dicc[pl].insert(0,len(dicc[pl]))
        # agregar diccionario de cada documento           
        docs.append(dicc)        

    return docs

    

    





