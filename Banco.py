import json
import csv
from datetime import datetime

cuentas = []
ancho = 50


def guardarJSON():
    with open("cuentas.json", "w", encoding="utf-8") as archivo:
        json.dump(cuentas, archivo, indent=4, ensure_ascii=False)

def cargarJSON():
    global cuentas
    try:
        with open("cuentas.json", "r", encoding="utf-8") as archivo:
            cuentas = json.load(archivo)
    except FileNotFoundError:
        cuentas = []


def guardarHistorialCSV(numero, nombre, cantidad, saldo):
    with open("historial_depositos.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([fecha, numero, nombre, cantidad, saldo])


def ingresarCuenta():
    print("=" * ancho)
    print("CREAR CUENTA".center(ancho))
    print("=" * ancho)

    while True:
        try:
            numero = int(input("NUMERO DE CUENTA: "))
            cedula = int(input("NUMERO DE CEDULA: "))
            nombre = input("NOMBRE Y APELLIDO: ").lower()

            cuenta = {
                "numero": numero,
                "cedula": cedula,
                "nombre": nombre,
                "dinero": 0
            }

            cuentas.append(cuenta)
            guardarJSON()

            print("\nCUENTA GUARDADA!")
            print(f"Numero: {numero}\nCedula: {cedula}\nNombre: {nombre}")
            break

        except ValueError:
            print("VALORES INCORRECTOS... VUELVA A INTENTARLO :(")


def ingresarDinero():
    print("=" * ancho)
    print("INGRESAR DINERO".center(ancho))
    print("=" * ancho)

    while True:
        try:
            print("1. Nombre y cédula")
            print("2. Número de cuenta")

            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                cedula = int(input("Ingrese su cédula: "))
                nombre = input("Ingrese su nombre: ").lower()
                usuario = next((c for c in cuentas if c["cedula"] == cedula and c["nombre"] == nombre), None)

            elif opcion == 2:
                numero = int(input("Ingrese el número de cuenta: "))
                usuario = next((c for c in cuentas if c["numero"] == numero), None)

            else:
                print("Opción inválida")
                continue

            if usuario:
                print(f"\nBIENVENID@ {usuario['nombre']}")

                cantidad = int(input("Ingrese la cantidad a depositar: "))
                usuario["dinero"] += cantidad

                
                guardarJSON()

                guardarHistorialCSV(usuario["numero"], usuario["nombre"], cantidad, usuario["dinero"])

                print(f"\nSE AGREGARON {cantidad} A LA CUENTA DE {usuario['nombre']}")
                print(f"SALDO ACTUAL: {usuario['dinero']}")

                break
            else:
                print("CUENTA NO ENCONTRADA")

        except ValueError:
            print("VALORES INCORRECTOS... VUELVA A INTENTARLO :(")


def verSaldo():
    print("=" * ancho)
    print("VER SALDO".center(ancho))
    print("=" * ancho)

    while True:
        try:
            numero = int(input("Ingrese el número de cuenta: "))

            usuario = next((c for c in cuentas if c["numero"] == numero), None)

            if usuario:
                print("\n--- SALDO ---")
                print(f"Cuenta: {usuario['numero']}")
                print(f"Cédula: {usuario['cedula']}")
                print(f"Nombre: {usuario['nombre']}")
                print(f"Saldo: {usuario['dinero']}")
                break
            else:
                print("CUENTA NO EXISTE... VUELVA A INTENTARLO")

        except ValueError:
            print("NUMERO INVALIDO")



cargarJSON()

while True:
    try:
        print("=" * ancho)
        print("BANCO".center(ancho))
        print("=" * ancho)

        print("1. Agregar cuenta")
        print("2. Depositar")
        print("3. Ver saldo")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            ingresarCuenta()
        elif opcion == 2:
            ingresarDinero()
        elif opcion == 3:
            verSaldo()
        else:
            print("OPCIÓN NO EXISTE")

    except ValueError:
        print("VALOR INVALIDO")
