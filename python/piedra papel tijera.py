#piedra papel tijera
#random 0-2  
import random
print("Programa piedra papel tijera vs cpu")

#Respuesta = input("Ingresa 1.piedra 2.papel 3. tijera")
variable=["piedra","papel","tijera"] 


while True:
   # print("a")
    try:
        cpu1= int(input("ingrese un numero 1.piedra 2. papel 3. tijera\n"))
        print(type(cpu1))
        
        if(cpu1>0 and cpu1<3):
            cpu1= variable[cpu1 -1]
            print(cpu1)
            break
        else:
            print("fuera de rango ingrese una opcion valida")   
    except:
        print("ingresa una opcion valida")
        
        

print(cpu1)
#cpu1= variable[0]
#cpu2= variable[1] 
cpu2= random.choice(variable)
campo={cpu1,cpu2}
print(campo)
campo.union(cpu1,cpu2)

print("Usuario: "+ cpu1+" computadora: "+ cpu2)

if(("piedra" and "tijera" )in campo )==True:
    print( str(campo)  + "gana piedra")
    
elif(("piedra" and "papel" )in campo)==True:
    print( str(campo)  + "gana papel")
elif(("papel" and "tijera" )in campo)==True:
    print( str(campo)  + "gana tijera")
else:
    print("empate")
#hagalo sencillo  opcion 1 2 3
#si escribe tijera = 1 