import os, random, time
def menu():
    while True:
        limpiar_pantalla()
        print("""            1. Asignar sueldo aleatorios
            2. Clasificar sueldos
            3. Ver estadistica
            4. Reporte de sueldos
            5. Salir del programa """)
        try:
            opc = int(input("ingrese una opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("opción invalida vuelva a intentar")
                esperar_3_segundos()
        except:
            print("Error¡¡¡  Debes ingresar una opción entre 1 y el 5")
            esperar_3_segundos()
    

def generar_sueldos():
    for x in range (10):
        n = random.randint(300000,2500000)
        sueldos_ra = []
        sueldos_ra.append (n)
    print ("Sueldos Creados")
    esperar_2_segundos()
    return sueldos_ra

def clasificacion_sueldos(sueldos,Trabajadores):
    cont_trabajador = []
    cont_800000 = 0
    cont_20000000 = 0
    cont_sueldomayor = 0
    for x in range (10):
        if sueldos[x] >800000:
            cont_trabajador.append = x
            cont_800000+1
        elif sueldos[x] <=800000 and sueldos[x] >=2000000:
            cont_20000000+1
        else :
            cont_sueldomayor+1
    print("Sueldos menores a $800.000 Total: ",cont_800000)
    print("Nombre empleado    Sueldo")
    for x in range (cont_800000):
        print(f"{Trabajadores[cont_trabajador[x]]}  {sueldos[cont_trabajador[x]]}")
    print("\n Sueldos entre $800.000 y 2.000.000 Total: ",cont_20000000)
    for x in range (cont_20000000):
        print(f"{Trabajadores[cont_trabajador[x]]}  {sueldos[cont_trabajador[x]]}")
    print("\n Sueldos superiores a 2.000.000 Total: ",cont_sueldomayor)

def ver_estadistica(sueldos):
    promedio = 0
    for x in range (10):
        promedio = promedio + sueldos[x]
        mult = 1
        mult = mult * sueldos[x]
    promedio = promedio / 10
    media_geometrica = mult ** 1 / 10
    print("sueldo mas alto: ",sueldos[9])
    print("sueldo mas bajo: ",sueldos[0])
    print("promedio de sueldos: ",promedio)
    print("Media Geométrica: ",media_geometrica)
    esperar_3_segundos()

def esperar_2_segundos():
    time.sleep(2)

def esperar_3_segundos():
    time.sleep(3)

def limpiar_pantalla():
    os.system("cls")