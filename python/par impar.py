#par impar

def parimpar( numero= int(input("ingrese un numero")), ):
    
    
    if numero% 2==0:
      return "par"
    else:
        return "impar"
    
    
try:
    print(parimpar())
except ValueError:
    print("el programa fallo porque se ingreso una letra o un numero flotante")