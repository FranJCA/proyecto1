#¿Cuál es mi acrónimo?

print("programa para saber tu acronimo")
acronimo = input("ingresa el nombre de la organizacion grupo u asociacion :\n")

ac = acronimo.split()
print("El acronimo es :")

conectores= ["de", "a", "y", "as","or","del"]

#print(ac)
for i in range(len(ac)):
    
    if(ac[i] in conectores): 
        pass
    else:
        print(ac[i][0],end="")







