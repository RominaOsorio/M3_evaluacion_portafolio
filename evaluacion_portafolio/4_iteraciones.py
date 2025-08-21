# https://github.com/RominaOsorio/M3_evaluacion_portafolio


def tabla_multiplicar(num):
    print(f"\nTabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def calcular_factorial(n):
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"\nEl factorial de {n} es {factorial}")


def menu():
    while True:
        print("\n=== Elige una opción ===")
        print("1. Generar tabla de multiplicar")
        print("2. Calcular factorial")
        print("3. Salir\n")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            try:
                num = int(input("\nIngrese un número para la tabla de multiplicar: "))
                tabla_multiplicar(num)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "2":
            try:
                n = int(input("\nIngrese un número para calcular su factorial: "))
                if n < 0:
                    print(
                        "Error: El factorial no está definido para números negativos."
                    )
                else:
                    calcular_factorial(n)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "3":
            print("\nHasta pronto!\n")
            break
        else:
            print("\nOpción inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()
