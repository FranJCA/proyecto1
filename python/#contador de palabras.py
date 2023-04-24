#contador de palabras

print("contador de palabras")
palabra= input("ingresa una frase \n")

def contador (entrada):
    contar=0
    
    for i in entrada:
        if i==" ":
            contar  =contar+1;

            
    contar=contar+1;
    print(contar)
    return contar

cc=contador(palabra)
print ("Tu oracion se compone de un total de  " ,cc, " Palabras ")