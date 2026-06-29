# Proyecto Integrador: El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas

**Sistema:** Generador de Contraseñas Seguras en Python

## Datos del Proyecto

- **Integrantes:** [ESCRIBE TU NOMBRE AQUÍ]
- **Fecha:** Junio 2026

---

## Objetivo del Sistema

Desarrollar una solución informática automatizada mediante el uso de Python y estructuración lógica que resuelva el problema de la "fatiga de contraseñas". El sistema tiene como objetivo asistir a los usuarios en la creación ágil de contraseñas que cumplan con altos estándares de seguridad (combinación de letras, números y símbolos), contribuyendo así a mitigar vulnerabilidades y proteger la identidad digital en el entorno actual, evidenciando el impacto positivo de la tecnología en la seguridad de la sociedad.

---

## Descripción de Funcionalidades

1. **Generación Criptográficamente Segura:** Selecciona caracteres de forma aleatoria de diccionarios definidos (mayúsculas, minúsculas, números, símbolos).
2. **Diversidad Garantizada:** Asegura la inclusión de al menos un carácter por cada criterio seleccionado por el usuario.
3. **Longitud Personalizable y Segura:** Permite al usuario definir el tamaño de su contraseña exigiendo una longitud mínima (8 caracteres) para proteger frente a ataques de fuerza bruta.
4. **Validación de Entradas:** Manejo de excepciones (`try-except`) que impide el colapso del programa si el usuario ingresa letras cuando se espera un número, o selecciona opciones inválidas.
5. **Arquitectura Modular:** Dividido en múltiples módulos (`core.py`, `cli.py`, `config.py`) para una mejor escalabilidad, separación de intereses (lógica vs interfaz) y buenas prácticas de desarrollo.

---

## Estructura Lógica y Diagramas de Flujo

El algoritmo fue modelado utilizando la notación estándar en PlantUML y se divide en la planificación de los siguientes procesos:

- **`diagrama-principal.png`**: Muestra el bucle principal de ejecución, validación de la longitud y el flujo de los subprocesos.
- **`diagrama-sub1.png`**: Detalla el "Sub-proceso 1" que construye el conjunto de caracteres según los criterios ingresados.
- **`diagrama-sub2.png`**: Detalla el "Sub-proceso 2" que se encarga del relleno aleatorio y la mezcla (shuffle) para generar el resultado final.

---

## Cómo Ejecutar el Proyecto

1. Abre tu terminal o consola de comandos.
2. Clona o descarga este repositorio.
3. Navega hasta la carpeta del proyecto.
4. Ejecuta el módulo principal mediante:

```bash
python -m generador_password
```
