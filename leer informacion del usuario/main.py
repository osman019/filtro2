import json 
import modules.corefile as cf
title =  """
**********************************
* GUARDAR INFORMACION DE USUARIOS* 
**********************************
"""
print(title)
id= input("ingrese el id del usuario: ")
nombres = input("ingrese los nombres: ")
apellidos = input("ingrese apellidos: ")
ubicación = input("ingrese la ubicacion: ")
dirección = input("ingrese la direccion:")
ciudad = input("ingrese la ciudad:")
longitud = input("ingrese londitud: ")
latitud=input("ingrese latitud: ")
email=input("ingrese su correo: ")
edad=input("ingrese su edad:")
ocupación=input("ingrese su ocupacion: ")

cf.AddData('data')
