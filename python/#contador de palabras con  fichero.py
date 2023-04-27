#contador de palabras

print("contador de palabras fichero")
#palabra= input("ingresa una frase \n")

fichero = open('python\\texto.txt', 'r')
palabra= fichero.read()

print(palabra)
def contador (entrada):
    contar=0
    
    for i in entrada:
        if i==" ":
            contar  =contar+1;

            
    contar=contar+1;
    print(contar)
    return contar

fichero.close()
cc=contador(palabra)
print ("Tu oracion se compone de un total de  " ,cc, " Palabras ")