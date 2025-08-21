
## Evaluación de Portafolio - Python

Este proyecto corresponde a la evaluación final del modulo 3 del curso de Python, en el cual se aplican las competencias técnicas adquiridas a lo largo de las clases.
El objetivo es demostrar el dominio de los fundamentos del lenguaje Python mediante la implementación de programas simples, organizados en distintos archivos para mayor claridad.

Cada script aborda un requerimiento funcional específico, siguiendo las instrucciones planteadas en la evaluación.

---

### Tecnologías utilizadas
- Lenguaje: Python
- Control de versiones: Git y GitHub
- Entorno: Consola / Terminal

---

### `1_conversor.py`
Este archivo implementa un menú interactivo que permite al usuario elegir entre diferentes tipos de conversores.
Incluye:
1. Conversor de Temperatura → Convierte grados Celsius a Fahrenheit y Kelvin.
2. Conversor de Moneda → Convierte pesos chilenos (CLP) a dólares (USD) utilizando una tasa de cambio fija. Se valida que la cantidad ingresada de pesos sea un número entero.
3. Conversor de Longitud → Convierte metros a centímetros y kilómetros.
4. Opción de Salida → Permite finalizar el programa.

### Ejemplo de ejecución:

=== Conversores ===

- Conversor de Temperatura (°C a °F y K)
- Conversor de Moneda (Pesos a Dólares)
- Conversor de Longitud (Metros a cm y km)
- Salir
Seleccione una opción (1-4):

###  `2_formulario.py`
Este programa solicita información personal al usuario mediante entrada en consola y almacena cada dato en variables del tipo adecuado.
Implementa validación de datos para garantizar que el usuario ingrese información correcta, solicitando el dato nuevamente hasta que sea válido.

### Ejemplo de ejecución:

=== Campos solicitados ===

- Nombre (`str`) → Solo permite letras y espacios.
- Edad (`int`) → Debe ser un número entero.
- Estatura (`float`) → Debe ser un número decimal.
- Estudiante (`bool`) → Solo acepta `"si"` o `"no"`.

### `3_condicionales.py`
Programa que solicita al usuario un número y determina si es positivo, negativo o cero.
Incluye validación de entrada y alertas en consola para que el usuario solo pueda ingresar números válidos.

#### Funcionalidades:
- Valida que el valor ingresado sea un número (`float`).
- Muestra un mensaje de error si el usuario deja el campo vacío.
- Muestra un mensaje de error si el usuario ingresa letras o caracteres inválidos.
- Evalúa el número y determina si es positivo, negativo o cero.

### `4_iteraciones.py`
Este archivo implementa un menú que permite al usuario elegir entre generar una tabla de multiplicar o calcular el factorial de un número.
También incluye una opción para salir del programa.

#### Funcionalidades:
1. Tabla de multiplicar → Genera la tabla del número ingresado, desde 1 hasta 10.
2. Factorial → Calcula el factorial del número ingresado utilizando un ciclo `while`.
3. Salir → Finaliza el programa.
4. Validaciones → El programa muestra mensajes de error si el usuario ingresa letras, deja el campo vacío o proporciona un valor inválido.

### Ejemplo de ejecución:

=== Elige una opción ===
1. Generar tabla de multiplicar
2. Calcular factorial
3. Salir
Seleccione una opción (1/2/3):

### `5_agenda.py`
Este archivo implementa una agenda de contactos con validaciones, búsqueda flexible y almacenamiento en diccionarios.

#### Funcionalidades principales:

1. **Agregar contacto**
- Nombre: Acepta solo letras y espacios.
- Teléfono: solo números.
2. **Ver contactos**
- Imprime el diccionario completo.
3. **Buscar contacto**
- Búsqueda (case-insensitive).
- Muestra resultados como diccionario.
4. **Eliminar contacto**
- Busca sin distinguir mayúsculas/minúsculas.
- Lista coincidencias y exige escribir el nombre exacto para eliminar.
- Confirmación obligatoria con `"si"` o `"no"`.
5. **Salir**

#### Ejemplo de ejecución:

=== Menú Agenda ===
1. Agregar contacto
2. Ver contactos
3. Buscar contacto
4. Eliminar contacto
5. Salir
Seleccione una opción:

### `6_funciones.py`
Este archivo implementa un menú interactivo para calcular el área de diferentes figuras geométricas: triángulo, rectángulo y círculo.

#### Funcionalidades principales:

1. Calcular área de un triángulo
2. Calcular área de un rectángulo
3. Calcular área de un círculo
4. Salir

#### Ejemplo de ejecución:

=== Cálculo de áreas ===
1. Triángulo
2. Rectángulo
3. Círculo
4. Salir
Seleccione una opción:

### Cómo ejecutar los programas
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/evaluacion_portafolio.git
   cd evaluacion_portafolio

2. Ejecutar los archivo con Python

