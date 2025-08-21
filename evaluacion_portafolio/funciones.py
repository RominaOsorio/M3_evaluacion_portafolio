# https://github.com/RominaOsorio/M3_evaluacion_portafolio


def pedir_float(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Debes ingresar un número válido.")


def calcular_area():
    while True:
        print("\n--- Cálculo de Áreas ---")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            base = pedir_float("Base: ")
            altura = pedir_float("Altura: ")
            area = (base * altura) / 2
            print(f"\nÁrea del triángulo: {area:.2f}")

        elif opcion == "2":
            base = pedir_float("Base: ")
            altura = pedir_float("Altura: ")
            area = base * altura
            print(f"\nÁrea del rectángulo: {area:.2f}")

        elif opcion == "3":
            radio = pedir_float("Radio: ")
            area = 3.14159 * (radio**2)
            print(f"\nÁrea del círculo: {area:.2f}")

        elif opcion == "4":
            print("\nHasta luego!\n")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    calcular_area()
