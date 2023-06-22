#saber la version de python instalada
import sys
print(sys.version)
print(sys.version_info)

# sys.version_info(major=3, minor=10, micro=6, releaselevel='final', serial=0)
# camios semanticos cambios minos o relevnate de las versiones

#Ejercicio 2 Jugando con los strings
print ("hola mundo")
print("Hola mundo como estan",end="")
print("OhnoEstoyPEgado",end="")
print("Hola","mundo","pero con rayitas, bueno este ultimo string no","XD",sep="-")
print()

numero=1
numero0=2
print("si sumamos {} con {} tenemos".format(numero0, numero),"suma",numero+numero0)

print(f"si sumamos {numero} con {numero0} tenemos {numero0 + numero} lo mismo pero de otra forma"+" adjunto extra")

print()
lista_simple = [2,3,5,6,78,89,1000]
print(numero, f"format F {lista_simple} " )

diccionario={"valor1":2,"valor2":7,"valor3":5}

print(diccionario)

#progrmaa para saber la hora actual
import datetime
tiempo_ahora= datetime.datetime.now()
print(tiempo_ahora)
print(type(tiempo_ahora))
print(tiempo_ahora.strftime("%d %m %Y %H:%M:%S"))



