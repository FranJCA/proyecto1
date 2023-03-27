import random

number = random.randrange(1,50)
guess = int(input("adivina el numero magico, ingresa un numero entre el 1 y el 50 \n"))

while guess != number:
    
    if guess < number:
        print("el numero es mas alto, intenta de nuevo")
        guess = int(input("\n El numero magico esta entre 1 -50\n"))
    else:
        print("El numero es mas pequeño, intetalo denuevo")    
        guess = int(input("\n El numero magico esta entre 1 -50\n"))
        

print("Adivinastes el numero Has ganado!")