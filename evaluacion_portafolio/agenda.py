# https://github.com/RominaOsorio/M3_evaluacion_portafolio


def validar_nombre(nombre: str) -> bool:
    return bool(nombre) and all(palabra.isalpha() for palabra in nombre.split())


def validar_telefono(telefono: str) -> bool:
    return telefono.isdigit()


def confirmar_si_no(mensaje: str) -> bool:
    while True:
        r = input(mensaje).strip().lower()
        if r == "si":
            return True
        if r == "no":
            return False
        print("Responda 'si' o 'no'")


def agregar_contacto(contactos: dict) -> None:
    nombre = input("Ingrese el nombre: ").strip()
    if not validar_nombre(nombre):
        print("\nEl nombre solo debe contener letras y no puede estar vacío.")
        return

    telefono = input("Ingrese el teléfono: ").strip()
    if not validar_telefono(telefono):
        print("\nEl teléfono solo debe contener números.")
        return

    contactos[nombre] = telefono
    print(f"\nContacto '{nombre}' agregado correctamente.")


def ver_contactos(contactos: dict) -> None:
    if not contactos:
        print("\nNo hay contactos registrados.")
    else:
        print("\nDiccionario de datos:")
        print(contactos)


def buscar_contactos(contactos: dict, termino: str) -> dict:
    t = termino.strip().lower()
    if not t:
        return {}
    return {k: v for k, v in contactos.items() if t in k.lower()}


def buscar_y_mostrar(contactos: dict) -> None:
    if not contactos:
        print("\nNo hay contactos registrados")
        return
    termino = input("Ingrese nombre a buscar: ").strip()
    if not validar_nombre(termino):
        print("Búsqueda inválida. Use solo letras.")
        return

    resultados = buscar_contactos(contactos, termino)
    if resultados:
        print("\nCoincidncias")
        print(resultados)
    else:
        print("\nNo se encontraron contactos que coincidan.")


def eliminar_contacto(contactos: dict) -> None:
    if not contactos:
        print("\nNo hay contactos registrados para eliminar.")
        return

    termino = input("Ingrese nombre del contacto a eliminar: ").strip()
    if not validar_nombre(termino):
        print("Nombre inválido. Use solo letras.")
        return

    coincidencias = buscar_contactos(contactos, termino)

    if not coincidencias:
        print("\nNo se encontraron contactos que coincidan.")
        return

    print("\nSe encontraron estas coincidencias:")
    for i, (k, v) in enumerate(coincidencias.items(), start=1):
        print(f"{i}. {k}: {v}")

    while True:
        exacto = input(
            "\nEscriba el nombre exacto tal como aparece para eliminar: "
        ).strip()
        if exacto in coincidencias:
            if confirmar_si_no(f"¿Eliminar definitivamente '{exacto}'? (si/no): "):
                del contactos[exacto]
                print("Contacto eliminado.")
            else:
                print("\nOperación cancelada.")
            return
        print(" El texto ingresado no coincide. Intente nuevamente.")


def menu():
    contactos = {}
    while True:
        print("\n=== Menú de Contactos ===")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            ver_contactos(contactos)
        elif opcion == "3":
            buscar_y_mostrar(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
