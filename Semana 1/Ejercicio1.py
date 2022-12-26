'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana 

Cree un programa que utilice funciones para jugar a un juego de adivinar un número. 
El programa debe generar un número aleatorio entre 1 y 100, y luego pedir al usuario 
que adivine el número. Después de cada intento, el programa debe decirle al usuario
si su estimación es demasiado alta o demasiado baja.
El programa debe permitir al usuario hacer un máximo de 10 intentos para adivinar
el número. Si el usuario no adivina el número después de 10 intentos, el programa 
debe mostrar el número que se generó.
'''

import random

# Genera un número entero aleatorio del 1 al 100, ambos inclusive
def generar_aleatorio():
    return random.randint(1, 100)

# Informa al jugador si el número ingresado es mayor o menor al aleatorio por adivinar.
def estimacion(intento, aleatorio):
    if intento > aleatorio:
        print("El número ingresado es mayor que el número que tienes que adivinar.")
    else:
        print("El número es ingresado es menor que el número que tienes que adivinar.") 
    

def main(): 

    aleatorio = generar_aleatorio()
    print("Se generó un número aleatorio entre 1 y 100, intenta adivinarlo.")

    cuenta_intentos  = 0
    while cuenta_intentos < 10:
        cuenta_intentos += 1
        intento = int(input("Ingrese número: "))
        if intento == aleatorio:
            print("Excelente!!!")
            break
        else:
            estimacion(intento, aleatorio)
            print(f"Te quedan {str(10 - cuenta_intentos)} oportunidades para intentarlo.")

    if cuenta_intentos == 10:
        print(f"El número que no pudiste adivinar era {str(aleatorio)}")         
    
if __name__ == '__main__':
    main()