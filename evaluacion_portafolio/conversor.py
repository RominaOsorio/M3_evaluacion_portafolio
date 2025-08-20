# # https://github.com/RominaOsorio/M3_evaluacion_portafolio

while True:
    print("\n=== Conversores ===\n")
    print("1. Conversor de Temperatura (°C a °F y K)")
    print("2. Conversor de Moneda (Pesos a Dólares)")
    print("3. Conversor de Longitud (Metros a cm y km)")
    print("4. Salir")

    opcion = input("\nSeleccione una opción (1-4):")

    if opcion == "1":
        celsius = float(input("Ingrese temperatura en °C: "))
        fahrenheit = (celsius * 9 / 5) + 32
        kelvin = celsius + 273.15
        print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F y {kelvin:.2f}K\n")

    elif opcion == "2":
        pesos = int(input("Ingrese cantidad en Pesos: "))
        tasa_cambio = 950
        dolares = pesos / tasa_cambio
        print(
            f"${pesos} pesos equivalen a ${dolares:.2f} dólares (1 USD = {tasa_cambio} pesos)"
        )

    elif opcion == "3":
        metros = float(input("Ingrese longitud en metros: "))
        centimetros = metros * 100
        kilometros = metros / 1000
        print(f"{metros} m equivalen a {centimetros:.2f} cm y {kilometros:.3f} km")

    elif opcion == "4":
        print("\nHasta luego!\n")
        break

    else:
        print("\nOpción inválida. Intente nuevamente.\n")
