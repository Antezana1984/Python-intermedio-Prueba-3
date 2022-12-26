'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana Pizarro

Cree un programa que permita jugar a piedra, papel o tijera. El programa debe
permitir al usuario jugar contra la computadora. El programa debe permitir al
usuario jugar tantas veces como desee. El programa debe mostrar el número de
victorias, derrotas y empates de cada jugador al final del juego.

Si el usuario ingrese un numero fuera del rango el programa debe seguir 
pidiendo un numero hasta que ingrese uno correcto.
Si el usuario ingrese un valor que no sea entero el programa debe seguir
pidiendo un numero hasta que ingrese uno correcto.

'''  
import random

'''
Genera una piedra, papel o tijera para la computadora
piedra = 1
papel  = 2
tijera = 3
'''
def generar_aleatorio():
    return random.randint(1, 3)

# Converierte los numeros 1, 2 o 3 a piedra, papel o tijera
def convierte(numero):
    if numero == 1:
        mano = "piedra"
    elif numero == 2:
        mano = "papel"
    else:
        mano = "tijera"
    return mano

'''
Dedice quien gana: devuelve 1 si gana la mano 1, 
devulve 2 si gana la mano 2, 
devulve 3 si hay empate
'''
def quien_gana(mano1, mano2):
    resultado = 0
    if mano1 == "piedra":
        if mano2 == "piedra":
            resultado = 3
        elif mano2 == "papel":
            resultado = 2
        elif mano2 == "tijera":
            resultado = 1

    elif mano1 == "papel":
        if mano2 == "piedra":
            resultado = 1
        elif mano2 == "papel":
            resultado = 3
        elif mano2 == "tijera":
            resultado = 2
    
    else:
        if mano2 == "piedra":
            resultado = 2
        elif mano2 == "papel":
            resultado = 1
        elif mano2 == "tijera":
            resultado = 3

    return resultado
    

def main(): 

    computador = 0
    jugador = 0
    empates = 0

    while True:
        respuesta = input("Desea jugar? (s/n) ")
        # Sólo se juega si dice "s", de otro modo hace break y muestra los contadores de resultados
        if respuesta == "s":
            resultado = 0

            #Se recibe la elección del jugador
            intento = int(input("Ingrese piedra, papel, o tijera: "))
            #El número elegido se convierte en texto (piedra, papel, o tijera)
            mano_jugador = convierte(intento)
            print("El jugador eligió: " + mano_jugador)

            #Se genera una elección para el computador
            aleatorio = generar_aleatorio()
            mano_computador = convierte(aleatorio)
            print("El computador jugó: " + mano_computador)

            #Se decide quien gana
            resultado = quien_gana(mano_computador, mano_jugador)

            #Se guanda el resultado en contadores
            if resultado == 1:
                computador += 1
                print("Ganó el computador.")
            elif resultado == 2:
                jugador += 1
                print("Ganó el jugador.")
            elif resultado == 3:
                empates += 1
                print("Hubo un empate.")                    
        else:
            break

    print(f"El computador ganó: {str(computador)}")
    print(f"El jugador ganó: {str(jugador)}")
    print(f"Empates: {str(empates)}")


if __name__ == '__main__':
    main()