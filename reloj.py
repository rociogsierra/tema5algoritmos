
import time
import os
import datetime

#PARA EJECUTARLO TENGO EN CUENTA:
#%a - Nombre del día de la semana
#%A - Nombre del día completo
#%b - Nombre abreviado del mes
#%B - Nombre completo del mes
#%c - Fecha y hora actual
#%d - Día del mes
#%H - Hora (formato 24 horas)
#%I - Hora (formato 12 horas)
#%j - Día del año
#%m - Mes en número
#%M- Minutos
#%p - Equivalente de AM o PM
#%S - Segundos
#%U - Semana del año (domingo como primer día de la semana)
#%w - Día de la semana
#%W - Semana del año (lunes como primer día de la semana)
#%x - Fecha actual
#%X - Hora actual
#%y - Número de año (14)
#%Y - Numero de año entero (2014)
#%Z - Zona horaria


#PRIMERA FORMA DE HACER EL EJERCICIO
ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
print(ahora.strftime("%d/%m/%Y, %H:%M:%S"))


#SEGUNDA FORMA DE HACER EL EJERCICIO
horario = datetime.now()
fecha = horario.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha)
#aquí añadiré "sleep" y "system", propuestos en el enunciado
time.sleep(secs = 4)
os.system("cls")


#TERCERA FORMA DE HACER EL EJERCICIO
x = datetime.datetime.now()
x.hour
x.minute
x.year
x.day
x.month
x.second

print("reloj de horas minutos y segundos: ")

print ("Hora = %s" %x.hour)
print ("Minutos = %s" %x.minute)
print ("Segundos =  %s" %x.second)
print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second))

#ejemplo de lo que devolverá esta función:
#Hora = 12
#Minutos = 10
#Segundos = 50

print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second))

#esta función devolverá lo mismo pero en otro formato
#ejemplo de lo que devolverá esta función:
#Formato hh:mm:ss = 12:10:50

#No lo pide el enunciado, pero añadiré año, mes y día para completar el ejercicio
print ("Año = %s" %x.year)
print ("Mes = %s" %x.month)
print ("Dia =  %s" %x.day)

#ejemplo de lo que devolverá esta función:
#Año = 2022
#Mes = 12
#Dia = 11


