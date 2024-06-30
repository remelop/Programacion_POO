"""
El programa transforma las unidades de medida. Permite convertir entre kilogramos y libras y entre kilómetros y millas. Utiliza varios tipos de datos, como enteros, flotantes, cadenas y booleanos.
"""

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
print("1. Kilogramos a Libras")
print("2. Libras a Kilogramos")

opcion = int(input("Ingrese el número de la opción deseada: "))

# Variable booleana para verificar si la opción es válida
opcion_valida = True

# Realizar la conversión según la opción elegida
if opcion == 1:
    kilogramos = float(input("Ingrese la cantidad en kilogramos: "))
    libras = kg_a_libras(kilogramos)
    print(f"{kilogramos} kilogramos son {libras} libras.")
elif opcion == 2:
    libras = float(input("Ingrese la cantidad en libras: "))
    kilogramos = libras_a_kg(libras)
    print(f"{libras} libras son {kilogramos} kilogramos.")
else:
    opcion_valida = False
    print("Opción no válida. Por favor, reinicie el programa y seleccione una opción válida.")
    """
    Muestra un mensaje de error al usuario.

    Args:
      mensaje: El mensaje de error a mostrar (string).
    """

# Mensaje de finalización si la opción fue válida
if opcion_valida:
    print("Conversión completada con éxito.")
