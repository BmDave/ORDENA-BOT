import os #importar el modulo OS (sistema operativo), para manejar archivos.
import shutil #importar el modulo shutil para manejar archivos de alta calidad.

FolderA = '' #dirección actual de la carpeta

FolderD = ''#dirección a enviar.

ExtentionSearch = ''#La extención del archivo 

if __name__ == '__main__': #condicional principal

    def confirm_path (pathSearch, comments): #función de validación de ruta
        while True:
            pathSearch = input(comments)
            confirm = os.path.isdir(pathSearch) #la método os.path.isdir devuelve un valor bool

            if confirm: #Se comprueba que existen las direcciones
                return pathSearch #devuelve la variable
                break
            else:
                print("Error, revise la dirección de los archivos. \n") 
         
    def Search_file (ext,ext_current,fileA,source,destinetion):
        #Se comprueba la extención del archivo
        if ext in ext_current:
            #para evitar errores    
            try:
                #con el shutil.move, movemos los archivos a otra dirección
                shutil.move(source +  fileA, destinetion) # (la ruta con el archivo incluido la extencion / el destino)
                print("Archivo: "+ fileA)
            except PermissionError:
                print("Uno de los archivos tiene problemas.\n")
        elif  ext not in ext_current: #Si no es igual a la extención
            pass
        else: #Errores grandes
            print("No se puedo ejecutar el programa.\n")

    def ext_sintaxis (ext):#verificar la extención del archivo
        while True:
            #Se llama un input
            ext = input('Ingrese un extensión (ejemplo ".pdf"): ')
            try:
                if ext[0] == "." and len(ext) == 4:
                    return ext
                    break
                else: 
                    print("Uno de los archivos tiene problemas.\n")
            except IndexError:
                ext = input('Ingrese un extensión (ejemplo ".pdf"): ')

    print("ORDENA-BOT\n")
    ExtentionSearch = ext_sintaxis(ExtentionSearch)#se llama la función

    #Se llama la función y un comentario
    FolderA = confirm_path(FolderA, 'Ingrese la ruta actual de la carpeta según el ejemplo ("C:/Users/carpeta/"): ')
    FolderD = confirm_path(FolderD, 'Ingrese la ruta de destino de la carpeta según el ejemplo ("C:/Users/carpeta/"): ')
    
    with os.scandir(FolderA) as AllDir: #con el with hacemos el método más corta
        AllDir = [filedir.name for filedir in AllDir if filedir.is_file()]
        #Con AllDir resuminos el For y el if
    #Bucle para revisar todos los archivos de una carpeta

    for filename in AllDir:
        #Guardar la dirección de todos los archivos de la carpeta
        name, extention = os.path.splitext(FolderA + filename)
        #Se llama una función
        Search_file (extention,ExtentionSearch,filename,FolderA,FolderD)


    print("\n Proceso terminado.")   