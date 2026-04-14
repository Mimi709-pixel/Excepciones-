#Maria Jose Bermudez Calderon 
#Samuel Jose Cardenas Martinez 


# ===============================
# PROGRAMAS CON EXCEPCIONES EN PYTHON
# ===============================

# 1. VALIDAR CORREO ELECTRÓNICO
print("\n--- VALIDAR CORREO ---")
try:
    correo = input("Ingrese su correo: ")

    if "@" not in correo or "." not in correo:
        raise ValueError("Correo inválido")

    print("Correo válido")

except ValueError as e:
    print(f"Error: {e}")


# 2. INVENTARIO DE ZAPATOS
print("\n--- INVENTARIO DE ZAPATOS ---")
try:
    inventario = [
        {"talla": 38, "color": "negro", "tipo": "deportivo"},
        {"talla": 40, "color": "blanco", "tipo": "casual"},
        {"talla": 37, "color": "rojo", "tipo": "formal"}
    ]

    talla = int(input("Ingrese la talla: "))
    color = input("Ingrese el color: ").lower()
    tipo = input("Ingrese el tipo: ").lower()

    encontrado = False

    for zapato in inventario:
        if zapato["talla"] == talla and zapato["color"] == color and zapato["tipo"] == tipo:
            encontrado = True
            break

    if encontrado:
        print("Zapato disponible")
    else:
        raise Exception("Zapato no disponible")

except ValueError:
    print("Error: la talla debe ser un número")
except Exception as e:
    print(f"Error: {e}")


# 3. CALCULAR EDAD
print("\n--- CALCULAR EDAD ---")
from datetime import datetime

try:
    nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    fecha_nac = datetime.strptime(nacimiento, "%Y-%m-%d")

    hoy = datetime.today()
    edad = hoy.year - fecha_nac.year

    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1

    print(f"Su edad es: {edad} años")

except ValueError:
    print("Error: formato de fecha incorrecto")


# 4. CÁLCULO DE NÓMINA
print("\n--- CÁLCULO DE NÓMINA ---")
try:
    sueldo = float(input("Ingrese su sueldo mensual: "))

    pago_quincena = sueldo / 2
    auxilio_transporte = 162000 / 2  # valor aproximado

    total = pago_quincena + auxilio_transporte

    print(f"Pago por 15 días: {pago_quincena}")
    print(f"Auxilio de transporte: {auxilio_transporte}")
    print(f"Total a pagar: {total}")

except ValueError:
    print("Error: debe ingresar un número válido")


# 5. GUARDAR 10 PALABRAS EN ARCHIVO
print("\n--- GUARDAR PALABRAS ---")
try:
    palabras = []

    for i in range(10):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        palabras.append(palabra)

    with open("palabras.txt", "w") as archivo:
        for p in palabras:
            archivo.write(p + "\n")

    print("Palabras guardadas correctamente en 'palabras.txt'")

except Exception as e:
    print(f"Error al guardar el archivo: {e}")