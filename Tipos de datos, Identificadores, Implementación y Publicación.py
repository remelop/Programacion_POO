"""
El programa transforma las unidades de medida. Permite convertir entre kilogramos y libras y entre kilómetros y millas. Utiliza varios tipos de datos, como enteros, flotantes, cadenas y booleanos.
"""

# Función para convertir kilómetros a millas
def km_a_millas(kilometros):
    millas_por_kilometro = 0.62
    millas = kilometros * millas_por_kilometro
    return millas

# Función para convertir millas a kilómetros
def millas_a_km(millas):
    kilometros_por_milla = 1.60
    kilometros = millas * kilometros_por_milla
    return kilometros

# Función para convertir kilogramos a libras
def kg_a_libras(kilogramos):
    libras_por_kg = 2.20
    libras = kilogramos * libras_por_kg
    return libras

# Función para convertir libras a kilogramos
def libras_a_kg(libras):
    kg_por_libra = 0.45
    kilogramos = libras * kg_por_libra
    return kilogramos

# Solicitar al usuario que elija el tipo de conversión
print("Seleccione el tipo de conversión:")
print("1. Kilómetros a Millas")
print("2. Millas a Kilómetros")
print("3. Kilogramos a Libras")
print("4. Libras a Kilogramos")

opcion = int(input("Ingrese el número de la opción deseada: "))

# Variable booleana para verificar si la opción es válida
opcion_valida = True

# Realizar la conversión según la opción elegida
if opcion == 1:
    kilometros = float(input("Ingrese la cantidad en kilómetros: "))
    millas = km_a_millas(kilometros)
    print(f"{kilometros} kilómetros son {millas} millas.")
elif opcion == 2:
    millas = float(input("Ingrese la cantidad en millas: "))
    kilometros = millas_a_km(millas)
    print(f"{millas} millas son {kilometros} kilómetros.")
elif opcion == 3:
    kilogramos = float(input("Ingrese la cantidad en kilogramos: "))
    libras = kg_a_libras(kilogramos)
    print(f"{kilogramos} kilogramos son {libras} libras.")
elif opcion == 4:
    libras = float(input("Ingrese la cantidad en libras: "))
    kilogramos = libras_a_kg(libras)
    print(f"{libras} libras son {kilogramos} kilogramos.")
else:
    opcion_valida = False
    print("Opción no válida. Por favor, reinicie el programa y seleccione una opción válida.")

# Mensaje de finalización si la opción fue válida
if opcion_valida:
    print("Conversión completada con éxito.")
