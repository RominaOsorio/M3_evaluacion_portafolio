# https://github.com/RominaOsorio/M3_evaluacion_portafolio


def pedir_numero(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: No ingresó ningún valor")
            continue
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido")


numero = pedir_numero("\nIngrese un número: ")

if numero > 0:
    print("El número es positivo\n")
elif numero < 0:
    print("El número es negativo\n")
else:
    print("El número es cero\n")
