from cryptography.fernet import Fernet
from tkinter import ttk
import tkinter as tk
import os,sys
from tkinter import filedialog as fd

def clave():
    key_gen = Fernet.generate_key()
    nombrearch = fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("key files","*.key"),("todos los archivos","*")))
    nombrearch += ".key"
    with open(nombrearch,"wb") as archivo_key:
        archivo_key.write(key_gen)

def cargarCLAVE():
    # Permite al usuario seleccionar un archivo de clave y carga la clave
    archivo_key=fd.askopenfilename(initialdir = "/",title = "Seleccione la key",filetypes = (("key files","*.key"),("todos los archivos","*")))
    key = open(archivo_key,"rb").read()
    return key

def encriptarARCHIVO():
    # Permite al usuario seleccionar un archivo y lo encripta usando la clave proporcionada
    key = cargarCLAVE()
    nom_archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    f = Fernet(key)
    with open(nom_archivo,"rb") as archivo:
        data = archivo.read()
        data_encriptada = f.encrypt(data)

    nombre = nom_archivo + "_encrypted" + ".txt"

    i = 1
    while os.path.isfile(nombre):
        nombre = f"{nom_archivo}_encrypted({i}).txt"
        i += 1
    


    with open(nombre,"wb") as archivo:
        archivo.write(data_encriptada)

def des_encriptarARCHIVO():
    # Permite al usuario seleccionar un archivo encriptado y lo desencripta usando la clave proporcionada
    key = cargarCLAVE()
    nom_archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    f = Fernet(key)
    with open(nom_archivo,"rb") as archivo:
        data = archivo.read()
        data_desencriptada = f.decrypt(data).decode()

    nombre = nom_archivo + "_decrypted" + ".txt"

    i = 1
    while os.path.isfile(nombre):
        nombre = f"{nom_archivo}_decrypted({i}).txt"
        i += 1

    with open(nombre,"w") as archivo:
        archivo.write(data_desencriptada)

    

window = tk.Tk()
window.title("Encriptador")
window.geometry("300x150")

btngenerar = tk.Button(text="Generar clave", command=clave)
btncodificar = tk.Button(text="Seleccione Archivo a codificar", command=encriptarARCHIVO)
btndecodificar = tk.Button(text="Seleccione Archivo a decodificar", command=des_encriptarARCHIVO)
btngenerar.pack(pady=5)
btncodificar.pack(pady=5)
btndecodificar.pack(pady=5)

window.mainloop()