import random, csv, statistics
import os
os.system("cls")



trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def sueldos_aleatorios():
    sueldos = []
    for _ in range(len(trabajadores)):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

def clasificar_sueldos(sueldos):
    menor_800k = []
    entre_800k_2m = []
    mayor_2m = []

    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menor_800k.append((trabajadores[i], sueldo))
        elif sueldo <= 2000000:
            entre_800k_2m.append((trabajadores[i], sueldo))
        else:
            mayor_2m.append((trabajadores[i], sueldo))

    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(menor_800k)}")
    print("Nombre empleado   Sueldo")
    for nombre, sueldo in menor_800k:
        print(f"{nombre:<17} ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800k_2m)}")
    print("Nombre empleado   Sueldo")
    for nombre, sueldo in entre_800k_2m:
        print(f"{nombre:<17} ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(mayor_2m)}")
    print("Nombre empleado   Sueldo")
    for nombre, sueldo in mayor_2m:
        print(f"{nombre:<17} ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")


def generar_reporte(sueldos):
    descuento_salud = 0.07
    descuento_afp = 0.12

    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for i, sueldo in enumerate(sueldos):
            desc_salud = sueldo * descuento_salud
            desc_afp = sueldo * descuento_afp
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([trabajadores[i], sueldo, desc_salud, desc_afp, sueldo_liquido])
    
    print("Reporte de sueldos generado correctamente en reporte_sueldos.csv")

def menu():
    sueldos = []

    while True:
        print("MENU")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            sueldos = sueldos_aleatorios()
            print("Sueldos aleatorios asignados correctamente.")
        elif opcion == 2:
            if sueldos:
                clasificar_sueldos(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == 3:
            print("ver estadistica")
        elif opcion == 4:
            if sueldos:
                generar_reporte(sueldos)
            else:
                print("Debe asignar sueldos aleatorios primero.")
        elif opcion == 5:
            print("Saliendo del programa...")
            print("Desarrollador Julio Ramirez")
            print("RUT: 22046282-k")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    menu()
