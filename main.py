from animal import Animal
from leon import Lion
from oso import Bear
from tigre import Tiger
from zoo import Zoo
import os

def menu(): 
    opcion = -1
    while opcion < 0 or opcion > 6:
        os.system("cls")
        print("Menú: John's Zoo")
        print("[1] Incorporar Animal")
        print("[2] Liberar Animal")
        print("[3] Listar Todos los Animales")
        print("[4] Listar Animales Carnívoros")
        print("[5] Listar Animales Herbívoros")
        print("[6] Listar Animales Omnívoros")
        print("[0] Salir")
        try:
            opcion = int(input("Ingrese su opción: "))
        except:
            input("El valor ingresado no parece ser un número...")
        if opcion < 0 or opcion > 6:
            input("Opción ingresada no válida, presione ENTER para continuar...")
    return opcion

######################################################################################
opcion = menu()
zoo1 = Zoo("John's Zoo")

while opcion > 0:
    if opcion == 1:
        print("Ingrese los datos del nuevo animal")
        animal_type = int(input("Ingrese el tipo de animal: (1) León (2) Oso (3) Tigre: "))
        if animal_type == 1:
            name = input("Ingrese nombre: ")
            age = int(input("Ingrese edad: "))
            habitat = input("Ingrese el habitat: ")
            heath_level = int(input("Ingrese nivel de salud: "))
            hapiness_level = int(input("Ingrese nivel de felicidad: "))
            melena = input("El león tiene melena? (Si / No): ")
            if melena == 'Si':
                melena = True
            else:    
                melena = False    
            new_animal = Lion(name, age, habitat, heath_level, hapiness_level, melena)
        elif animal_type == 2:
            pass

        if zoo1.add_animal(new_animal) == True:
            print("Felicititaciones, se incorporó el animal al Zoo...")
            zoo1.print_all_info()
        else:
            print("Lamentamos informar que el animal no pudo ser incoporado...")

    input("Presione ENTER para continuar... ")
    opcion = menu()

