
'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana Pizarro

Búsqueda de correos electrónicos:

Cree un programa que lea desde un archivo de texto los correos electrónicos y los guarde en una lista. 
Cree una función que le permita al usuario buscar un correo electrónico en la lista. La función debe 
devolver la posición del correo electrónico en la lista. Si el correo electrónico no se encuentra en 
la lista, la función debe devolver -1. Imprima el resultado de la búsqueda, si encontró el correo 
electrónico o no, y en caso de que lo haya encontrado, la posición en la lista. También la cantidad de 
correos electrónicos que hay en la lista. Y finalmente el proveedor de correo electrónico si lo encontró.

Cree una función adicional que permita filtrar todos los correos de un mismo proveedor. Por ejemplo, 
si el usuario ingresa gmail.com, la función debe devolver todos los correos de gmail.com que se 
encuentran en la lista.

''' 
from io import open

# Limpia los correos del salto de línea
def limpiar_lista(lista_de_correos):
    for correo in range(len(lista_de_correos)):
        cadena = lista_de_correos[correo]
        cadena = cadena.replace("\n", "")
        lista_de_correos[correo] = cadena
    return lista_de_correos
        
# Busca el correo específico en la lista, devolviendo su ubicación
def buscar_correo(lista):
    correo = input("Ingrese correo a buscar (con minúsculas): ")
    ubición = -1
    for contador in range(len(lista)):
        if lista[contador] == correo:
            ubición = contador
    return ubición

# Busca el proveedor del correo, si el correo es ina.rangel@gmail.com, entrega sólo 'gmail'
def proveedor(correo):
    posicion_arroba = correo.find("@")
    proveedor = correo[posicion_arroba + 1:]

    posicion_del_punto = proveedor.find(".")
    
    # Retorna el proveedor sin el arroba ni el punto
    return proveedor[:posicion_del_punto]

# Busca el proveedor en la lista
def lista_de_proveedores(lista, proveedor_a_buscar):
    lista_filtrada = []
    for contador in range(len(lista)):
        cadena = lista[contador] 
        if cadena.find(proveedor_a_buscar) != -1:
            lista_filtrada.append(cadena)
    
    return lista_filtrada
    

def main(): 
    #Abre y cierra el archivo de los correos
    with open("correos.txt", "r") as archivo:
        lista_de_correos = archivo.readlines()

    # A los correos les quita el salto de línea final
    lista = limpiar_lista(lista_de_correos)

    #imprime la cantidad de correos
    print(f"La cantidad de correos en el archivo es: {len(lista)}")

    # Busca un correo en específico y devuelve ubicación, si no lo
    # encuentra devuelve  -1
    ubicacion = buscar_correo(lista)

    if ubicacion == -1:
        print("El correo no se encontró.")
    else:
        print(f"El correo se encontró, y su posición en la lista es : {ubicacion}")
        print("Se hace presente que el primer elemento es cero.")

        # Le dice al usuario cual es el proveedor del correo buscado
        print(f"El proveedor de correo es: {proveedor(lista[ubicacion])}")
    
    # Le dice al usuario cuales proveedores están disponibles para la búsqueda
    instrucciones ="""
    Escriba uno de los siguientes proveedores válidos:

    austin.rr.com
    austintx.com
    chase.com
    creativepanel.com
    fsddatasvc.com
    gmail.com
    honeywell.com
    hotmail.com
    intelligencepress.com
    mh.com
    natsource.com
    pira.com
    rssmb.com
    sanmarcos.net
    surffree.com
    tgn.net
    thedoghousemail.com
    webtv.net
    yahoo.com

    """
    print(instrucciones)


    proveedor_a_buscar = input("Ingrese proveedor a buscar (con minúsculas): ")
    
    # Imprime lista de correos del mismo proveedor, por ejemplo yahoo.com
    print(lista_de_proveedores(lista, proveedor_a_buscar))

if __name__ == '__main__':
    main()
    