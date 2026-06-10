# Guiones para los Videos de Presentación

Como parte de los entregables del Paso 1 y Paso 2, debes grabar videos explicativos. A continuación, te presento una guía estructurada para que sepas exactamente qué decir y mostrar.

---

## Video 1: Avance Inicial (Entregable del Paso 1)

**Objetivo:** Mostrar la configuración inicial, el repositorio y los diagramas.

1. **Introducción (0:00 - 0:15)**
   - "Hola, soy [Tu Nombre] y este es el avance inicial del Paso 1 para el proyecto del Generador Seguro de Contraseñas."
2. **Configuración del Repositorio (0:15 - 0:45)**
   - _Abre GitHub en tu navegador y muestra el repositorio creado._
   - "He configurado un repositorio en GitHub para el control de versiones. Aquí podemos ver el primer commit donde subí la estructura inicial y los diagramas."
3. **Explicación del Diagrama de Flujo (0:45 - 1:30)**
   - _Abre la imagen `diagrama-flujo.png`._
   - "Este es el diagrama de flujo desarrollado con la sintaxis de PlantUML. Muestra el proceso lógico: iniciamos leyendo la longitud y los criterios. Usamos un condicional para validar que los datos sean correctos. Luego, entramos en dos bucles: el primero garantiza que haya al menos un carácter de cada tipo seleccionado, y el segundo completa la contraseña hasta alcanzar la longitud deseada. Finalmente, barajamos los caracteres."
4. **Entorno de Desarrollo y Avance del Código (1:30 - 2:00)**
   - _Abre VSCode (o tu IDE) mostrando `generador.py`._
   - "He preparado el entorno utilizando Python y la librería nativa `secrets` (criptográficamente segura). En esta primera fase, he definido la estructura inicial de la aplicación por consola y los métodos principales."
   - "Con esto concluye el Paso 1."

---

## Video 2: Demostración y Avance del Desarrollo (Entregables del Paso 2)

**Objetivo:** Explicar el código lógico aplicado (bucles, condicionales) y demostrar que funciona.

1. **Introducción (0:00 - 0:10)**
   - "Bienvenidos al entregable del Paso 2. En esta fase he implementado toda la lógica del software en consola."
2. **Explicación del Código (0:10 - 1:30)**
   - _Muestra el archivo `generador.py` en pantalla._
   - "El código está organizado modularmente y comentado. Para cumplir con la rúbrica:"
   - **Condicionales:** "En la función `generar_password()`, usamos un bloque `if` para validar que la longitud sea mayor o igual a 8 y que el usuario haya aceptado al menos un criterio. Si esto no se cumple, el programa arroja un error en consola y vuelve a iterar."
   - **Bucles:** "Utilizamos múltiples estructuras repetitivas. Un bucle `while` para insistir en que el usuario introduzca datos correctos (como la longitud o 's/n'). Un bucle `for` itera sobre los criterios activos para asegurar la diversidad de caracteres. Finalmente, un bucle `while` se repite hasta que la contraseña alcance la longitud solicitada por el usuario."
3. **Demostración de Funcionamiento (1:30 - 2:30)**
   - _Abre la terminal integrada en VSCode y ejecuta `python generador.py`._
   - "Ahora vamos a probarlo en consola. Ingresamos una longitud de 16 y ponemos 's' en todos los criterios."
   - _La consola imprime la contraseña._
   - "Como ven, la clave se genera correctamente y de forma aleatoria."
   - _Inicia otra vez y pon longitud menor a 8, o 'n' a todas las opciones._
   - "Si pongo una longitud menor o rechazo todos los criterios, el condicional captura el error y me pide volver a intentarlo, demostrando que la validación lógica funciona."
4. **Cierre (2:30 - 2:40)**
   - "Todo el código de consola en Python ha sido subido a mi repositorio de GitHub, cumpliendo con los entregables del Paso 2."
