# Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

# Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

# Ejemplo:

#     Mensaje que se muestra: ¿En qué número estás pensando?
#     Entrada: 25
#     Salida: ¡Es un número impar! ¿Puedes añadir otro?

print("Binevenido a el progrma para adivinar un numero secreto \n")

#recuerda apagar la consola en cada prueba

while  True:
    numero=  input("Ingrese un numero secreto del 1 al 100") 
    print(type(numero))
    try:
        numero=int(numero)
        
    except:
        print("No ingrese letras o decimales")
        continue;
        
    print(type(numero))
    if (numero> 0 and numero<100):
        break;
    else:
        print("Rango del 1 al 100 unicamente")

adivinanza =0
intentos=3
while True:
    print("adivina el numero secreto")
    adivinanza=input()
    try: 
        
        adivinanza=int(adivinanza)
        
        if(adivinanza==numero):
            print("Felizidades haz decifrado el numero oculto, Ganastes ")
            break;
        elif (adivinanza<numero):
            print("El numero es mayor ")
        elif (adivinanza>numero):
            print("elnumero es menor ")
        else:
            print("no deberias poder ver este mensaje")    
        
        intentos=intentos-1;
        print("te quedan "+str(intentos)+" intenos")
        
        if(intentos<= 0):
            print("Perdites")
            break;
            
    except:
        print("introduce valores validos")

print("Fin del programa")   