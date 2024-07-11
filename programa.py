from funciones import *

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_random = []

while True:
    
    opc = menu()
    if opc == 1:
        limpiar_pantalla()
        sueldos_random = generar_sueldos()
        sueldos_random.sort
    elif opc == 2:
        limpiar_pantalla()
        clasificacion_sueldos(sueldos_random,trabajadores)
    elif opc == 3:
        limpiar_pantalla()
        ver_estadistica(sueldos_random)
    elif opc == 4:
        limpiar_pantalla()
        print("g")
        pass
    else:
        limpiar_pantalla()
        print("Finalizando programa...")
        print("Desarrollado por Felipe Melo")
        print("rut 21.553.968-7")