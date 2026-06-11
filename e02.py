numerosecreto = 0 

import random
numerosecreto = random.randint(1,20)

intentos=6

print("adivina el numero entre el 1 y 20")
print("tienes solo 6 intentos")

for i in range(intentos):
    intentos=int(input("ingrese un numero"))
    
    if intentos == numerosecreto:
        print("¡correcto!, acertaste")
        
    elif intentos < numerosecreto:
         print("el numero es mayor")
    else:
        print("el numero es menor")

else:
     print("has perdido, el numero secreto era", numerosecreto)
        
        
        
        
        
        