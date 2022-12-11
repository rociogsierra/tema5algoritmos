
import sys

#trabajar sobre el fichero contador.txt
#si el fichero no existe o está vacío lo crearemos con el número 0
#si existe simplemente leeremos el valor del contador.

fichero = open("contador.txt", "a+")
fichero.seek(0)
argumentos = fichero.readline()

if len(argumentos) == 0:
    argumentos = "0"
    fichero.write(argumentos)
fichero.close()

#a partir de un argumento:
#si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla
#si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla
#si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla

try:
    contador = int(argumentos)
    if len(sys.argv) == 2:
        
        if sys.argv[1] == "inc":
            contador = contador + 1
        
        elif sys.argv[1] == "dec":
            contador = contador - 1
    
    print(contador)

    fichero = open("contador.txt", "w")
    fichero.write(str(contador))
    fichero.close()

#utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.

except:
    print("Error: Fichero corrupto")





