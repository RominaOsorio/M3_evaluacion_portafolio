# https://github.com/RominaOsorio/M3_evaluacion_portafolio


def pedir_string(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor.isalpha():
            return valor
        print("Error: Debe ingresar solo letras.")


def pedir_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido")


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido")


def pedir_bool(mensaje: str) -> bool:
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ["si", "no"]:
            return valor == "si"
        print("Error: Debe responder 'si' o 'no'")


nombre = pedir_string("\nIngrese su nombre: ")
edad = pedir_int("Ingrese su edad: ")
estatura = pedir_float("Ingrese su estatura: ")
estudiante = pedir_bool("¿Es estudiante? (si/no): ")

print("\n--- Datos Registrados ---\n")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Estatura: {estatura} m")
print(f"Estudiante: {estudiante}\n")
