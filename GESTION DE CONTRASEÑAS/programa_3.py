import time

password = "malboro"
seguir = True
chances = 0


while (seguir):
    intento = input ("ingrese contraseña: ")
    if (intento == password):
        print ("Welcome!")
        seguir = False
    else:
        print ("contraseña incorrecta.")
        chances += 1
        if (chances == 3):
            seguir = False
            print ("Pruebe mas tarde.")
        time.sleep(chances*1)

print ("fin del programa.")
