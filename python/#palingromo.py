#palingromo

print("programa saber si una palabra es palindromo")
#"".join(cadena.split())
palindormo1= "".join(input("ingresa una palabra ").lower().split())
palindormo2= "".join(reversed(palindormo1)).lower()


#print(palindormo1.split() + palindormo2.split())

if (palindormo1==palindormo2):
    print("Es palindromo")
else:   
    print(" no es palindromo")
